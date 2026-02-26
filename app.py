import streamlit as st

from utils import load_model
import styles
from pages import auth_render, link_render, cyber_render, track_render, contact_render, admin_render

st.set_page_config(page_title="DRISHTA AI", layout="wide")

# ================= SESSION STATE =================
if "entered" not in st.session_state:
    st.session_state.entered = False

# ================= UI STYLE =================
styles.apply_styles()
styles.header_bar()

# ================= LANDING PAGE =================
if not st.session_state.entered:

    st.markdown(
        "<h1 style='text-align:center;color:#facc15;font-size:60px;'>👁️ DRISHTA AI</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<h3 style='text-align:center;'>Seeing Beyond Digital Illusion</h3>",
        unsafe_allow_html=True
    )

    st.markdown("""
<div style='text-align:center;font-size:20px;max-width:800px;margin:auto;'>
In the age of generative AI, reality can be fabricated.
Deepfakes and synthetic media are increasingly used for
harassment, impersonation, and psychological harm.

DRISHTA represents the ancient concept of the Witness —
an intelligence that sees truth beyond illusion.

Generative AI can fabricate reality through deepfakes and synthetic media.
DRISHTA acts as a digital witness — helping people verify truth,
detect manipulation, and protect dignity online.
</div>
""", unsafe_allow_html=True)

    # landing button with animation trigger
    c1,c2,c3 = st.columns([2,3,2])
    with c2:
        if st.button("🚀 Enter DRISHTA Platform", use_container_width=True):
            st.session_state.play_animation = True

    # if animation flag set, show galaxy animation then proceed
    if st.session_state.get("play_animation", False):
        styles.galaxy_animation()
        # let the video play and animation run for 5 seconds
        import time
        time.sleep(1)
        st.session_state.entered = True
        st.session_state.play_animation = False
        st.rerun()

    st.stop()

# ================= LOAD AI MODEL =================
classifier = load_model()

# ================= SIDEBAR =================
page = st.sidebar.radio(
    "DRISHTA Modules",
    [
        "👁️ AI Authenticity Check",
        "🔗 Fake Link Detection",
        "⚖️ Cyber Crime Report",
        "🔐 Private Case Tracking",
        "📩 Contact Us",
        "📊 Admin Viewer"
    ]
)

# =====================================================
# RENDER SELECTED PAGE
# =====================================================
if page == "👁️ AI Authenticity Check":
    auth_render(classifier)
elif page == "🔗 Fake Link Detection":
    link_render()
elif page == "⚖️ Cyber Crime Report":
    cyber_render()
elif page == "🔐 Private Case Tracking":
    track_render()
elif page == "📩 Contact Us":
    contact_render()
elif page == "📊 Admin Viewer":
    admin_render()

# ================= FOOTER =================
st.markdown("""
<hr>
<div style='text-align:center;'>
<p style='color:gray;'>DRISHTA AI — Ethical AI for Digital Justice</p>
<p style='color:#facc15; font-size:14px; font-weight:bold;'>Developed by CYBERPUNKS</p>
</div>
""", unsafe_allow_html=True)
