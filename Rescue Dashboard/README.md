# Module 2: Rescue Dashboard - Z.AI Emergency Portal

## Overview
The Rescue Dashboard serves as the centralized Command & Control station for emergency responders. It transforms raw, fragmented SOS data into structured, prioritized mission cards, allowing commanders to deploy assets efficiently.

## Key Features
* **Agentic Priority Engine:** Automatically categorizes missions from P0 (Critical) to P3 (Stable) based on spatial reasoning and context analysis.
* **Hotzone Visualization:** An interactive map powered by PyDeck that visualizes SOS density and mission status (Red: Pending, Blue: En Route, Grey: Rescued).
* **Mission Lifecycle Management:** Tracks the flow of rescue operations from dispatch to safe resolution with real-time Firebase synchronization.
* **Asset Tracking:** Live monitoring of available rescue units (Helicopters, Boats, Medics, 4x4 Units).

## Technical Details
* **Framework:** Streamlit (Python)
* **Mapping:** PyDeck (Spatial Data Visualization)
* **Backend:** Firebase Firestore Admin SDK.

## How to Run Locally
1. Navigate to this directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Ensure `.streamlit/secrets.toml` is configured with Firebase Admin credentials.
4. Run the app: `streamlit run rescue_dashboard.py`
