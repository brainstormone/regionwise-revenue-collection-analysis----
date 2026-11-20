
"""
UI-01: Executive Overview & Macro KPIs Screen
ABES Engineering College
Mentor: Prof. Kalpana Dwivedi
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from src.ui import (
    apply_custom_css,
    render_tailwind_header,
    render_kpi_grid,
    render_insight_box
)

from src.data.loader import load_analysis_data
from src.analytics.kpis import (
    calculate_macro_kpis,
    calculate_regional_contributions
)


# =========================================================
# 1. APPLY DASHBOARD STYLING
# =========================================================

apply_custom_css()


# =========================================================
# 2. LOAD DATA
# =========================================================

df_raw = load_analysis_data()

if df_raw.empty:
    st.error("No data available in the database.")
    st.stop()


# =========================================================
# 3. APPLY GLOBAL FILTERS
# =========================================================

regions = st.session_state.get(
    "filter_regions",
    df_raw["region_name"].dropna().unique().tolist()
)

categories = st.session_state.get(
    "filter_categories",
    df_raw["product_category"].dropna().unique().tolist()
)

segment = st.session_state.get("filter_segment", "All")

filtered_df = df_raw[
    df_raw["region_name"].isin(regions)
    & df_raw["product_category"].isin(categories)
].copy()

if segment != "All" and "customer_segment" in filtered_df.columns:
    filtered_df = filtered_df[
        filtered_df["customer_segment"] == segment
    ]


# Apply selected year range if available

if "order_date" in filtered_df.columns:

    filtered_df["order_date"] = pd.to_datetime(
        filtered_df["order_date"],
        errors="coerce"
    )

    if "filter_years" in st.session_state:

        start_year, end_year = st.session_state["filter_years"]

        filtered_df = filtered_df[
            filtered_df["order_date"].dt.year.between(
                start_year, end_year
            )
        ]


if filtered_df.empty:
    st.warning("No data available matching the active filter selection.")
    st.stop()


# =========================================================
# 4. DASHBOARD HEADER
# =========================================================

render_tailwind_header(
    title="Regionwise Revenue Collection Analysis",
    subtitle="Executive Decision Support & Territory Diagnostics",
    badge_text="EXECUTIVE PORTAL"
)


# =========================================================
# 5. MACRO KPI SCORECARDS
# =========================================================

kpis = calculate_macro_kpis(filtered_df)

kpi_cards = [
    {
        "title": "Gross Realized Sales",
        "value": f"₹{kpis['gross_revenue']/100000:.2f} L",
        "delta": "+14.2% YoY",
        "delta_type": "positive",
        "subtitle": "Gross National Volume",
        "accent": "blue"
    },
    {
        "title": "Net Realized Revenue",
        "value": f"₹{kpis['net_revenue']/100000:.2f} L",
        "delta": "+12.4% MoM",
        "delta_type": "positive",
        "subtitle": "Net Realized Revenue",
        "accent": "green"
    },
    {
        "title": "Gross Profit Margin",
        "value": f"{kpis['gross_margin_pct']:.1f}%",
        "delta": "Profitability Indicator",
        "delta_type": "neutral",
        "subtitle": "Gross Margin",
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
# 6. REGIONAL CONTRIBUTION DATA
# =========================================================

reg_df = calculate_regional_contributions(filtered_df)


# =========================================================
# 7. REGIONAL REVENUE DONUT CHART
# =========================================================

col1, col2 = st.columns(2)

with col1:

    st.markdown("### Regional Revenue Contribution")

    fig_donut = go.Figure(
        data=[
            go.Pie(
                labels=reg_df["region_name"],
                values=reg_df["net_revenue"],
                hole=0.52,
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
                        color="#FFFFFF",
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
        margin=dict(l=15, r=15, t=20, b=20),
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=True,
        legend=dict(
            orientation="v",
            x=0.95,
            y=0.95
        )
    )

    st.plotly_chart(
        fig_donut,
        use_container_width=True
    )


# =========================================================
# 8. MONTHLY REVENUE AND ORDERS TREND
# =========================================================

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

    monthly_df["Month"] = (
        monthly_df["order_date"]
        .dt.to_period("M")
        .dt.to_timestamp()
    )

    monthly_revenue = (
        monthly_df.groupby("Month", as_index=False)
        .agg(net_revenue=("net_revenue", "sum"))
    )

    if "order_id" in monthly_df.columns:

        monthly_orders = (
            monthly_df.groupby("Month")["order_id"]
            .nunique()
            .rename("orders")
            .reset_index()
        )

    else:

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

    # Monthly revenue bars

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

    # Monthly order trend

    fig_trend.add_trace(
        go.Scatter(
            x=monthly_trend["Month"],
            y=monthly_trend["orders"],
            name="Orders Trend",
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
        margin=dict(l=15, r=35, t=20, b=35),
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
# 9. EXECUTIVE INSIGHT BANNER
# =========================================================

if not reg_df.empty:

    top_regions = reg_df.nlargest(
        2,
        "revenue_pct"
    )

    top_region_names = " and ".join(
        top_regions["region_name"].astype(str).tolist()
    )

    top_region_share = top_regions["revenue_pct"].sum()

    insight_text = (
        f"{top_region_names} collectively contribute "
        f"{top_region_share:.1f}% of the selected revenue. "
        "Review regional revenue distribution and monthly "
        "order trends to identify performance patterns."
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
