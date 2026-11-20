
"""
UI Framework & Reusable Components
Region-Wise Revenue Contribution Analysis
ABES Engineering College
Mentor: Prof. Kalpana Dwivedi
"""

from pathlib import Path
from html import escape
from typing import List, Dict, Any, Optional

import streamlit as st


def apply_custom_css() -> None:
    """Apply dashboard-wide styling."""

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #F4F6FA;
    }

    .block-container {
        max-width: 1500px;
        padding-top: 1rem;
        padding-bottom: 2rem;
    }

    /* Dark sidebar */
    section[data-testid="stSidebar"] {
        background: #11151F;
        border-right: 1px solid #292F3B;
    }

    section[data-testid="stSidebar"] * {
        color: #F1F5F9;
    }

    section[data-testid="stSidebar"] label {
        color: #E2E8F0 !important;
    }

    section[data-testid="stSidebar"] [data-baseweb="select"] > div {
        background: #F8FAFC;
        color: #111827;
        border-radius: 7px;
    }

    section[data-testid="stSidebar"] [data-baseweb="select"] * {
        color: #111827;
    }

    section[data-testid="stSidebar"] [data-testid="stSlider"] {
        padding-top: 8px;
    }

    /* Dashboard header */
    .dashboard-header {
        background: linear-gradient(115deg, #650D20 0%, #94152F 55%, #700D25 100%);
        color: white;
        border-radius: 0 0 16px 16px;
        padding: 35px 28px 38px;
        margin-bottom: 24px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(70, 10, 25, 0.18);
    }

    .dashboard-header h1 {
        color: white !important;
        font-size: 36px !important;
        font-weight: 800 !important;
        margin: 0 0 8px 0 !important;
        line-height: 1.2 !important;
    }

    .dashboard-header p {
        color: #FCE7EC !important;
        font-size: 18px;
        margin: 0;
    }

    /* KPI cards */
    .kpi-card {
        background: white;
        border: 1px solid #E1E5EC;
        border-radius: 11px;
        padding: 18px 12px;
        min-height: 105px;
        text-align: center;
        box-shadow: 0 3px 8px rgba(15, 23, 42, 0.07);
        margin-bottom: 15px;
    }

    .kpi-title {
        color: #475569;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 8px;
    }

    .kpi-value {
        color: #111827;
        font-size: 27px;
        font-weight: 800;
        line-height: 1.2;
    }

    /* Insight banner */
    .insight-banner {
        background: #FFF5DC;
        border: 1px solid #F5D99A;
        border-radius: 9px;
        padding: 14px 18px;
        color: #654B16;
        font-size: 14px;
        margin: 8px 0 20px 0;
    }

    /* Chart containers */
    div[data-testid="stPlotlyChart"] {
        background: white;
        border: 1px solid #E0E4EA;
        border-radius: 11px;
        padding: 8px;
        box-shadow: 0 3px 8px rgba(15, 23, 42, 0.06);
    }

    h2, h3 {
        color: #172033;
    }

    </style>
    """, unsafe_allow_html=True)


def render_sidebar_branding() -> None:
    """Render ABES branding in the sidebar if the logo exists."""

    logo_path = Path("assets/abes-logo.png")

    if logo_path.exists():
        st.sidebar.image(str(logo_path), width=185)
    else:
        st.sidebar.markdown(
            "<h2 style='color:white; margin-bottom:0;'>ABES</h2>"
            "<p style='color:#CBD5E1; margin-top:0;'>Engineering College</p>",
            unsafe_allow_html=True
        )

    st.sidebar.markdown("---")


def render_tailwind_header(
    title: str,
    subtitle: str,
    badge_text: str = "EXECUTIVE PORTAL",
    height: int = 190
) -> None:
    """Render the maroon dashboard header."""

    safe_title = escape(title)
    safe_subtitle = escape(subtitle)
    safe_badge = escape(badge_text)

    st.markdown(f"""
    <div class="dashboard-header">
        <div style="margin-bottom:15px;">
            <span style="
                background:#263D91;
                color:white;
                padding:6px 15px;
                border-radius:20px;
                font-size:13px;
                font-weight:700;
                letter-spacing:0.5px;">
                {safe_badge}
            </span>
            <span style="color:#DCE7FF; font-size:14px; margin-left:10px;">
                ABES Engineering College &nbsp; • &nbsp; Data Analytics Spec.
            </span>
        </div>
        <h1>{safe_title}</h1>
        <p>{safe_subtitle}</p>
        <div style="
            margin-top:15px;
            font-size:13px;
            color:#FFE5EA;">
            Mentor: Prof. Kalpana Dwivedi
            &nbsp; • &nbsp; Python 3.12 &nbsp; • &nbsp; SQLite &nbsp; • &nbsp; Plotly
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_kpi_grid(
    kpi_list: List[Dict[str, Any]],
    height: int = 145
) -> None:
    """Render four KPI cards in one row."""

    columns = st.columns(4)

    for column, item in zip(columns, kpi_list):
        title = escape(str(item.get("title", "")))
        value = escape(str(item.get("value", "")))

        with column:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">{title}</div>
                <div class="kpi-value">{value}</div>
            </div>
            """, unsafe_allow_html=True)


def render_insight_box(
    title: str,
    text: str,
    box_type: str = "warning",
    height: int = 100
) -> None:
    """Render the yellow executive insight banner."""

    safe_title = escape(title)
    safe_text = escape(text)

    st.markdown(f"""
    <div class="insight-banner">
        <strong>⚠ {safe_title}:</strong>
        {safe_text}
    </div>
    """, unsafe_allow_html=True)


def render_chart_header(
    title: str,
    subtitle: str = "",
    help_text: Optional[str] = None
) -> None:
    """Render a chart heading."""

    col1, col2 = st.columns([0.85, 0.15])

    with col1:
        st.markdown(f"### {title}")

        if subtitle:
            st.caption(subtitle)

    with col2:
        if help_text:
            with st.popover("Info"):
                st.markdown(help_text)
