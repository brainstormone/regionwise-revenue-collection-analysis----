"""
Region-Wise Revenue Contribution Analysis
Main Application Controller
MCA 2nd Year Capstone Project - ABES Engineering College
"""

from pathlib import Path

import pandas as pd
import streamlit as st

from src.ui import apply_custom_css
from src.data.loader import load_analysis_data


# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Region-Wise Revenue Contribution Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# 2. PROJECT PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "assets" / "abes-logo.png"
PAGES_DIR = BASE_DIR / "pages"


# =========================================================
# 3. GLOBAL STYLING
# =========================================================

apply_custom_css()


# =========================================================
# 4. ABES BRANDING
# =========================================================

if LOGO_PATH.is_file() and LOGO_PATH.stat().st_size > 100:
    st.logo(str(LOGO_PATH), size="large")


# =========================================================
# 5. LOAD DATABASE
# =========================================================

try:
    df_raw = load_analysis_data()
except Exception as error:
    st.error(f"Unable to load database records: {error}")
    st.stop()

if df_raw is None or df_raw.empty:
    st.error("No records were found in the database.")
    st.stop()


# =========================================================
# 6. VALIDATE REQUIRED DATABASE COLUMNS
# =========================================================

required_columns = ["region_name", "product_category"]
missing_columns = [
    column for column in required_columns
    if column not in df_raw.columns
]

if missing_columns:
    st.error(
        "Missing required database columns: "
        + ", ".join(missing_columns)
    )
    st.stop()


# =========================================================
# 7. PREPARE GLOBAL FILTER OPTIONS
# =========================================================

all_regions = sorted(
    df_raw["region_name"].dropna().astype(str).unique().tolist()
)

all_categories = sorted(
    df_raw["product_category"].dropna().astype(str).unique().tolist()
)
