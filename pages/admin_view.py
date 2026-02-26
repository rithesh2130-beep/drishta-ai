import streamlit as st
from utils import safe_load_json


def render():
    st.title("📊 DRISHTA Admin Data Viewer")

    # require explicit submission each visit
    with st.form("admin_form"):
        code = st.text_input("Enter admin code", type="password")
        submit = st.form_submit_button("Unlock")

    if not submit or code != "RITHESH":
        if submit:
            st.error("Incorrect code")
        # either not submitted yet or wrong code - don't show anything else
        return

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
