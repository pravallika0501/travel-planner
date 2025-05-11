# NextGen Travel Planner 🚀🌍  
An AI-powered intelligent tourist guide system that enhances travel experiences by providing personalized location-based suggestions, budget estimation, restaurant recommendations, and interactive chatbot support.

---

## 📌 Project Description

The **NextGen Travel Planner** is a smart web application designed to help travelers make informed decisions. It suggests nearby tourist places based on the user's current location, provides detailed information, estimates total travel costs, recommends restaurants, and includes a chatbot for interactive assistance.

---

## 🔧 Features

- 🔍 **Tourist Place Recommendations**: Suggests attractions near the user based on geolocation (within a 5 km radius).
- 💸 **Budget Estimation**: Calculates total trip cost including travel, entry fees, and food.
- 🍽️ **Restaurant Finder**: Recommends nearby restaurants based on cuisine, rating, and distance (within 3 km).
- 🤖 **Interactive Chatbot**: Provides help regarding travel tips, recommendations, and budget inquiries.
- 🗺️ **Visual Map Integration**: Displays tourist spots and restaurants on an interactive map.
- 📱 **User-Friendly Interface**: Built using Streamlit for simplicity and fast interaction.

---

## 🏗️ System Architecture

User Input → Streamlit UI → Backend Logic (Python) → Dataset Filtering → Recommendations → Output + Map Display


---

## 🛠️ Technologies Used

- **Frontend**: Streamlit
- **Backend**: Python 3.10
- **Libraries**:
  - `pandas` – data manipulation
  - `geopy` – distance calculation
  - `folium`, `streamlit-folium` – map visualization
  - `openai` (optional) – GPT integration for smart chatbot
- **Datasets**:
  - Tourist Places Dataset (CSV)
  - Restaurants Dataset (CSV)

---

## 📂 Project Structure
```bash
NextGen_Travel_Planner/
│
├── app.py # Main Streamlit application
├── data/
│ ├── tourist_places.csv # Tourist places dataset
│ └── restaurants.csv # Restaurant dataset
├── chatbot.py
├── requirements.txt # Required Python packages
└── README.md # This file
```


---

## 🚀 Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/NextGen_Travel_Planner.git
cd NextGen_Travel_Planner
```
2. **Install dependencies:**

```bash
pip install -r requirements.txt
```
3. **Run the application**
```bash
streamlit run app.py
```

---

## 🤖 Chatbot Logic
-User Intent Detection:
-Greetings
-Nearby place inquiries
-Budget-related questions
-Restaurant recommendations
-General travel advice
-Response Generation:
-Predefined answers for FAQs

---

## ✅ Results
-Successfully recommends nearby attractions and eateries.
-Provides useful budget insights.
-Simple and intuitive chatbot interaction.
-Positive feedback from testers regarding usability.

---

## 🧠 Future Enhancements
-🌐 Google Places API integration for real-time data.
-🧑‍💼 User profile-based personalized suggestions.
-🗺️ Route planning and itinerary builder.
-🏨 Hotel search and booking options.
-🧾 User reviews and rating system.
-🗣️ Multilingual chatbot and UI.
