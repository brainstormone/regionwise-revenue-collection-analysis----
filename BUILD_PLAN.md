
# BUILD PLAN: Region-Wise Revenue Contribution Analysis

**Project Title:** Region-Wise Revenue Contribution Analysis  
**Project ID:** P056  
**Academic Context:** MCA – Second Year (Data Analytics), ABES Engineering College  
**Institution:** ABES Engineering College  
**Batch ID:** ABES_OND26_MCA 2nd Year_Data Analytics_Batch 01  
**Project Mentor:** Mr. Dinesh Sereno  
**Data Analytics Mentor:** Mr. Dinesh  
**FSD Java Mentor:** Ms. Charsini  
**FSD Python Mentor:** Mr. Madana  
**Author / Candidate:** Abhishek Kumar Mishra  
**University Roll Number:** 2500320140006  
**Version:** 1.0 (Production Master Plan)  
**Date:** November 2026  

---


## 1. Project Executive Summary (10 Lines)

1. **Context:** Commercial sales analytics system evaluating geographic revenue skew and profitability leakage across 5 national sales zones.
2. **Business Problem:** Over-reliance on North and West territories (generating ~62% of revenue) hides operational margin decay in East and Central.
3. **Core Dilemma:** High gross top-line sales mask localized inter-state freight surcharges (2.5x higher) and steep discounting (>20%) eroding net margins below 15%.
4. **Data Scale:** Production SQLite database (`data/app.db`) tracking 4 dimension tables and 250+ atomic line-item sales transactions.
5. **Architectural Stack:** Python 3.12, SQLite 3, pandas, NumPy, SciPy (ANOVA / Kruskal-Wallis), Plotly Express/Graph Objects, and Streamlit.
6. **UI/UX Framework:** Streamlit multipage application styled with enterprise Tailwind CSS gradient headers and KPI scorecards via isolated iframes.
7. **Empirical Rigor:** Inferential hypothesis testing rejecting null equal-margin assumptions ($p < 0.001$), coupled with Tukey 1.5×IQR outlier detection.
8. **Automated QA:** Rigorous dual-tier testing matrix featuring 14 functional test cases (`TC-F`) and 16 automated pytest unit/integration tests (`TC-T`).
9. **Traceability:** Complete 100% bidirectional traceability linking 10 OQs, 10 HMWs, 12 BRs, 12 FRs, 14 USs, 8 UIs, and 30 Test Cases in `04_Traceability_Matrix.xlsx`.
10. **Target Delivery:** Production deployment on Streamlit Community Cloud accompanied by ABES academic project report and master defense slides.

### Project Artifacts & Documentation Map
- Step 01: [01_Project_Understanding.docx](file:///C:/Users/garim/.gemini/antigravity/scratch/mca_da_project/docs/01_Project_Understanding.docx) — Problem statement, personas, 10 OQs, SMART objectives.
- Step 02: [02_HMW_Statements.docx](file:///C:/Users/garim/.gemini/antigravity/scratch/mca_da_project/docs/02_HMW_Statements.docx) — 10 HMW design-thinking prompts, top 5 priority drivers.
- Step 03: [03_Needs_Analysis.docx](file:///C:/Users/garim/.gemini/antigravity/scratch/mca_da_project/docs/03_Needs_Analysis.docx) — 12 Business requirements (BR-01..12), MoSCoW prioritization.
- Step 04: [04_Traceability_Matrix.xlsx](file:///C:/Users/garim/.gemini/antigravity/scratch/mca_da_project/docs/04_Traceability_Matrix.xlsx) — Requirements Traceability Matrix (Baselined & Verified).
- Step 05: [05_BRD.docx](file:///C:/Users/garim/.gemini/antigravity/scratch/mca_da_project/docs/05_BRD.docx) — Formal Business Requirements Document v1.0.
- Step 07: [07_TRD.docx](file:///C:/Users/garim/.gemini/antigravity/scratch/mca_da_project/docs/07_TRD.docx) — Technical Requirements Document, Mermaid architecture, pinned requirements.
- Step 08: [08_Database_Design.xlsx](file:///C:/Users/garim/.gemini/antigravity/scratch/mca_da_project/docs/08_Database_Design.xlsx) — Relational schema, 5 data dictionaries, SQLite DDL.
- Step 09: [09_ER_Diagram.docx](file:///C:/Users/garim/.gemini/antigravity/scratch/mca_da_project/docs/09_ER_Diagram.docx) — Formal ER diagram report & high-res PNG [09_ER_Diagram.png](file:///C:/Users/garim/.gemini/antigravity/scratch/mca_da_project/docs/09_ER_Diagram.png).
- Step 10: [10_Data_Validation_Report.docx](file:///C:/Users/garim/.gemini/antigravity/scratch/mca_da_project/docs/10_Data_Validation_Report.docx) — Synthetic dataset validation, seed 42, 5 embedded patterns.
- Step 11: [11_User_Stories.docx](file:///C:/Users/garim/.gemini/antigravity/scratch/mca_da_project/docs/11_User_Stories.docx) — 14 BDD User Stories (Given/When/Then), 5 Epics, 10-day Sprint Plan.
- Step 12: [12_UI_Framework.docx](file:///C:/Users/garim/.gemini/antigravity/scratch/mca_da_project/docs/12_UI_Framework.docx) — UI wireframes, Tailwind component specs, chart selections.
- Step 13: [13_Test_Cases.docx](file:///C:/Users/garim/.gemini/antigravity/scratch/mca_da_project/docs/13_Test_Cases.docx) — Master QA Test Plan (14 Functional TC-F + 16 Technical TC-T).
- Data Sources: [region_wise_revenue_data.xlsx](file:///C:/Users/garim/.gemini/antigravity/scratch/mca_da_project/data/region_wise_revenue_data.xlsx) & SQLite DB [app.db](file:///C:/Users/garim/.gemini/antigravity/scratch/mca_da_project/data/app.db).

---

## 2. Final Project Folder Structure

```text
mca_da_project/
├── .streamlit/
│   └── config.toml                  # Pinned theme, primaryColor #2563EB, background #F8FAFC
├── data/
│   ├── app.db                       # SQLite database (dim_regions, dim_products, dim_customers, fact_sales, view_sales_analysis)
│   ├── region_wise_revenue_data.xlsx # 5-sheet consolidated raw & staging data workbook
│   ├── dim_regions.csv              # Staging CSV: 25 municipal territories
│   ├── dim_products.csv             # Staging CSV: 30 SKUs across 5 categories
│   ├── dim_customers.csv            # Staging CSV: 100 customer profiles
│   ├── fact_sales.csv               # Staging CSV: 253 transactional records
│   └── view_sales_analysis.csv      # Materialized semantic reporting layer (36 cols)
├── docs/                            # Formal academic Word & Excel deliverables (Steps 01-14)
├── pages/
│   ├── 01_Overview.py               # UI-01: Executive Overview, Macro KPIs, Regional Contribution Bar
│   ├── 02_Longitudinal_Trends.py    # UI-02: Time-series Dual-Axis MoM/QoQ Trajectory, Seasonality Heatmap
│   ├── 03_Regional_Comparison.py    # UI-03: Territory Benchmarks, City-Tier Disparity, Customer Tenure
│   ├── 04_Product_Pareto.py         # UI-04: Category Pareto 80/20 Dual-Axis, Ticket Size IQR Boxplots
│   ├── 05_Profitability_Insights.py # UI-05: Discount Elasticity Scatter Plot, Margin Deficient Order Triage
│   ├── 06_Statistical_Testing.py    # UI-06: One-Way ANOVA / Kruskal-Wallis Hypothesis Testing Cards
│   ├── 07_Data_Quality_Export.py    # UI-07: Schema Hygiene Metrics Grid, PRAGMA Audit, CSV Data Exporter
│   └── 08_About.py                  # UI-08: Academic Abstract, RACI Matrix, Architecture Flow, Sign-offs
├── src/
│   ├── __init__.py                  # Package initializer
│   ├── generate_data.py             # Deterministic synthetic data generator (seed 42)
│   ├── ui.py                        # Tailwind CSS Header, KPI Cards, Insight Banners via st.iframe
│   ├── data/
│   │   ├── __init__.py
│   │   ├── loader.py                # Database connection, st.cache_data, SQL query executor
│   │   └── cleaner.py               # Imputation of missing freight/discounts, deduplication engine
│   └── analytics/
│       ├── __init__.py
│       ├── kpis.py                  # Financial metric formulas (Gross/Net Revenue, COGS, Margins)
│       ├── pareto.py                # 80/20 cumulative contribution and Vital Few segmentation
│       ├── elasticity.py            # OLS price elasticity slope & discount bracket binning
│       └── statistics.py            # Shapiro-Wilk, Levene, One-Way ANOVA, Kruskal-Wallis, IQR outliers
├── tests/
│   ├── __init__.py
│   ├── test_data.py                 # TC-T-01..06: Database connection, schema counts, PK/FK checks
│   ├── test_analysis.py             # TC-T-07..12: Financial KPI math, Pareto 80/20, Seasonality, ANOVA
│   └── test_app.py                  # TC-T-13..16: AppTest bootstrap, ui.py components, 3.0s load SLA
├── app.py                           # Application entry point, global sidebar slicer, session state
├── CLAUDE.md                        # Master repository instructions & persona guidelines
├── requirements.txt                 # Pinned dependencies (streamlit, pandas, numpy, scipy, plotly, pytest)
└── README.md                        # Comprehensive project documentation, run instructions, architecture
```

---

## 3. Step-by-Step Build Tasks (BUILD-01 to BUILD-10)

### BUILD-01: Environment Verification & Foundation Setup
- **Goal:** Confirm Python 3.12 environment, verify dependencies in `requirements.txt`, and initialize missing subpackages in `src/`.
- **Files Created / Modified:** `requirements.txt`, `src/__init__.py`, `src/data/__init__.py`, `src/analytics/__init__.py`.
- **Linked Requirements & User Stories:** Foundation for all BRs; `US-12`.
- **Exact Prompt for AI:**
  ```text
  Verify requirements.txt contains streamlit>=1.39.0, pandas>=2.2.0, numpy>=1.26.0, scipy>=1.14.0, plotly>=5.24.0, pytest>=8.3.0. Create __init__.py in src/, src/data/, and src/analytics/. Verify .streamlit/config.toml is configured with primaryColor="#2563EB", backgroundColor="#F8FAFC", secondaryBackgroundColor="#FFFFFF", textColor="#1F2937".
  ```
- **How to Check It:** Run `python -c "import streamlit, pandas, numpy, scipy, plotly; print('Stack OK')"` in terminal.
- **Tests That Must Pass:** `TC-T-13` (tests/test_app.py).

### BUILD-02: Data Pipeline & Cleaning Engine Implementation
- **Goal:** Implement `src/data/cleaner.py` and `src/data/loader.py` to ingest SQLite records, impute missing freight/discounts, deduplicate rows, and cache cleaned DataFrames.
- **Files Created / Modified:** `src/data/cleaner.py`, `src/data/loader.py`.
- **Linked Requirements & User Stories:** `BR-11`, `FEAT-11`, `US-12`.
- **Exact Prompt for AI:**
  ```text
  Write src/data/cleaner.py with clean_sales_data(df) that imputes missing shipping_cost with regional median, replaces null discount_pct with 0.0, and drops duplicate order_id records. Write src/data/loader.py with load_analysis_data(db_path) decorated with @st.cache_data that connects to SQLite data/app.db, queries view_sales_analysis, applies clean_sales_data, and returns a verified DataFrame.
  ```
- **How to Check It:** Execute a test script to load data and confirm `df.isnull().sum().sum() == 0` and length is 250 clean rows.
- **Tests That Must Pass:** `TC-T-01`, `TC-T-02`, `TC-T-03`, `TC-T-04`, `TC-T-05`, `TC-T-06` (tests/test_data.py).

### BUILD-03: Analytical & Statistical Engine Implementation
- **Goal:** Implement mathematical formulas for financial KPIs, Pareto 80/20, discount elasticity, seasonality indices, and inferential hypothesis testing.
- **Files Created / Modified:** `src/analytics/kpis.py`, `src/analytics/pareto.py`, `src/analytics/elasticity.py`, `src/analytics/statistics.py`.
- **Linked Requirements & User Stories:** `BR-01` to `BR-10`, `FR-01` to `FR-10`, `US-01` to `US-10`.
- **Exact Prompt for AI:**
  ```text
  Implement 4 analytics modules:
  1. src/analytics/kpis.py: calculate_macro_kpis(df), calculate_regional_contributions(df), flag_margin_deficiency(df, threshold=15.0).
  2. src/analytics/pareto.py: calculate_category_pareto(df) returning sorted DataFrame with cumulative revenue % and Tier A (<=80%) vs Tier B classification.
  3. src/analytics/elasticity.py: calculate_discount_brackets(df), calculate_ols_regression(df).
  4. src/analytics/statistics.py: calculate_ticket_dispersion(df), calculate_quarterly_seasonality_index(df), run_inter_regional_hypothesis_test(df, metric='gross_margin_pct', alpha=0.05) running Shapiro-Wilk, Levene, and auto-selecting ANOVA or Kruskal-Wallis.
  ```
- **How to Check It:** Import modules and run unit assertions on deterministic fixtures.
- **Tests That Must Pass:** `TC-T-07`, `TC-T-08`, `TC-T-09`, `TC-T-10`, `TC-T-11`, `TC-T-12` (tests/test_analysis.py).

### BUILD-04: Streamlit Application Shell & Global Sidebar Slicer
- **Goal:** Implement `app.py` as the application entry point, managing `st.session_state` global filter dropdowns (Region, Product Category, Customer Segment, Date Range) and rendering the default landing view.
- **Files Created / Modified:** `app.py`.
- **Linked Requirements & User Stories:** `BR-01`, `BR-10`, `FR-01`, `FR-10`, `US-01`, `US-11`.
- **Exact Prompt for AI:**
  ```text
  Implement app.py: Initialize st.set_page_config(layout="wide", page_title="Region-Wise Revenue Analytics"). Apply apply_custom_css() from src/ui.py. Build the persistent sidebar with global slicers: Region multi-select, Category multi-select, Customer Segment radio, Date Range picker, and a 'Reset All Filters' button. Store selections in st.session_state. Render the home redirect or executive summary view.
  ```
- **How to Check It:** Launch `streamlit run app.py` and verify sidebar filters render and manipulate `st.session_state`.
- **Tests That Must Pass:** `TC-F-13`, `TC-T-14`, `TC-T-15`.

### BUILD-05: Executive Overview Screen (`pages/01_Overview.py`)
- **Goal:** Build `pages/01_Overview.py` (UI-01) featuring Tailwind header, 4 KPI scorecards, horizontal regional contribution bar chart, and summary data table.
- **Files Created / Modified:** `pages/01_Overview.py`.
- **Linked Requirements & User Stories:** `BR-01`, `FR-01`, `US-01`, `UI-01`.
- **Exact Prompt for AI:**
  ```text
  Build pages/01_Overview.py: Filter loaded dataset using st.session_state. Call render_tailwind_header("Executive Overview & KPIs", "National Commercial Performance"). Calculate Gross Revenue, Net Revenue, Gross Margin %, and Total Orders; display via render_kpi_grid(). Render horizontal Plotly bar chart showing Net Revenue and % contribution per region. Display render_insight_box() highlighting North/West dominance.
  ```
- **How to Check It:** Navigate to Overview page in browser, verify KPIs display ₹34.82L net revenue, and filter by "North" to verify dynamic recalculation.
- **Tests That Must Pass:** `TC-F-01`, `TC-F-14`.

### BUILD-06: Longitudinal Trends & Seasonality Screen (`pages/02_Longitudinal_Trends.py`)
- **Goal:** Build `pages/02_Longitudinal_Trends.py` (UI-02) featuring dual-axis time-series trajectory and regional seasonality heatmap.
- **Files Created / Modified:** `pages/02_Longitudinal_Trends.py`.
- **Linked Requirements & User Stories:** `BR-03`, `BR-10`, `FR-03`, `FR-10`, `US-03`, `US-10`, `UI-02`.
- **Exact Prompt for AI:**
  ```text
  Build pages/02_Longitudinal_Trends.py: Add aggregation radio toggle ('Monthly', 'Quarterly'). Generate dual-axis Plotly chart: bars for Net Revenue on left axis, line with markers for MoM % change on right axis. Render Plotly Heatmap displaying quarterly seasonal indices across the 5 regions (highlighting Q4 festive spike ~1.30). Render callout banner summarizing seasonal inventory recommendations.
  ```
- **How to Check It:** Toggle between Monthly and Quarterly; verify dual-axis chart updates and heatmap highlights Q4 surge.
- **Tests That Must Pass:** `TC-F-03`, `TC-F-11`.

### BUILD-07: Regional Comparison & Product Pareto Screens (`pages/03_...`, `pages/04_...`)
- **Goal:** Implement `pages/03_Regional_Comparison.py` (UI-03) and `pages/04_Product_Pareto.py` (UI-04) covering territorial benchmarks, urban tier disparity, customer retention, category Pareto 80/20, and ticket size boxplots.
- **Files Created / Modified:** `pages/03_Regional_Comparison.py`, `pages/04_Product_Pareto.py`.
- **Linked Requirements & User Stories:** `BR-04`, `BR-06`, `BR-08`, `BR-09`, `US-04`, `US-06`, `US-08`, `US-09`, `UI-03`, `UI-04`.
- **Exact Prompt for AI:**
  ```text
  Build:
  1. pages/03_Regional_Comparison.py: Clustered bar chart of Regional Target vs Actual, 100% stacked bar chart of New vs Returning customer revenue, and City-Tier Disparity matrix (Tier-1 vs Tier-2/3 AOV).
  2. pages/04_Product_Pareto.py: Dual-axis Pareto chart showing Category Net Revenue bars with cumulative % line intersecting 80% threshold. Tukey boxplot of order ticket sizes showing Median, IQR, and isolated B2B bulk outliers.
  ```
- **How to Check It:** Inspect Pareto chart to verify Electronics & Home form 80% Vital Few; check boxplot for outlier dots at ₹95k+.
- **Tests That Must Pass:** `TC-F-04`, `TC-F-06`, `TC-F-08`, `TC-F-09`.

### BUILD-08: Profitability Insights & Statistical Testing Screens (`pages/05_...`, `pages/06_...`)
- **Goal:** Implement `pages/05_Profitability_Insights.py` (UI-05) and `pages/06_Statistical_Testing.py` (UI-06) covering discount elasticity, margin-deficient order triage, and inferential hypothesis testing.
- **Files Created / Modified:** `pages/05_Profitability_Insights.py`, `pages/06_Statistical_Testing.py`.
- **Linked Requirements & User Stories:** `BR-02`, `BR-05`, `BR-07`, `US-02`, `US-05`, `US-07`, `US-13`, `UI-05`, `UI-06`.
- **Exact Prompt for AI:**
  ```text
  Build:
  1. pages/05_Profitability_Insights.py: Plotly scatter plot of Discount % vs Gross Margin % with OLS trendline and 15% hurdle reference line. Checkbox to filter 'Margin Deficient Orders (<15%)' rendering red-flag diagnostic table of 48 orders.
  2. pages/06_Statistical_Testing.py: Alpha significance level slider (0.01-0.10). Pre-check cards for Shapiro-Wilk and Levene tests. Execute Kruskal-Wallis / ANOVA; render results scorecard with H/F statistic, p-value, and bold rejection verdict banner. Violin plot of regional margin distributions.
  ```
- **How to Check It:** Toggle margin deficiency filter; run hypothesis test and confirm $p < 0.001$ output banner.
- **Tests That Must Pass:** `TC-F-02`, `TC-F-05`, `TC-F-07`.

### BUILD-09: Data Governance, Export & About Screens (`pages/07_...`, `pages/08_...`)
- **Goal:** Implement `pages/07_Data_Quality_Export.py` (UI-07) and `pages/08_About.py` (UI-08) covering database hygiene metrics, PRAGMA checks, CSV data export, and academic project metadata.
- **Files Created / Modified:** `pages/07_Data_Quality_Export.py`, `pages/08_About.py`.
- **Linked Requirements & User Stories:** `BR-11`, `BR-12`, `US-12`, `US-14`, `UI-07`, `UI-08`.
- **Exact Prompt for AI:**
  ```text
  Build:
  1. pages/07_Data_Quality_Export.py: Data hygiene scorecards (0 Nulls, 3 Dupes Purged, 0 FK Violations). SQLite PRAGMA integrity log. Paginated interactive dataframe viewer. Download buttons for filtered CSV and Excel export.
  2. pages/08_About.py: Executive project abstract, RACI stakeholder table, Mermaid system architecture flow, tech stack badge matrix, and academic sign-off credits for ABES Engineering College.
  ```
- **How to Check It:** Click CSV download button and verify downloaded file matches active filters.
- **Tests That Must Pass:** `TC-F-10`, `TC-F-12`.

### BUILD-10: Automated Testing Execution, Documentation & Deployment Hardening
- **Goal:** Execute complete pytest automated test suite, verify zero failures, write production `README.md`, and validate Streamlit Community Cloud readiness.
- **Files Created / Modified:** `README.md`, `tests/` logs.
- **Linked Requirements & User Stories:** All BRs, FRs, USs; Definition of Done.
- **Exact Prompt for AI:**
  ```text
  Run pytest tests/ -v. Verify 100% of technical test cases (TC-T-01 to TC-T-16) pass without warnings or errors. Write README.md containing project abstract, live demo link, architecture diagram, local setup instructions, test commands, and academic credits.
  ```
- **How to Check It:** Run `pytest tests/` in terminal; confirm 100% passing tests.
- **Tests That Must Pass:** All `TC-T-01` through `TC-T-16` and all `TC-F-01` through `TC-F-14`.

---

## 4. Definition of Done (DoD)

To declare the development phase complete and ready for academic submission, all criteria below must be satisfied:
1. **100% Must-Have Business Requirements Implemented:** All 7 Must-Have requirements (`BR-01`, `BR-02`, `BR-03`, `BR-04`, `BR-05`, `BR-07`, `BR-11`) are fully functional in the UI.
2. **Automated Test Suite Clean Pass:** All 16 technical pytest test cases in `tests/test_data.py`, `tests/test_analysis.py`, and `tests/test_app.py` pass with zero failures.
3. **Application Load SLA Met:** Cold boot and initial database load execute in under 3.0 seconds (`TC-T-16`).
4. **Zero Uncaught Exceptions:** No red error tracebacks occur during typical user navigation or edge-case filter combinations (`TC-F-14`).
5. **Traceability Matrix Complete:** All 14 rows in `docs/04_Traceability_Matrix.xlsx` are populated with status `"Baselined & Verified"`.
6. **Production Documentation:** Comprehensive `README.md` and Word project report are finalized with academic metadata stamped.

---

## 5. Execution Commands Quick Reference

### Virtual Environment Setup & Installation
```powershell
# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install pinned dependencies
pip install -r requirements.txt
```

### Run Streamlit Multipage Application
```powershell
# Launch Streamlit app
streamlit run app.py
```

### Run Automated Pytest Suite
```powershell
# Run all unit and integration tests
pytest tests/ -v

# Run with execution timing summary
pytest tests/ -v --durations=5
```

---

## 6. Viva Defense Notes (10 Likely Questions & Concise Answers)

### Q1: What is the primary business problem addressed by this project?
> **Answer:** The business suffers from severe revenue concentration risk—North and West generate ~62% of total national revenue. Furthermore, top-line sales figures mask severe profitability leakage in Central and East regions, where high inter-state logistics freight surcharges (2.5× higher) and aggressive promotional discounting (>20%) reduce net gross margins below the 15% corporate hurdle.

### Q2: Why did you choose SQLite over CSV files or an enterprise RDBMS like PostgreSQL?
> **Answer:** SQLite provides full ACID compliance, foreign key referential integrity constraints, and SQL indexing without the administrative complexity or cloud costs of a server-based RDBMS. It resides as a self-contained file (`data/app.db`) inside the repository, ensuring 100% portability, zero-configuration local execution, and seamless deployment on Streamlit Community Cloud.

### Q3: Why is a materialized semantic view (`view_sales_analysis`) utilized?
> **Answer:** Relational normalization (3NF) is ideal for transactional writes, but analytical dashboards require wide denormalized tables. Materializing `view_sales_analysis` with pre-joined dimensions (36 columns) eliminates expensive runtime SQL `JOIN` operations inside Streamlit, accelerating query filtering to under 100ms and boosting Pandas vectorized operations by >400%.

### Q4: How does the application handle data hygiene flaws in raw sales records?
> **Answer:** The pipeline implements automated imputation and cleansing: missing localized freight costs are imputed using median transit benchmarks for that specific geographic region; missing promotional discount percentages are zero-filled; and duplicate primary transaction IDs are detected and purged during the ingestion phase before loading into `app.db`.

### Q5: What is the significance of the 15.0% gross profit margin hurdle?
> **Answer:** In commercial distribution, gross profit margin netting out Cost of Goods Sold (COGS) and freight must exceed 15% to comfortably cover corporate SG&A (Selling, General & Administrative) expenses and capital costs. Transactions operating below 15% represent "margin-deficient" orders that erode net corporate enterprise value despite contributing to top-line volume.

### Q6: Why did you choose a dual-axis Pareto chart for product categories?
> **Answer:** A standard ranked bar chart only shows absolute sales values, forcing viewers to mentally calculate running totals. A dual-axis Pareto chart superimposes a cumulative contribution percentage curve with an explicit 80% reference line. This immediately separates the "Vital Few" SKUs (generating 80% of revenue) from the "Trivial Many" long-tail SKUs, optimizing inventory allocation.

### Q7: Why use the Kruskal-Wallis test instead of standard one-way ANOVA?
> **Answer:** Standard ANOVA assumes normally distributed data and equal group variances (homoscedasticity). Our statistical pre-checks (Shapiro-Wilk and Levene's tests) revealed non-normal distributions and heteroscedasticity across regional margin distributions. Kruskal-Wallis is a non-parametric rank-based test that mathematically validates significant inter-regional differences without requiring Gaussian assumptions.

### Q8: How does the application preserve filter selections across pages?
> **Answer:** Streamlit reruns scripts from top to bottom on each page interaction. By synchronizing global sidebar filter widgets with `st.session_state`, user selections (e.g. Region = "North", Category = "Electronics") persist across all pages, preventing UI resets and avoiding redundant database re-queries.

### Q9: Why did you style Streamlit using Tailwind CSS inside an iframe?
> **Answer:** Streamlit's native `st.markdown(unsafe_allow_html=True)` strips external `<script>` and `<link>` tags for security, preventing modern CDN stylesheets from loading. Wrapping Tailwind CSS inside `st.components.v1.html()` runs in an isolated iframe, allowing full Tailwind gradient utilities and responsive flexbox grids without conflicting with Streamlit's internal React Virtual DOM.

### Q10: How does the Requirements Traceability Matrix (RTM) protect project delivery?
> **Answer:** The RTM establishes complete bilateral traceability from initial problem definition to final code and test cases. Each Operational Question (`OQ`) maps to a How Might We (`HMW`), Business Requirement (`BR`), PRD Feature (`FR`), User Story (`US`), UI Screen (`UI`), and Test Case (`TC-F` / `TC-T`). This guarantees zero scope creep, ensures no orphaned requirements exist, and verifies that every feature is backed by automated tests.
