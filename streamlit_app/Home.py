import streamlit as st
import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from app.main import run_trip

st.set_page_config(
    page_title="TripMate AI",
    page_icon="✈️",
    layout="wide",
)

st.title("🌍 TripMate AI")

user_input = st.text_area(
    "Describe your trip",
    placeholder="Example: Plan a 5-day family trip from Delhi to Goa with a budget of ₹30,000.",
)

if st.button("Generate Trip Plan"):
    if user_input.strip():

        with st.spinner("Planning your trip..."):
            result = run_trip(user_input)

        st.header("📋 Trip Plan")
        st.markdown(result.get("planner", "No plan available."))

        st.header("🌤 Weather")
        st.markdown(result.get("weather", "No weather information."))

        st.header("📍 Places")
        st.markdown(result.get("places", "No places information."))

        st.header("✈ Flights")
        st.markdown(result.get("flights", "No flight information."))

        st.header("🏨 Hotels")
        st.markdown(result.get("hotels", "No hotel information."))

        st.header("💰 Budget")
        st.markdown(result.get("budget", "No budget information."))

        st.header("🗓 Itinerary")
        st.markdown(result.get("itinerary", "No itinerary available."))

        st.header("✅ Final Reviewed Plan")
        st.markdown(result.get("final_plan", "No final plan available."))

    else:
        st.warning("Please enter your travel request.")