
"""
UI Framework & Reusable Components
Region-Wise Revenue Contribution Analysis
MCA 2nd Year Capstone Project - ABES Engineering College
Mentor: Prof. Kalpana Dwivedi
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
        --navy: #11151F;
        --navy-light: #252B3A;
        --maroon: #94152F;
        --maroon-dark: #650D20;
        --background: #F4F6FA;
        --card: #FFFFFF;
        --text: #172033;
        --muted: #718096;
        --border: #E1E5EC;
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
        transition: all 0.2s ease-in-out !important;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover {
        background: #303644 !important;
        border-left: 3px solid #E64A62 !important;
        transform: translateX(3px);
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a[aria-current="page"] {
        background: #303644 !important;
        border-left: 3px solid #E64A62 !important;
        font-weight: 700 !important;
    }

    /* Sidebar filters */

    section[data-testid="stSidebar"] label {
        color: #E5E7EB !important;
        font-size: 13px !important;
    }

    section[data-testid="stSidebar"] [data-baseweb="select"] > div {
        background: #F8FAFC !important;
        border-radius: 7px !important;
    }

    section[data-testid="stSidebar"] [data-baseweb="select"] * {
        color: #111827 !important;
    }

    section[data-testid="stSidebar"] [data-testid="stSlider"] p {
        color: #E5E7EB !important;
    }

    /* Sidebar buttons */

    section[data-testid="stSidebar"] .stButton button {
        background: #303644 !important;
        color: white !important;
        border: 1px solid #485064 !important;
        border-radius: 7px !important;
        transition: all 0.2s ease !important;
    }

    section[data-testid="stSidebar"] .stButton button:hover {
        background: var(--maroon) !important;
        border-color: #E64A62 !important;
        transform: translateY(-1px);
    }

    /* =====================================================
       DASHBOARD HEADER
       ===================================================== */

    .dashboard-header {
        position: relative;
        overflow: hidden;
        background: linear-gradient(
            115deg,
            #650D20 0%,
            #94152F 55%,
            #741027 100%
        );
        border-radius: 0 0 16px 16px;
        padding: 30px 25px;
        margin-bottom: 24px;
        min-height: 175px;
        text-align: center;
        box-shadow: 0 6px 18px rgba(101, 13, 32, 0.18);
    }

    .dashboard-header::after {
        content: "";
        position: absolute;
        top: -90px;
        right: -50px;
        width: 380px;
        height: 180px;
        background: rgba(255,255,255,0.07);
        border-radius: 50%;
        transform: rotate(-12deg);
        pointer-events: none;
    }

    .header-content {
        position: relative;
        z-index: 2;
    }

    .header-badge {
        display: inline-block;
        background: #263D91;
        color: #FFFFFF;
        border: 1px solid rgba(255,255,255,0.25);
        border-radius: 20px;
        padding: 6px 15px;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.7px;
        margin-bottom: 13px;
    }

    .header-title {
        color: #FFFFFF !important;
        font-size: clamp(25px, 3vw, 38px) !important;
        line-height: 1.2 !important;
        font-weight: 800 !important;
        margin: 0 0 9px 0 !important;
    }

    .header-subtitle {
        color: #FCE7EC !important;
        font-size: 17px !important;
        margin: 0 !important;
    }

    .header-mentor {
        color: #FFE5EA !important;
        font-size: 13px !important;
        font-weight: 600;
        margin-top: 13px !important;
    }

    /* =====================================================
       KPI CARDS
       ===================================================== */

    .kpi-card {
        background: #FFFFFF;
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 17px 15px;
        min-height: 112px;
        box-shadow: 0 3px 8px rgba(15,23,42,0.06);
        transition: all 0.22s ease-in-out;
        margin-bottom: 16px;
        box-sizing: border-box;
    }

    .kpi-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 9px 20px rgba(15,23,42,0.12);
        border-color: #C5CCD8;
    }

    .kpi-title {
        color: #64748B;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.7px;
        text-transform: uppercase;
        margin-bottom: 9px;
    }

    .kpi-value {
        color: #111827;
        font-size: clamp(20px, 2vw, 28px);
        font-weight: 800;
        line-height: 1.2;
    }

    .kpi-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 5px;
        border-top: 1px solid #EEF1F5;
        margin-top: 12px;
        padding-top: 9px;
        font-size: 11px;
    }

    .kpi-subtitle {
        color: #94A3B8;
        text-align: right;
    }

    .kpi-positive {
        color: #047857;
        background: #ECFDF5;
        border: 1px solid #A7F3D0;
        padding: 3px 8px;
        border-radius: 20px;
        white-space: nowrap;
    }

    .kpi-negative {
        color: #BE123C;
        background: #FFF1F2;
        border: 1px solid #FECDD3;
        padding: 3px 8px;
        border-radius: 20px;
        white-space: nowrap;
    }

    .kpi-neutral {
        color: #475569;
        background: #F1F5F9;
        border: 1px solid #E2E8F0;
        padding: 3px 8px;
        border-radius: 20px;
        white-space: nowrap;
    }

    /* =====================================================
       INSIGHT BANNER
       ===================================================== */

    .insight-banner {
        background: #FFF5DC;
        border: 1px solid #F5D99A;
        border-left: 5px solid #E6A12A;
        border-radius: 9px;
        padding: 14px 17px;
        margin: 12px 0 24px;
        color: #654B16;
        font-size: 14px;
        line-height: 1.8;
        transition: box-shadow 0.2s ease;
    }

    .insight-banner:hover {
        box-shadow: 0 5px 12px rgba(180,120,20,0.12);
    }

    .insight-title {
        font-weight: 800;
        color: #7C4A03;
        margin-right: 5px;
    }

    /* =====================================================
       CHARTS AND TABLES
       ===================================================== */

    .chart-heading {
        color: #172033;
        font-size: 22px;
        font-weight: 650;
        margin: 12px 0;
    }

    div[data-testid="stPlotlyChart"] {
        background: #FFFFFF;
        border: 1px solid #E0E4EA;
        border-radius: 11px;
        padding: 8px;
        box-shadow: 0 3px 8px rgba(15,23,42,0.05);
        transition: all 0.2s ease;
    }

    div[data-testid="stPlotlyChart"]:hover {
        box-shadow: 0 7px 16px rgba(15,23,42,0.09);
        border-color: #C8CED8;
    }

    [data-testid="stDataFrame"] {
        border: 1px solid #E0E4EA !important;
        border-radius: 9px !important;
        overflow: hidden;
    }

    /* General buttons */

    div.stButton > button {
        border-radius: 7px !important;
        transition: all 0.2s ease-in-out !important;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 12px rgba(15,23,42,0.12);
    }

    /* Responsive layout */

    @media (max-width: 900px) {
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }

        .dashboard-header {
            padding: 24px 16px;
        }

        .header-subtitle {
            font-size: 14px !important;
        }
    }

    </style>
    """, unsafe_allow_html=True)


# =========================================================
# 2. SIDEBAR BRANDING
# =========================================================

def render_sidebar_branding() -> None:
    """
    Display the ABES logo in the sidebar.

    The logo must be stored at:
    assets/abes-logo.png
    """

    logo_path = (
        Path(__file__).resolve().parent.parent
        / "assets"
        / "abes-logo.png"
    )

    if logo_path.is_file() and logo_path.stat().st_size > 100:
        st.sidebar.image(
            str(logo_path),
            width=185
        )
    else:
        st.sidebar.markdown("""
        <div style="padding:12px 5px;">
            <div style="font-size:27px;font-weight:800;color:white;">
                ABES
            </div>
            <div style="font-size:12px;color:#CBD5E1;">
                Engineering College
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.sidebar.markdown("---")


# =========================================================
# 3. DASHBOARD HEADER
# =========================================================

def render_tailwind_header(
    title: str,
    subtitle: str,
    badge_text: str = "EXECUTIVE PORTAL",
    height: int = 190
) -> None:
    """
    Render the maroon executive dashboard header.
    Function name retained for compatibility with existing pages.
    """

    safe_title = escape(str(title))
    safe_subtitle = escape(str(subtitle))
    safe_badge = escape(str(badge_text))

    st.markdown(f"""
    <div class="dashboard-header">
        <div class="header-content">

            <div class="header-badge">
                {safe_badge}
            </div>

            <h1 class="header-title">
                {safe_title}
            </h1>

            <p class="header-subtitle">
                {safe_subtitle}
            </p>

            <p class="header-mentor">
                Mentor: Prof. Kalpana Dwivedi
                &nbsp; • &nbsp;
                Python 3.12 • SQLite • Plotly
            </p>

        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# 4. KPI GRID
# =========================================================

def render_kpi_grid(
    kpi_list: List[Dict[str, Any]],
    height: int = 120
) -> None:
    """
    Render responsive KPI cards using native Streamlit columns.
    """

    if not kpi_list:
        return

    columns = st.columns(len(kpi_list), gap="medium")

    for column, item in zip(columns, kpi_list):

        title = escape(str(item.get("title", "")))
        value = escape(str(item.get("value", "")))
        delta = escape(str(item.get("delta", "")))
        subtitle = escape(str(item.get("subtitle", "")))

        delta_type = item.get("delta_type", "neutral")

        if delta_type == "positive":
            badge_class = "kpi-positive"
            prefix = "▲ "
        elif delta_type == "negative":
            badge_class = "kpi-negative"
            prefix = "▼ "
        else:
            badge_class = "kpi-neutral"
            prefix = ""

        with column:

            st.markdown(f"""
            <div class="kpi-card">

                <div class="kpi-title">
                    {title}
                </div>

                <div class="kpi-value">
                    {value}
                </div>

                <div class="kpi-footer">

                    <span class="{badge_class}">
                        {prefix}{delta}
                    </span>

                    <span class="kpi-subtitle">
                        {subtitle}
                    </span>

                </div>

            </div>
            """, unsafe_allow_html=True)


# =========================================================
# 5. EXECUTIVE INSIGHT BANNER
# =========================================================

def render_insight_box(
    title: str,
    text: str,
    box_type: str = "info",
    height: int = 95
) -> None:
    """
    Render an executive insight banner.

    Supports: info, success, warning and danger.
    """

    safe_title = escape(str(title))
    safe_text = escape(str(text))

    configurations = {
        "info": ("#EFF6FF", "#2563EB", "#1E40AF", "ⓘ"),
        "success": ("#ECFDF5", "#059669", "#065F46", "✓"),
        "warning": ("#FFF5DC", "#E6A12A", "#7C4A03", "⚠"),
        "danger": ("#FFF1F2", "#E11D48", "#9F1239", "⚠"),
    }

    background, border, heading, icon = configurations.get(
        box_type,
        configurations["info"]
    )

    st.markdown(f"""
    <div style="
        background:{background};
        border:1px solid {border}33;
        border-left:5px solid {border};
        border-radius:9px;
        padding:14px 17px;
        margin:12px 0 24px;
        color:{heading};
        font-size:14px;
        line-height:1.8;
    ">

        <span style="font-weight:800;">
            {icon} {safe_title}:
        </span>

        {safe_text}

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# 6. CHART HEADER
# =========================================================

def render_chart_header(
    title: str,
    subtitle: str = "",
    help_text: Optional[str] = None
) -> None:
    """
    Render a reusable chart heading and optional information popover.
    """

    st.markdown(
        f'<div class="chart-heading">{escape(str(title))}</div>',
        unsafe_allow_html=True
    )

    if subtitle:
        st.caption(subtitle)

    if help_text:
        with st.popover("ⓘ Chart Information"):
            st.markdown(help_text)
