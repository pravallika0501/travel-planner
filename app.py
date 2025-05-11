import streamlit as st
import pandas as pd
from geopy.distance import geodesic
from chatbot import chatbot_response
from streamlit_folium import st_folium
import folium

# ---------- Caching data ----------
@st.cache_data
def load_places():
    df = pd.read_csv("data/bangalore_tourist_places.csv")
    df.columns = df.columns.str.strip()
    return df

@st.cache_data
def load_restaurants():
    df = pd.read_csv("data/bangalore_restaurants.csv")
    df.columns = df.columns.str.strip()
    return df

# ---------- Utility functions ----------
def find_nearby_places(user_location, radius_km=5):
    places = load_places()
    places['Distance_km'] = places.apply(
        lambda row: geodesic(user_location, (row['Latitude'], row['Longitude'])).km,
        axis=1
    )
    return places[places['Distance_km'] <= radius_km].sort_values(by='Distance_km')

def find_nearby_restaurants(place_location, radius_km=3):
    restaurants = load_restaurants()
    restaurants['Distance_km'] = restaurants.apply(
        lambda row: geodesic(place_location, (row['Latitude'], row['Longitude'])).km,
        axis=1
    )
    return restaurants[restaurants['Distance_km'] <= radius_km].sort_values(by='Distance_km')

def estimate_budget(entry_fee, transport_cost=150, food_avg=300):
    return entry_fee + transport_cost + food_avg

# ---------- Streamlit UI ----------
st.set_page_config(page_title="NextGen Travel Planner", layout="wide")
st.title("🧳 NextGen Travel Planner")
st.markdown("Plan your trip smartly with AI-powered suggestions and budgeting!")

# ---------- User Location ----------
st.sidebar.header("Your Location")
user_lat = st.sidebar.number_input("Latitude", value=12.9716, format="%.6f")
user_lon = st.sidebar.number_input("Longitude", value=77.5946, format="%.6f")
user_location = (user_lat, user_lon)

# ---------- Nearby Places ----------
if st.sidebar.button("Suggest Nearby Places"):
    results = find_nearby_places(user_location)
    
    st.subheader("📍 Nearby Tourist Spots")
    if results.empty:
        st.warning("No places found within 5 km. Try a different location or increase radius.")
    else:
        for _, row in results.head(5).iterrows():  # Limit to top 5
            with st.expander(f"{row['Name']} ({row['Distance_km']:.2f} km)"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"📝 **Description**: {row['Type']}")
                    st.write(f"⏰ **Opening Hours**: {row['Timings']}")
                    st.write(f"🎟️ **Entry Fee**: ₹{row['Entry Fee']}")
                with col2:
                    budget = estimate_budget(row['Entry Fee'])
                    st.metric("Estimated Budget", f"₹{budget}")

                # Restaurant Suggestions
                st.markdown("🍽️ **Nearby Restaurants:**")
                restaurants = find_nearby_restaurants((row['Latitude'], row['Longitude'])).head(5)
                for _, res in restaurants.iterrows():
                    st.write(f"- {res['Restaurant Name']} ({res['Cuisine']}, ₹{res['Approx Cost for Two (INR)']})")

            


# ---------- Chatbot Section ----------
st.markdown("---")
st.subheader("💬 Ask our Travel Bot")

user_query = st.text_input("Type your travel question:")
if user_query:
    response = chatbot_response(user_query)
    st.success(response)
