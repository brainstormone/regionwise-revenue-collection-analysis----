"""
UI Framework & Reusable Components Module
Region-Wise Revenue Contribution Analysis
MCA 2nd Year Capstone Project - ABES Engineering College
Mentor: Prof. Kalpana Dwivedi
"""

import streamlit as st
import streamlit.components.v1 as components
from typing import List, Dict, Any, Optional


def apply_custom_css() -> None:
    """
    Injects custom CSS to ensure consistent Tailwind-aligned styling
    across native Streamlit elements, reducing whitespace and improving typography.
    """
    custom_css = """
    <style>
        /* Modern Font and Background Cleanups */        
        html, body, [class*="css"] {
            font-family: Arial, sans-serif;
        }
        
        /* Main Container Padding Optimization */
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 2rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            max-width: 1350px !important;
        }
        
        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E2E8F0 !important;
        }
        
        /* Streamlit Native Metric Overrides */
        [data-testid="stMetricValue"] {
            font-size: 1.85rem !important;
            font-weight: 700 !important;
            color: #1E3A8A !important;
        }
        
        /* Native Button Modernization */
        div.stButton > button {
            background: linear-gradient(135deg, #1E40AF 0%, #2563EB 100%) !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 0.5rem !important;
            padding: 0.5rem 1.25rem !important;
            font-weight: 600 !important;
            font-size: 0.875rem !important;
            box-shadow: 0 2px 4px rgba(37, 99, 235, 0.2) !important;
            transition: all 0.2s ease-in-out !important;
        }
        
        div.stButton > button:hover {
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 6px rgba(37, 99, 235, 0.3) !important;
        }
        
        /* Card Containers */
        .ui-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 0.75rem;
            padding: 1.25rem;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
            margin-bottom: 1.25rem;
        }
        
        /* Table enhancements */
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
    Renders an enterprise gradient header card using Tailwind CSS inside an iframe.
    
    Args:
        title: Main page or section heading.
        subtitle: Secondary descriptive text.
        badge_text: Pill badge tag text (e.g., 'Step 12: UI Framework').
        height: Height in pixels for the iframe component.
    """
    html_code = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
        <style>body {{ font-family: 'Inter', sans-serif; }}</style>
    </head>
    <body class="bg-transparent m-0 p-0 antialiased">
        <div class="bg-gradient-to-r from-blue-950 via-blue-900 to-indigo-900 text-white rounded-xl p-5 shadow-md border border-blue-800">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3">
                <div class="space-y-1">
                    <div class="flex items-center gap-2">
                        <span class="px-2.5 py-0.5 bg-blue-600/60 border border-blue-400/40 text-blue-100 text-xs font-semibold rounded-full uppercase tracking-wider">
                            {badge_text}
                        </span>
                        <span class="text-xs text-blue-300 font-medium">ABES Engineering College</span>
                        <span class="text-xs text-blue-400">&bull;</span>
                        <span class="text-xs text-blue-300">Data Analytics Spec.</span>
                    </div>
                    <h1 class="text-xl sm:text-2xl font-extrabold text-white tracking-tight leading-tight">
                        {title}
                    </h1>
                    <p class="text-xs sm:text-sm text-blue-100/90 leading-snug">
                        {subtitle}
                    </p>
                </div>
                <div class="hidden sm:flex flex-col items-end text-right bg-blue-950/60 px-3 py-2 rounded-lg border border-blue-700/40 shrink-0">
                    <span class="text-xs font-bold text-white">Mentor: Prof. Kalpna Dwivedi</span>
                    <span class="text-[11px] text-blue-200">Python 3.12 &bull; SQLite &bull; Plotly</span>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    components.html(html_code, height=height)


def render_kpi_grid(
    kpi_list: List[Dict[str, Any]],
    height: int = 120
) -> None:
    """
    Renders a responsive 4-column KPI card grid using Tailwind CSS inside an iframe.
    
    Args:
        kpi_list: List of dictionaries with keys:
            - 'title': Label of KPI (e.g. 'Total Net Revenue')
            - 'value': Formatted string value (e.g. '₹34,82,450')
            - 'delta': Change metric string (e.g. '+12.4% MoM')
            - 'delta_type': 'positive' | 'negative' | 'neutral'
            - 'subtitle': Footnote or comparison target (e.g. 'vs Target: ₹32.00 L')
            - 'accent': 'blue' | 'green' | 'amber' | 'red' (border accent)
        height: Height in pixels for the container iframe.
    """
    cards_html = ""
    for item in kpi_list:
        title = item.get("title", "")
        value = item.get("value", "")
        delta = item.get("delta", "")
        delta_type = item.get("delta_type", "neutral")
        subtitle = item.get("subtitle", "")
        accent = item.get("accent", "blue")
        
        # Color palettes based on delta
        if delta_type == "positive":
            delta_badge = f'<span class="inline-flex items-center text-xs font-semibold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">&#9650; {delta}</span>'
        elif delta_type == "negative":
            delta_badge = f'<span class="inline-flex items-center text-xs font-semibold text-rose-700 bg-rose-50 px-2 py-0.5 rounded-full border border-rose-200">&#9660; {delta}</span>'
        else:
            delta_badge = f'<span class="inline-flex items-center text-xs font-medium text-slate-600 bg-slate-100 px-2 py-0.5 rounded-full border border-slate-200">{delta}</span>' if delta else ""
            
        accent_border = {
            "blue": "border-l-4 border-l-blue-600 border-slate-200",
            "green": "border-l-4 border-l-emerald-600 border-slate-200",
            "amber": "border-l-4 border-l-amber-500 border-slate-200",
            "red": "border-l-4 border-l-rose-600 border-slate-200",
        }.get(accent, "border-slate-200")

        card_html = f"""
        <div class="bg-white rounded-xl p-4 shadow-sm border {accent_border} flex flex-col justify-between hover:shadow-md transition-shadow">
            <div>
                <div class="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1">{title}</div>
                <div class="text-2xl font-bold text-slate-900 tracking-tight leading-none my-1">{value}</div>
            </div>
            <div class="mt-2 flex items-center justify-between text-xs pt-1 border-t border-slate-100">
                {delta_badge}
                <span class="text-slate-400 font-normal truncate ml-1">{subtitle}</span>
            </div>
        </div>
        """
        cards_html += card_html

    grid_cols = min(len(kpi_list), 4)
    cols_class = f"grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-{grid_cols} gap-4"
    
    html_code = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
        <style>body {{ font-family: 'Inter', sans-serif; }}</style>
    </head>
    <body class="bg-transparent m-0 p-0 antialiased">
        <div class="{cols_class}">
            {cards_html}
        </div>
    </body>
    </html>
    """
    components.html(html_code, height=height)


def render_insight_box(
    title: str,
    text: str,
    box_type: str = "info",
    height: int = 95
) -> None:
    """
    Renders a styled Tailwind insight callout banner for executive takeaways.
    
    Args:
        title: Short bold takeaway title.
        text: Detailed narrative explanation.
        box_type: 'info' | 'success' | 'warning' | 'danger'
        height: Height in pixels for the container iframe.
    """
    type_configs = {
        "info": {
            "bg": "bg-blue-50",
            "border": "border-blue-200",
            "border_l": "border-l-blue-600",
            "title_color": "text-blue-900",
            "text_color": "text-blue-800",
            "icon": "&#9432;"
        },
        "success": {
            "bg": "bg-emerald-50",
            "border": "border-emerald-200",
            "border_l": "border-l-emerald-600",
            "title_color": "text-emerald-900",
            "text_color": "text-emerald-800",
            "icon": "&#10003;"
        },
        "warning": {
            "bg": "bg-amber-50",
            "border": "border-amber-200",
            "border_l": "border-l-amber-600",
            "title_color": "text-amber-900",
            "text_color": "text-amber-800",
            "icon": "&#9888;"
        },
        "danger": {
            "bg": "bg-rose-50",
            "border": "border-rose-200",
            "border_l": "border-l-rose-600",
            "title_color": "text-rose-900",
            "text_color": "text-rose-800",
            "icon": "&#9888;"
        }
    }
    cfg = type_configs.get(box_type, type_configs["info"])
    
    html_code = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style>body {{ font-family: 'Inter', sans-serif; }}</style>
    </head>
    <body class="bg-transparent m-0 p-0 antialiased">
        <div class="{cfg['bg']} border {cfg['border']} border-l-4 {cfg['border_l']} rounded-lg p-3.5 shadow-sm">
            <div class="flex items-start gap-2.5">
                <span class="text-base font-bold {cfg['title_color']} leading-none mt-0.5">{cfg['icon']}</span>
                <div class="space-y-0.5">
                    <span class="text-xs font-bold uppercase tracking-wider {cfg['title_color']}">{title}:</span>
                    <span class="text-xs {cfg['text_color']} font-medium leading-relaxed">{text}</span>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    components.html(html_code, height=height)


def render_chart_header(
    title: str,
    subtitle: str = "",
    help_text: Optional[str] = None
) -> None:
    """
    Renders a standard clean chart header container in pure Streamlit.
    """
    col1, col2 = st.columns([0.85, 0.15])
    with col1:
        st.markdown(f"### {title}")
        if subtitle:
            st.caption(subtitle)
    with col2:
        if help_text:
            with st.popover("ℹ️ Info"):
                st.markdown(help_text)
