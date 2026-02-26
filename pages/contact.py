import streamlit as st
from utils import save_contact


def render():
    st.title("Contact DRISHTA")
    st.markdown("""
<div class="card">
<h3>Get in Touch</h3>
Have questions or want to report an incident? Reach out to us.
</div>
""", unsafe_allow_html=True)

    # contact form
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")

        if submitted:
            if name and email and message:
                contact_data = {
                    "name": name,
                    "email": email,
                    "message": message
                }
                save_contact(contact_data)
                st.success("✅ Thank you! Your message has been saved. We'll get back to you soon.")
            else:
                st.error("⚠️ Please fill in all fields.")

    st.markdown("""---
<div style='text-align:center; margin-top:40px;'>
<p><strong>Developed by:</strong> <span style='color:#facc15;'>CYBERPUNKS</span></p>
<p style='color:gray; font-size:12px;'>AI Safety • Digital Justice • Ethical Technology</p>
</div>
""", unsafe_allow_html=True)
