import os
import json
import time
import datetime
from urllib.parse import urlparse
import streamlit as st


# ===============================
# SAFE JSON LOADER (VERY IMPORTANT)
# ===============================
def safe_load_json(path):
    """Load JSON safely even if file is missing, empty, or corrupted"""
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r") as f:
            content = f.read().strip()

            # empty file protection
            if content == "":
                return []

            return json.loads(content)

    except Exception:
        # corrupted json protection
        return []


# ===============================
# AI MODEL LOADING
# ===============================
@st.cache_resource
def load_model():
    from transformers import pipeline
    return pipeline("image-classification")


# ===============================
# SAVE CYBER CASE
# ===============================
def save_case(case):
    os.makedirs("cases", exist_ok=True)
    file = "cases/cases.json"

    # safely read existing data
    data = safe_load_json(file)

    case["timestamp"] = str(datetime.datetime.now())
    data.append(case)

    with open(file, "w") as f:
        json.dump(data, f, indent=4)


# ===============================
# SCANNING ANIMATION
# ===============================
def drishta_scan():
    progress = st.progress(0)
    status = st.empty()
    status.markdown("### 🧠 DRISHTA AI analysing media...")

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    status.empty()


# ===============================
# LINK ANALYSIS
# ===============================
def analyze_link(link):

    # add https automatically
    if not link.startswith(("http://", "https://")):
        link = "https://" + link

    domain = urlparse(link).netloc.lower()

    if "instagram" in domain:
        return "Instagram", "Medium"
    elif "youtube" in domain or "youtu.be" in domain:
        return "YouTube", "Medium"
    elif "telegram" in domain or "t.me" in domain:
        return "Telegram", "High"
    elif "twitter" in domain or "x.com" in domain:
        return "X (Twitter)", "Medium"
    elif "facebook" in domain:
        return "Facebook", "Medium"

    return "Unknown", "Low"


# ===============================
# SAVE CONTACT FORM
# ===============================
def save_contact(contact_data):
    """Save contact form submissions safely"""
    os.makedirs("contacts", exist_ok=True)
    file = "contacts/contacts.json"

    data = safe_load_json(file)

    contact_data["timestamp"] = str(datetime.datetime.now())
    data.append(contact_data)

    with open(file, "w") as f:
        json.dump(data, f, indent=4)