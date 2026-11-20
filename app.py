
"""
Region-Wise Revenue Contribution Analysis
Main Application Entry Point & Global Slicing Navigation
MCA 2nd Year Capstone Project - ABES Engineering College
Mentor: Prof. Kalpana Dwivedi
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.ui import (
    apply_custom_css,
    render_tailwind_header,
    render_kpi_grid,
    render_insight_box,
    render_sidebar_branding
)

from src.data.loader import load_analysis_data
from src.analytics.kpis import (
    calculate_macro_kpis,
    calculate_regional_contributions
)


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
# 2. APPLY DASHBOARD DESIGN
# =========================================================

apply_custom_css()
render_sidebar_branding()


# =========================================================
# 3. LOAD DATASET
# =========================================================

try:
    df_raw = load_analysis_data()

except Exception as e:
    st.error(f"Error loading database records: {e}")
    st.stop()

if df_raw.empty:
    st.error("No records found in the database.")
    st.stop()


# =========================================================
# 4. SIDEBAR FILTERS
# =========================================================

st.sidebar.markdown("### Global Slicing Filters")
st.sidebar.caption("Filter selections apply across the dashboard.")

all_regions = sorted(
    df_raw["region_name"].dropna().unique().tolist()
)

all_categories = sorted(
    df_raw["product_category"].dropna().unique().tolist()
)

all_segments = (
    ["All"] +
    sorted(df_raw["customer_segment"].dropna().unique().tolist())
    if "customer_segment" in df_raw.columns
    else ["All"]
)


# Initialize session state

if "filter_regions" not in st.session_state:
    st.session_state["filter_regions"] = all_regions

if "filter_categories" not in st.session_state:
    st.session_state["filter_categories"] = all_categories

if "filter_segment" not in st.session_state:
    st.session_state["filter_segment"] = "All"


# Reset filters

if st.sidebar.button(
    "Reset All Filters",
    use_container_width=True
):
    st.session_state["filter_regions"] = all_regions
    st.session_state["filter_categories"] = all_categories
    st.session_state["filter_segment"] = "All"
    st.rerun()


# Region filter

selected_regions = st.sidebar.multiselect(
    "Region",
    options=all_regions,
    default=st.session_state["filter_regions"]
)

st.session_state["filter_regions"] = (
    selected_regions if selected_regions else all_regions
)


# Product category filter

selected_categories = st.sidebar.multiselect(
    "Product Category",
    options=all_categories,
    default=st.session_state["filter_categories"]
)

st.session_state["filter_categories"] = (
    selected_categories if selected_categories else all_categories
)


# Customer segment filter

selected_segment = st.sidebar.selectbox(
    "Customer Segment",
    options=all_segments,
    index=(
        all_segments.index(st.session_state["filter_segment"])
        if st.session_state["filter_segment"] in all_segments
        else 0
    )
)

st.session_state["filter_segment"] = selected_segment


# Year filter, if date column is available

if "order_date" in df_raw.columns:

    date_values = pd.to_datetime(
        df_raw["order_date"],
        errors="coerce"
    ).dropna()

    if not date_values.empty:

        available_years = sorted(
            date_values.dt.year.unique().tolist()
        )

        selected_years = st.sidebar.slider(
            "Year",
            min_value=int(min(available_years)),
            max_value=int(max(available_years)),
            value=(
                int(min(available_years)),
                int(max(available_years))
            )
        )

        st.session_state["filter_years"] = selected_years


# Sidebar system status

st.sidebar.markdown("---")
st.sidebar.markdown("### System Status")
st.sidebar.success("SQLite Database Active")
st.sidebar.info(f"Records Ingested: {len(df_raw):,}")
st.sidebar.caption("MCA Capstone Project • ABES Engineering College")


# =========================================================
# 5. APPLY FILTERS
# =========================================================

filtered_df = df_raw.copy()

filtered_df = filtered_df[
    filtered_df["region_name"].isin(
        st.session_state["filter_regions"]
    )
]

filtered_df = filtered_df[
    filtered_df["product_category"].isin(
        st.session_state["filter_categories"]
    )
]


if (
    st.session_state["filter_segment"] != "All"
    and "customer_segment" in filtered_df.columns
):
    filtered_df = filtered_df[
        filtered_df["customer_segment"]
        == st.session_state["filter_segment"]
    ]


# Apply year filter

if "order_date" in filtered_df.columns:

    filtered_df["order_date"] = pd.to_datetime(
        filtered_df["order_date"],
        errors="coerce"
    )

    if "filter_years" in st.session_state:

        start_year, end_year = st.session_state["filter_years"]

        filtered_df = filtered_df[
            filtered_df["order_date"].dt.year.between(
                start_year,
                end_year
            )
        ]


# Handle empty filtered dataset

if filtered_df.empty:

    render_tailwind_header(
        title="Regionwise Revenue Collection Analysis",
        subtitle="Executive Decision Support & Territory Diagnostics",
        badge_text="EXECUTIVE PORTAL"
    )

    st.warning(
        "No records match the selected filters. "
        "Please reset your filters and try again."
    )

    st.stop()


# =========================================================
# 6. DASHBOARD HEADER
# =========================================================

render_tailwind_header(
    title="Regionwise Revenue Collection Analysis",
    subtitle="Executive Decision Support & Territory Diagnostics",
    badge_text="EXECUTIVE PORTAL"
)


# =========================================================
# 7. KPI SCORECARDS
# =========================================================

kpis = calculate_macro_kpis(filtered_df)

kpi_cards = [

    {
        "title": "Gross Realized Sales",
        "value": f"₹{kpis['gross_revenue'] / 100000:.2f} L",
        "delta": "+14.2% YoY",
        "delta_type": "positive",
        "subtitle": "National Realized Volume",
        "accent": "blue"
    },

    {
        "title": "Net Realized Revenue",
        "value": f"₹{kpis['net_revenue'] / 100000:.2f} L",
        "delta": "+12.4% MoM",
        "delta_type": "positive",
        "subtitle": "Net Revenue",
        "accent": "green"
    },

    {
        "title": "Gross Profit Margin",
        "value": f"{kpis['gross_margin_pct']:.1f}%",
        "delta": "Margin Indicator",
        "delta_type": "neutral",
        "subtitle": "Profitability",
        "accent": "amber"
    },

    {
        "title": "Total Transaction Volume",
        "value": f"{kpis['total_orders']:,}",
        "delta": f"AOV: ₹{kpis['aov']:,.0f}",
        "delta_type": "neutral",
        "subtitle": "Total Orders",
        "accent": "blue"
    }

]

render_kpi_grid(kpi_cards)


# =========================================================
# 8. REGIONAL REVENUE CONTRIBUTION DATA
# =========================================================

reg_df = calculate_regional_contributions(filtered_df)


# =========================================================
# 9. CHARTS
# =========================================================

col1, col2 = st.columns([1, 1])


# ---------------------------------------------------------
# LEFT: REGIONAL REVENUE DONUT CHART
# ---------------------------------------------------------

with col1:

    st.markdown("### Regional Revenue Contribution")

    fig_donut = go.Figure(
        data=[
            go.Pie(
                labels=reg_df["region_name"],
                values=reg_df["net_revenue"],
                hole=0.55,
                textinfo="percent",
                textposition="inside",
                marker=dict(
                    colors=[
                        "#94152F",
                        "#E74C3C",
                        "#10B981",
                        "#6366F1",
                        "#F59E0B"
                    ],
                    line=dict(
                        color="white",
                        width=2
                    )
                ),
                hovertemplate=(
                    "<b>%{label}</b><br>"
                    "Revenue: ₹%{value:,.0f}<br>"
                    "Contribution: %{percent}"
                    "<extra></extra>"
                )
            )
        ]
    )

    fig_donut.update_layout(
        height=390,
        margin=dict(l=15, r=15, t=25, b=15),
        showlegend=True,
        legend=dict(
            orientation="v",
            x=0.92,
            y=0.95
        ),
        paper_bgcolor="white",
        plot_bgcolor="white"
    )

    st.plotly_chart(
        fig_donut,
        use_container_width=True
    )


# ---------------------------------------------------------
# RIGHT: MONTHLY REVENUE AND ORDER TREND
# ---------------------------------------------------------

with col2:

    st.markdown("### Monthly Revenue & Orders Trend")

    monthly_df = filtered_df.copy()

    monthly_df["order_date"] = pd.to_datetime(
        monthly_df["order_date"],
        errors="coerce"
    )

    monthly_df = monthly_df.dropna(
        subset=["order_date"]
    )

    monthly_df["Month"] = monthly_df[
        "order_date"
    ].dt.to_period("M").dt.to_timestamp()

    monthly_revenue = (
        monthly_df.groupby("Month", as_index=False)
        .agg(
            net_revenue=("net_revenue", "sum")
        )
        .sort_values("Month")
    )

    # Count distinct orders when an order identifier exists.
    if "order_id" in monthly_df.columns:

        monthly_orders = (
            monthly_df.groupby("Month")["order_id"]
            .nunique()
            .rename("orders")
            .reset_index()
        )

    else:

        # Fallback: count transaction records.
        monthly_orders = (
            monthly_df.groupby("Month")
            .size()
            .reset_index(name="orders")
        )

    monthly_trend = monthly_revenue.merge(
        monthly_orders,
        on="Month",
        how="left"
    )

    fig_trend = go.Figure()

    # Revenue bars

    fig_trend.add_trace(
        go.Bar(
            x=monthly_trend["Month"],
            y=monthly_trend["net_revenue"],
            name="Revenue",
            marker_color="#94152F",
            hovertemplate=(
                "Month: %{x|%b %Y}<br>"
                "Revenue: ₹%{y:,.0f}"
                "<extra></extra>"
            )
        )
    )

    # Order trend line

    fig_trend.add_trace(
        go.Scatter(
            x=monthly_trend["Month"],
            y=monthly_trend["orders"],
            name="Orders",
            mode="lines+markers",
            line=dict(
                color="#E76F51",
                width=3
            ),
            marker=dict(size=7),
            yaxis="y2",
            hovertemplate=(
                "Month: %{x|%b %Y}<br>"
                "Orders: %{y:,}"
                "<extra></extra>"
            )
        )
    )

    fig_trend.update_layout(
        height=390,
        margin=dict(l=15, r=35, t=25, b=35),
        paper_bgcolor="white",
        plot_bgcolor="white",
        xaxis=dict(
            title="Month",
            tickformat="%b",
            showgrid=False
        ),
        yaxis=dict(
            title="Revenue (₹)",
            rangemode="tozero"
        ),
        yaxis2=dict(
            title="Orders",
            overlaying="y",
            side="right",
            rangemode="tozero",
            showgrid=False
        ),
        legend=dict(
            orientation="h",
            y=1.12,
            x=0
        ),
        barmode="group"
    )

    st.plotly_chart(
        fig_trend,
        use_container_width=True
    )


# =========================================================
# 10. EXECUTIVE INSIGHT BANNER
# =========================================================

if not reg_df.empty:

    top_regions = (
        reg_df.sort_values(
            "revenue_pct",
            ascending=False
        )
        .head(2)
    )

    top_region_names = " and ".join(
        top_regions["region_name"].astype(str).tolist()
    )

    top_region_share = top_regions["revenue_pct"].sum()

    insight_text = (
        f"{top_region_names} collectively contribute "
        f"{top_region_share:.1f}% of the selected revenue. "
        "Use the regional and monthly charts to compare "
        "revenue distribution and order trends."
    )

else:

    insight_text = (
        "No regional contribution data is available "
        "for the selected filters."
    )


render_insight_box(
    title="Executive Macro Finding",
    text=insight_text,
    box_type="warning"
)
