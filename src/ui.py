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
