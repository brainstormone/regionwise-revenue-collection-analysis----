"""
UI-08: Project About, Architecture & Academic Reference Screen
"""

import streamlit as st
from src.ui import apply_custom_css, render_tailwind_header

apply_custom_css()

render_tailwind_header(
    title="Project Architecture, Methodology & Credits",
    subtitle="MCA 2nd Year Capstone Project - ABES Engineering College, Ghaziabad",
    badge_text="Screen UI-08"
)


# 1. Project Metadata Card
st.markdown("### 🎓 Academic Metadata & Institutional Context")
st.markdown("""
- **Project ID:** P056
- **Project Title:** Region-Wise Revenue Contribution Analysis
- **Program:** Master of Computer Applications (MCA) — Second Year
- **Specialization:** Data Analytics
- **Institution:** ABES Engineering College
- **Batch ID:** ABES_OND26_MCA 2nd Year_Data Analytics_Batch 01
- **Project Mentor:** Mr. Dinesh Sereno
- **Data Analytics Mentor:** Mr. Dinesh
- **FSD Java Mentor:** Ms. Charsini
- **FSD Python Mentor:** Mr. Madana
- **Candidate:** Abhishek Kumar Mishra
- **University Roll Number:** 2500320140006
- **Technology Stack:** Python 3.12, SQLite 3, pandas, NumPy, SciPy, Plotly, Streamlit, Tailwind CSS, pytest
""")


# 2. Architecture Data Flow Diagram
st.markdown("### 🏗️ End-to-End System Architecture")
st.markdown("""
```text
  [ Raw Synthetic CSVs ] 
            │
            ▼
  [ src/data/cleaner.py ] ── (Median Freight Imputation & PK Deduplication)
            │
            ▼
  [ SQLite data/app.db ]  ── (4 Dimension Tables + fact_sales + view_sales_analysis)
            │
            ▼
  [ src/data/loader.py ]  ── (@st.cache_data Zero-Flicker Sub-100ms Query Cache)
            │
            ▼
  [ src/analytics/ ]      ── (KPIs, Pareto 80/20, Elasticity OLS, Kruskal-Wallis)
            │
            ▼
  [ Streamlit Multipage ] ── (app.py + 8 Specialized Pages + Tailwind Components)
            │
            ▼
  [ Automated QA Suite ]  ── (pytest: test_data.py, test_analysis.py, test_app.py)
```
""")

# 3. Stakeholder RACI Matrix
st.markdown("### 👥 Stakeholder RACI Matrix")
st.markdown("""
| Stakeholder Role | Initial Problem / Need | Key Decision Made with App | RACI Designation |
| :--- | :--- | :--- | :---: |
| **Chief Commercial Officer (CCO)** | Macro territorial revenue concentration risk | National quota & marketing budget rebalancing | **Accountable (A)** |
| **Regional Sales Director** | Territory actual vs target variance | Sales rep targets, localized inventory buffers | **Responsible (R)** |
| **Product Category Lead** | Product margin leakage & discount dilution | Promotional discount ceilings (<20%) | **Consulted (C)** |
| **Supply Chain & Logistics Lead** | Inter-state freight transit surcharge drain | Regional warehouse & fulfillment optimization | **Consulted (C)** |
| **Lead Data Analyst / BI Developer** | Data reproducibility & schema integrity | Schema validation, automated QA testing | **Informed (I)** |
""")

st.info("📌 All deliverables (BRD, TRD, Database Design, ER Diagrams, Test Cases, Build Plan) are archived under `docs/`.")
