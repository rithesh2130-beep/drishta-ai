import streamlit as st
import os
import json
from utils import drishta_scan


def render():
    st.title("Anonymous Case Tracking")

    case_input = st.text_input("Enter Case ID")

    file = "cases/cases.json"

    if case_input and os.path.exists(file):

        drishta_scan()
        with open(file, "r") as f:
            cases = json.load(f)

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
