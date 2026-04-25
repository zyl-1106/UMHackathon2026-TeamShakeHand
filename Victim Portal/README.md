# Module 1: Victim Portal - Z.AI Emergency Portal

## Overview
This is the mobile-optimized frontend for flood victims to broadcast SOS signals. It is designed for low-bandwidth and high-stress scenarios, featuring a minimalist, button-driven interface to ensure data integrity even when users are panicking.

## Key Features
* **Standardized SOS Inputs:** Uses radio buttons for water levels and hazards to keep data packets extremely small for mesh transmission.
* **Dead Phone Protocol:** Automatically triggers a final SOS with GPS coordinates when battery drops below 5% and activates an emergency LED beacon.
* **Survival Tools:** Integrated on-screen visual flasher and audio siren to help rescuers locate victims in the dark.
* **Offline Mesh Simulation:** Implements a local Store-and-Forward queue to hold SOS packets until a network node is found.

## Technical Details
* **Framework:** Streamlit (Python)
* **API Integration:** Connects to Z.AI GLM for distress signal normalization.
* **Database:** Real-time sync with Firebase Firestore.

## How to Run Locally
1. Navigate to this directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Ensure `.streamlit/secrets.toml` is configured with Firebase and AI API keys.
4. Run the app: `streamlit run app.py`
