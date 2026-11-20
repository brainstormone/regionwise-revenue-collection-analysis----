
"""
UI Framework & Reusable Components Module
Region-Wise Revenue Contribution Analysis
MCA 2nd Year Capstone Project - ABES Engineering College
Mentor: Prof. Kalpna Dwivedi
"""

import streamlit as st
from typing import List, Dict, Any, Optional


def apply_custom_css() -> None:
    """Apply consistent styling to native Streamlit components."""

    custom_css = """
    <style>
        html, body, [class*="css"] {
            font-family: Arial, sans-serif;
        }

        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 2rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            max-width: 1350px !important;
        }

        section[data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E2E8F0 !important;
        }

        [data-testid="stMetricValue"] {
            font-size: 1.85rem !important;
            font-weight: 700 !important;
            color: #1E3A8A !important;
        }

        div.stButton > button {
            background: linear-gradient(
                135deg, #1E40AF 0%, #2563EB 100%
            ) !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 0.5rem !important;
            padding: 0.5rem 1.25rem !important;
            font-weight: 600 !important;
            font-size: 0.875rem !important;
            transition: all 0.2s ease-in-out !important;
        }

        div.stButton > button:hover {
            transform: translateY(-1px) !important;
        }

        .ui-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 0.75rem;
            padding: 1.25rem;
            margin-bottom: 1.25rem;
        }

        [data-testid="stDataFrame"] {
            border: 1px solid #E2E8F0 !important;
            border-radius: 0.5rem !important;
        }
    </style>
    """

    st.markdown(custom_css, unsafe_allow_html=True)


def render_tailwind_header(
    title: str,
    subtitle: str,
    badge_text: str = "MCA Capstone DA",
    height: int = 135
) -> None:
    """
    Render the dashboard header using native Streamlit components.

    The height parameter is retained for compatibility with existing calls.
    """

    with st.container():
        st.caption(
            f"{badge_text}  |  ABES Engineering College  |  Data Analytics"
        )

        st.markdown(f"## {title}")
        st.caption(subtitle)

        st.caption(
            "Mentor: Prof. Kalpna Dwivedi  |  "
            "Python 3.12  |  SQLite  |  Plotly"
        )


def render_kpi_grid(
    kpi_list: List[Dict[str, Any]],
    height: int = 120
) -> None:
    """
    Render KPI cards using native Streamlit columns and metrics.

    Expected dictionary keys:
    title, value, delta, delta_type, subtitle, accent.
    """

    if not kpi_list:
        return

    # Display a maximum of four KPI cards per row.
    for start in range(0, len(kpi_list), 4):
        row_items = kpi_list[start:start + 4]
        columns = st.columns(len(row_items))

        for col, item in zip(columns, row_items):
            with col:
                with st.container(border=True):
                    title = item.get("title", "")
                    value = item.get("value", "")
                    delta = item.get("delta", "")
                    subtitle = item.get("subtitle", "")

                    st.metric(
                        label=title,
                        value=value,
                        delta=delta if delta else None
                    )

                    if subtitle:
                        st.caption(subtitle)


def render_insight_box(
    title: str,
    text: str,
    box_type: str = "info",
    height: int = 95
) -> None:
    """
    Render insight messages using native Streamlit alert components.
    """

    message = f"**{title}**\n\n{text}"

    alert_functions = {
        "info": st.info,
        "success": st.success,
        "warning": st.warning,
        "danger": st.error
    }

    display_alert = alert_functions.get(box_type, st.info)
    display_alert(message)


def render_chart_header(
    title: str,
    subtitle: str = "",
    help_text: Optional[str] = None
) -> None:
    """Render a standard chart heading with optional help information."""

    col1, col2 = st.columns([0.85, 0.15])

    with col1:
        st.markdown(f"### {title}")

        if subtitle:
            st.caption(subtitle)

    with col2:
        if help_text:
            with st.popover("ℹ️ Info"):
                st.markdown(help_text)
