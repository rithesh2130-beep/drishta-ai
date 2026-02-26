import streamlit as st
from utils import safe_load_json


def render():
    st.title("📊 DRISHTA Admin Data Viewer")

    # basic session-based access control so user must explicitly unlock
    if "admin_authenticated" not in st.session_state:
        st.session_state.admin_authenticated = False

    if not st.session_state.admin_authenticated:
        code = st.text_input("Enter admin code", type="password", key="admin_code")
        if st.button("Unlock"):
            if code == "RITHESH":
                st.session_state.admin_authenticated = True
            else:
                st.error("Incorrect code")
        # stop before rendering any data until correct code entered
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
