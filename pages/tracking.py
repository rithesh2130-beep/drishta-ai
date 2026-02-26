import streamlit as st
import os
from utils import safe_load_json


def render():
    st.title("🔐 Anonymous Case Tracking")

    st.markdown("""
Enter your **Anonymous Case ID** to privately monitor investigation progress.
Your identity is never stored or revealed.
""")

    case_input = st.text_input("Enter Case ID")

    file = "cases/cases.json"

    # Ensure directory exists (cloud-safe)
    os.makedirs("cases", exist_ok=True)

    # SAFE JSON LOAD (prevents all deployment crashes)
    cases = safe_load_json(file)

    # ===============================
    # SEARCH CASE
    # ===============================
    if case_input:

        found = False

        for case in cases:
            if case.get("case_id") == case_input:

                found = True

                st.success("✅ Case Found")

                st.write(f"**Platform:** {case.get('platform', 'Unknown')}")
                st.write(f"**Status:** {case.get('status', 'Under Investigation')}")
                st.write(f"**Submitted:** {case.get('timestamp', 'N/A')}")

                st.progress(60)

                st.info("""
🔎 DRISHTA monitoring system is actively tracking harmful media spread
and coordinating automated reporting workflows.
""")

                break

        if not found:
            st.error("❌ Invalid Case ID or case not yet registered.")