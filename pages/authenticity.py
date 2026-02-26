import streamlit as st
from PIL import Image
from utils import drishta_scan, analyze_link


def render(classifier):
    st.title("AI Authenticity Detection")

    uploaded_file = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])
    link_check = st.text_input("Optional: Paste Media Link")

    if st.button("Run Authenticity Analysis"):

        drishta_scan()

        # -------- LINK PLATFORM DETECTION --------
        if link_check:
            platform, risk = analyze_link(link_check)

            st.markdown("### 🔗 Platform Detection")
            st.write(f"Detected Platform: **{platform}**")

            if risk == "High":
                st.error("High-risk sharing environment")
            elif risk == "Medium":
                st.warning("Moderate resharing risk")
            else:
                st.success("Low distribution risk")

        # -------- IMAGE AI DETECTION --------
        if uploaded_file:

            image = Image.open(uploaded_file).convert("RGB")
            result = classifier(image)

            confidence = result[0]["score"]

            ai_prob = int(confidence * 100)
            real_prob = 100 - ai_prob

            st.markdown("""
<div class="card">
<h3>🧾 DRISHTA FINAL AUTHENTICITY REPORT</h3>
</div>
""", unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            col1.metric("AI Generated Probability", f"{ai_prob}%")
            col2.metric("Authenticity Probability", f"{real_prob}%")

            st.progress(ai_prob/100)

            if ai_prob >= 75:
                st.error("⚠️ Verdict: Highly likely AI-generated — NOT fully believable.")
            elif ai_prob >= 50:
                st.warning("⚠️ Verdict: Authenticity uncertain — verify before trusting.")
            else:
                st.success("✅ Verdict: Media appears believable and authentic.")
