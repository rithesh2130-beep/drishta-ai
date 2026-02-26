import streamlit as st
import random
import datetime
from utils import drishta_scan, analyze_link, save_case


def render():
    st.title("Cyber Protection Workflow")

    abuse_link = st.text_input("Paste Abusive Media Link")

    if abuse_link and st.button("Initiate Protection"):

        drishta_scan()
        case_id = "DR-" + str(random.randint(10000, 99999))
        platform, _ = analyze_link(abuse_link)

        st.success("Protection Workflow Started")
        st.info(f"Anonymous Case ID: {case_id}")

        st.write("✔ Takedown request simulated")
        st.write("✔ Duplicate monitoring activated")
        st.write("✔ Cyber complaint prepared")

        case = {
            "case_id": case_id,
            "platform": platform,
            "status": "Under Investigation",
            "timestamp": str(datetime.datetime.now())
        }

        save_case(case)

        report = f"""
DRISHTA INCIDENT REPORT
Case ID: {case_id}
Platform: {platform}
Timestamp: {datetime.datetime.now()}
"""

        st.download_button("Download Complaint Report", report, "DRISHTA_Report.txt")
