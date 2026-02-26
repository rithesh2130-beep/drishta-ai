import streamlit as st
from utils import safe_load_json


def render():

    st.title("📊 DRISHTA Admin Panel")

    st.markdown("""
This panel is restricted for **internal monitoring only**.
Unauthorized access is not permitted.
""")

    # =====================================================
    # ADMIN AUTHENTICATION
    # =====================================================
    with st.form("admin_form"):
        code = st.text_input("Enter Admin Access Code", type="password")
        submit = st.form_submit_button("🔓 Unlock Panel")

    # stop execution unless correct login
    if not submit:
        st.info("🔒 Admin authentication required.")
        st.stop()

    if code != "RITHESH":
        st.error("❌ Incorrect access code")
        st.stop()

    # =====================================================
    # ACCESS GRANTED
    # =====================================================
    st.success("✅ Admin Access Granted")
    st.warning("Demo-only admin dashboard (prototype environment)")

    st.divider()

    # =====================================================
    # CYBER CASE DATA
    # =====================================================
    st.header("⚖️ Cyber Crime Cases")

    cases = safe_load_json("cases/cases.json")

    if cases:
        st.dataframe(cases, use_container_width=True)
    else:
        st.info("No cyber cases recorded yet.")

    st.divider()

    # =====================================================
    # CONTACT FORM DATA
    # =====================================================
    st.header("📩 Contact Submissions")

    contacts = safe_load_json("contacts/contacts.json")

    if contacts:
        st.dataframe(contacts, use_container_width=True)
    else:
        st.info("No contact submissions yet.")