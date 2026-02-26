import streamlit as st
from utils import safe_load_json


def render():
    st.title("📊 DRISHTA Admin Data Viewer")

    # simple access control
    code = st.text_input("Enter admin code", type="password")
    if code != "RITHESH":
        if code:
            st.error("Incorrect code")
        st.stop()

    st.warning("Demo-only admin panel (not for production)")

    # ================= CASES =================
    st.header("⚖️ Cyber Cases")

    cases = safe_load_json("cases/cases.json")

    if cases:
        st.dataframe(cases)
    else:
        st.info("No cases stored yet.")

    # ================= CONTACTS =================
    st.header("📩 Contact Messages")

    contacts = safe_load_json("contacts/contacts.json")

    if contacts:
        st.dataframe(contacts)
    else:
        st.info("No contact submissions yet.")
