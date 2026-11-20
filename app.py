
"""
Region-Wise Revenue Contribution Analysis
Main Application Controller
MCA 2nd Year Capstone Project - ABES Engineering College
Mentor: Prof. Kalpana Dwivedi
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
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. PROJECT PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "abes-logo.png"


# =========================================================
# 3. GLOBAL STYLING
# =========================================================

apply_custom_css()


# =========================================================
# 4. ABES LOGO
# =========================================================

if LOGO_PATH.is_file() and LOGO_PATH.stat().st_size > 100:

    st.logo(
        str(LOGO_PATH),
        size="large"
    )

else:

    st.sidebar.warning(
        "ABES logo not found. Check assets/abes-logo.png."
    )


# =========================================================
# 5. LOAD DATABASE
# =========================================================

try:

    df_raw = load_analysis_data()

except Exception as error:

    st.error(
        f"Unable to load database records: {error}"
    )

    st.stop()


if df_raw is None or df_raw.empty:

    st.error(
        "No records were found in the database."
    )

    st.stop()


# =========================================================
# 6. VALIDATE REQUIRED COLUMNS
# =========================================================

required_columns = [
    "region_name",
    "product_category"
]

missing_columns = [
    column
    for column in required_columns
    if column not in df_raw.columns
]

if missing_columns:

    st.error(
        "Required database columns are missing: "
        + ", ".join(missing_columns)
    )

    st.stop()


# =========================================================
# 7. PREPARE FILTER OPTIONS
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


if "customer_segment" in df_raw.columns:

    all_segments = (
        ["All"]
        + sorted(
            df_raw["customer_segment"]
            .dropna()
            .unique()
            .tolist()
        )
    )

else:

    all_segments = ["All"]


# Prepare available years

available_years = []

if "order_date" in df_raw.columns:

    parsed_dates = pd.to_datetime(
        df_raw["order_date"],
        errors="coerce"
    )

    available_years = sorted(
        parsed_dates.dropna().dt.year.unique().tolist()
    )


# =========================================================
# 8. INITIALIZE SESSION STATE
# =========================================================

if "filter_regions" not in st.session_state:

    st.session_state["filter_regions"] = all_regions


if "filter_categories" not in st.session_state:

    st.session_state["filter_categories"] = all_categories


if "filter_segment" not in st.session_state:

    st.session_state["filter_segment"] = "All"


if available_years:

    default_year_range = (
        int(min(available_years)),
        int(max(available_years))
    )

    if "filter_years" not in st.session_state:

        st.session_state["filter_years"] = default_year_range


# Remove selections that are no longer available

st.session_state["filter_regions"] = [
    value
    for value in st.session_state["filter_regions"]
    if value in all_regions
]

st.session_state["filter_categories"] = [
    value
    for value in st.session_state["filter_categories"]
    if value in all_categories
]

if st.session_state["filter_segment"] not in all_segments:

    st.session_state["filter_segment"] = "All"


# =========================================================
# 9. SIDEBAR FILTERS
# =========================================================

st.sidebar.markdown(
    "### Global Slicing Filters"
)

st.sidebar.caption(
    "Filter selections apply across dashboard pages."
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

    min_year = int(min(available_years))
    max_year = int(max(available_years))

    current_range = st.session_state["filter_years"]

    # Keep the saved range within the available years

    start_year = max(
        min_year,
        min(max_year, int(current_range[0]))
    )

    end_year = max(
        min_year,
        min(max_year, int(current_range[1]))
    )

    if start_year > end_year:

        start_year = min_year
        end_year = max_year

    st.session_state["filter_years"] = (
        start_year,
        end_year
    )

    if min_year < max_year:

        st.sidebar.slider(
            "Year Range",
            min_value=min_year,
            max_value=max_year,
            key="filter_years"
        )

    else:

        st.sidebar.caption(
            f"Available year: {min_year}"
        )


# =========================================================
# 10. RESET FILTERS
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
# 11. SIDEBAR SYSTEM STATUS
# =========================================================

st.sidebar.markdown("---")

st.sidebar.markdown(
    "### System Status"
)

st.sidebar.success(
    "SQLite Database Active"
)

st.sidebar.info(
    f"Records Ingested: {len(df_raw):,}"
)

st.sidebar.markdown(
    """
    <div style="
        border-top: 1px solid #303644;
        padding-top: 12px;
        margin-top: 15px;
        color: #94A3B8;
        font-size: 11px;
        line-height: 1.8;
    ">
        Region-Wise Revenue Contribution Analysis<br>
        MCA 2nd Year Capstone Project<br>
        ABES Engineering College<br>
        Mentor: Prof. Kalpana Dwivedi
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 12. MULTIPAGE NAVIGATION
# =========================================================

overview_page = BASE_DIR / "pages" / "01_Overview.py"

trends_page = BASE_DIR / "pages" / "02_Longitudinal_Trends.py"


# Validate page files before registering navigation

if not overview_page.is_file():

    st.error(
        "Overview page not found: pages/01_Overview.py"
    )

    st.stop()


if not trends_page.is_file():

    st.error(
        "Longitudinal Trends page not found: "
        "pages/02_Longitudinal_Trends.py"
    )

    st.stop()


pages = [

    st.Page(
        str(overview_page),
        title="01 Overview",
        icon="📊",
        default=True
    ),

    st.Page(
        str(trends_page),
        title="02 Longitudinal Trends",
        icon="📈"
    )

]


# =========================================================
# 13. RUN APPLICATION NAVIGATION
# =========================================================

navigation = st.navigation(
    pages,
    position="sidebar"
)

navigation.run()
