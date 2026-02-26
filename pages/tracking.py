import streamlit as st
import os
import json


def render():
    st.title("Anonymous Case Tracking")

    case_input = st.text_input("Enter Case ID")

    file = "cases/cases.json"

    # Ensure cases directory exists
    os.makedirs("cases", exist_ok=True)

    # Create empty cases.json if it doesn't exist
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump([], f)

    # Safe loading
    try:
        with open(file, "r") as f:
            cases = json.load(f)
    except json.JSONDecodeError:
        cases = []

    # Search for case if input provided
    if case_input:
        for case in cases:
            if case["case_id"] == case_input:
                st.success("Case Found")
                st.write(f"Platform: {case['platform']}")
                st.write(f"Status: {case['status']}")
                st.write(f"Submitted: {case['timestamp']}")
                st.progress(60)
                break
        else:
            st.error("Invalid Case ID")
