
"""
Region-Wise Revenue Contribution Analysis
Main Application Controller
MCA 2nd Year Capstone Project - ABES Engineering College
Mentor: Prof. Kalpana Dwivedi
"""

from pathlib import Path

import streamlit as st
import pandas as pd

from src.ui import apply_custom_css
from src.data.loader import load_analysis_data


# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Region-Wise Revenue Contribution Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. GLOBAL STYLING
# =========================================================

apply_custom_css()


# =========================================================
# 3. ABES LOGO
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

logo_path = BASE_DIR / "assets" / "abes-logo.png"

if logo_path.is_file() and logo_path.stat().st_size > 100:

    st.logo(
        str(logo_path),
        size="large"
    )

else:
    st.sidebar.error(
        "ABES logo not found. Check assets/abes-logo.png."
    )


# =========================================================
# 4. LOAD DATASET
# =========================================================

try:
    df_raw = load_analysis_data()

except Exception as error:
    st.error(f"Unable to load database records: {error}")
    st.stop()


if df_raw.empty:
    st.error("No records found in the database.")
    st.stop()


# =========================================================
# 5. PREPARE FILTER OPTIONS
# =========================================================

all_regions = sorted(
    df_raw["region_name"]
    .dropna()
    .unique()
    .tolist()
)

all_categories = sorted(
    df_raw["product_category"]
    .dropna()
    .unique()
    .tolist()
)

all_segments = (
    ["All"] +
    sorted(
        df_raw["customer_segment"]
        .dropna()
        .unique()
        .tolist()
    )
    if "customer_segment" in df_raw.columns
    else ["All"]
)


# Prepare available years

if "order_date" in df_raw.columns:

    date_values = pd.to_datetime(
        df_raw["order_date"],
        errors="coerce"
    ).dropna()

    available_years = sorted(
        date_values.dt.year.unique().tolist()
    )

else:
    available_years = []


# =========================================================
# 6. INITIALIZE FILTER SESSION STATE
# =========================================================

if "filter_regions" not in st.session_state:
    st.session_state["filter_regions"] = all_regions

if "filter_categories" not in st.session_state:
    st.session_state["filter_categories"] = all_categories

if "filter_segment" not in st.session_state:
    st.session_state["filter_segment"] = "All"

if available_years:

    default_years = (
        int(min(available_years)),
        int(max(available_years))
    )

    if "filter_years" not in st.session_state:
        st.session_state["filter_years"] = default_years


# Keep stored selections valid if dataset options change

st.session_state["filter_regions"] = [
    region
    for region in st.session_state["filter_regions"]
    if region in all_regions
]

st.session_state["filter_categories"] = [
    category
    for category in st.session_state["filter_categories"]
    if category in all_categories
]

if st.session_state["filter_segment"] not in all_segments:
    st.session_state["filter_segment"] = "All"


# =========================================================
# 7. SIDEBAR FILTERS
# =========================================================

st.sidebar.markdown("### Global Slicing Filters")

st.sidebar.caption(
    "Filter selections apply across all dashboard pages."
)


# Region filter

st.sidebar.multiselect(
    "Region",
    options=all_regions,
    key="filter_regions"
)


# Product category filter

st.sidebar.multiselect(
    "Product Category",
    options=all_categories,
    key="filter_categories"
)


# Customer segment filter

st.sidebar.selectbox(
    "Customer Segment",
    options=all_segments,
    key="filter_segment"
)


# Year range filter

if available_years:

    minimum_year = int(min(available_years))
    maximum_year = int(max(available_years))

    current_years = st.session_state["filter_years"]

    current_years = (
        max(minimum_year, min(maximum_year, current_years[0])),
        max(minimum_year, min(maximum_year, current_years[1]))
    )

    if current_years[0] > current_years[1]:
        current_years = (minimum_year, maximum_year)

    st.session_state["filter_years"] = current_years

    if minimum_year < maximum_year:

        st.sidebar.slider(
            "Year Range",
            min_value=minimum_year,
            max_value=maximum_year,
            key="filter_years"
        )

    else:
        st.sidebar.caption(f"Available year: {minimum_year}")


# =========================================================
# 8. RESET FILTERS
# =========================================================

if st.sidebar.button(
    "↻ Reset All Filters",
    use_container_width=True
):

    st.session_state["filter_regions"] = all_regions
    st.session_state["filter_categories"] = all_categories
    st.session_state["filter_segment"] = "All"

    if available_years:
        st.session_state["filter_years"] = (
            int(min(available_years)),
            int(max(available_years))
        )

    st.rerun()


# =========================================================
# 9. SIDEBAR SYSTEM STATUS
# =========================================================

st.sidebar.markdown("---")

st.sidebar.markdown("### System Status")

st.sidebar.success("SQLite Database Active")

st.sidebar.info(
    f"Records Ingested: {len(df_raw):,}"
)

st.sidebar.caption(
    "MCA Capstone Project • ABES Engineering College"
)

st.sidebar.markdown(
    """
    <div style="
        border-top:1px solid #303644;
        padding-top:12px;
        margin-top:15px;
        color:#94A3B8;
        font-size:11px;
        line-height:1.7;
    ">
        Region-Wise Revenue Contribution Analysis<br>
        Mentor: Prof. Kalpana Dwivedi
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 10. MULTIPAGE NAVIGATION
# =========================================================

pages = [

    st.Page(
        "pages/01_Overview.py",
        title="01 Overview",
        icon="📊",
        default=True
    ),

    st.Page(
        "pages/02_Longitudinal_Trends.py",
        title="02 Longitudinal Trends",
        icon="📈"
    ),

    st.Page(
        "pages/03_Regional_Comparison.py",
        title="03 Regional Comparison",
        icon="🌍"
    ),

    st.Page(
        "pages/04_Product_Pareto.py",
        title="04 Product Pareto",
        icon="📦"
    ),

    st.Page(
        "pages/05_Profitability_Insights.py",
        title="05 Profitability Insights",
        icon="💹"
    ),

    st.Page(
        "pages/06_Statistical_Testing.py",
        title="06 Statistical Testing",
        icon="📐"
    ),

    st.Page(
        "pages/07_Data_Quality_Export.py",
        title="07 Data Quality & Export",
        icon="📁"
    ),

    st.Page(
        "pages/08_About.py",
        title="08 About",
        icon="ℹ️"
    )

]


# Run selected page

navigation = st.navigation(pages)

navigation.run()
