import os
import json
import time
from urllib.parse import urlparse
import streamlit as st


@st.cache_resource
# load_model remains in main app or maybe here
# but we provide it as an export as well

def load_model():
    from transformers import pipeline
    return pipeline("image-classification")


def save_case(case):
    os.makedirs("cases", exist_ok=True)
    file = "cases/cases.json"

    if os.path.exists(file):
        try:
            with open(file, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []
    else:
        data = []

    data.append(case)

    with open(file, "w") as f:
        json.dump(data, f, indent=4)


# simple scanning animation shared across pages

def drishta_scan():
    progress = st.progress(0)
    status = st.empty()
    status.markdown("### 🧠 DRISHTA AI analysing media...")

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    status.empty()


def analyze_link(link):
    # add https if missing
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
def save_contact(contact_data):
    """Save contact form submissions to database"""
    os.makedirs("contacts", exist_ok=True)
    file = "contacts/contacts.json"

    if os.path.exists(file):
        with open(file, "r") as f:
            data = json.load(f)
    else:
        data = []

    import datetime
    contact_data["timestamp"] = str(datetime.datetime.now())
    data.append(contact_data)

    with open(file, "w") as f:
        json.dump(data, f, indent=4)
