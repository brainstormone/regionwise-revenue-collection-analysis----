
"""
UI Framework & Reusable Components
Region-Wise Revenue Contribution Analysis
MCA 2nd Year Capstone Project - ABES Engineering College
"""

from pathlib import Path
from html import escape
from typing import List, Dict, Any, Optional

import streamlit as st


# =========================================================
# 1. GLOBAL CUSTOM CSS
# =========================================================

def apply_custom_css() -> None:
    """Apply the ABES executive dashboard design system."""

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --navy: #241018;
        --navy-light: #3B1724;
        --maroon: #9B1835;
        --maroon-dark: #6F1028;
        --background: #F7F4F5;
        --card: #FFFFFF;
        --text: #172033;
        --muted: #718096;
        --border: #E9DDE1;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
    }

    .stApp {
        background: var(--background);
    }

    .block-container {
        max-width: 1500px !important;
        padding: 1.2rem 2rem 2rem !important;
    }

    /* Remove unnecessary decoration */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {
        background: var(--navy) !important;
        border-right: 1px solid #252B3A !important;
    }

    section[data-testid="stSidebar"] > div {
        background: var(--navy) !important;
    }

    section[data-testid="stSidebar"] * {
        color: #E5E7EB;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #FFFFFF !important;
    }

    /* Navigation links */

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] {
        padding-top: 8px;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a {
        background: transparent !important;
        border-radius: 7px !important;
        margin: 3px 8px !important;
        padding: 10px 12px !important;
        border-left: 3px solid transparent !important;
