import streamlit as st
from utils import drishta_scan, analyze_link


def render():
    st.title("Fake Link Intelligence")

    link = st.text_input("Paste Suspicious Link")

    if link and st.button("Analyze Link"):

        drishta_scan()
        platform, risk = analyze_link(link)

        st.write(f"Platform Detected: **{platform}**")

        if risk == "High":
            st.error("High-Risk Distribution Channel")
        elif risk == "Medium":
            st.warning("Moderate Spread Risk")
        else:
            st.success("Low Risk Link")
