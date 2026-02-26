import streamlit as st


def apply_styles():
    st.markdown("""
<style>
.stApp {background: linear-gradient(135deg,#020617,#0f172a); color:white;}
.block-container {
    padding-top: 1rem;
}
.card {
    background:#111827;
    padding:20px;
    border-radius:12px;
    box-shadow:0 0 20px rgba(255,255,255,0.05);
}
h1,h2,h3 {color:#facc15;}
.stButton>button {
    background:#facc15;
    color:black;
    border-radius:8px;
    font-weight:bold;
}
.topbar {
    background:#020617;
    padding:15px;
    border-radius:10px;
    margin-bottom:20px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
    color:#facc15;
}
</style>
""", unsafe_allow_html=True)


def header_bar():
    st.markdown(
        '<div class="topbar">👁️ DRISHTA AI — The Digital Witness</div>',
        unsafe_allow_html=True
    )


def galaxy_animation():
    # full-screen galaxy travel + single slow bass buss sound + breathing effect
    st.markdown("""
<style>
@keyframes starfield {
    from {background-position: 0 0;}
    to {background-position: -2000px 2000px;}
}
@keyframes breathe {
    0%,100% {transform: scale(1);}
    50% {transform: scale(1.02);}
}
.galaxy {
    position: fixed;
    top:0; left:0;
    width:100%; height:100%;
    background:black;
    animation: breathe 1s ease-in-out infinite;
    z-index:9999;
}
.stars {
    width:100%; height:100%;
    background: radial-gradient(circle, white 1px, transparent 1px) repeat;
    background-size: 20px 20px;
    animation: starfield 20s linear infinite;
}
</style>
<div class="galaxy"><div class="stars"></div></div>
<audio autoplay>
    <source src="https://www.soundjay.com/mechanical/sounds/mechanical-bass-01.mp3" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)

