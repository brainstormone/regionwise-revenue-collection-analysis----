# Regionwise Revenue Collection Analysis & Executive Decision Support System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-SQLite3-brightgreen.svg)](https://sqlite.org/)
[![Tests](https://img.shields.io/badge/Tests-16%20Passed-success.svg)](tests/)
[![Status](https://img.shields.io/badge/Status-Production%20Live-darkred.svg)](#)

A production-grade Commercial Revenue Analytics & Decision Support Platform built for enterprise multi-zone sales intelligence, margin diagnostics, pricing elasticity evaluation, and territory performance optimization. Developed as the capstone academic deliverable for the **MCA 2nd Year (Data Analytics Specialization)** at **ABES Engineering College, Ghaziabad** in partnership with the **HCLTech Career Shaper Programme**.

---

## 📁 Project Directory Structure

```text
rw-collection-analysis/
│
├── .streamlit/
│   └── config.toml
│
├── data/
│   ├── app.db
│   ├── dim_customers.csv
│   ├── dim_products.csv
│   ├── dim_regions.csv
│   ├── fact_sales.csv
│   ├── region_wise_revenue_data.xlsx
│   └── view_sales_analysis.csv
│
├── docs/
│   ├── 01_Project_Understanding.docx
│   ├── 01_name_project_understanding.docx
│   ├── 02_HMW_Statements.docx
│   ├── 03_Needs_Analysis.docx
│   ├── 04_Traceability_Matrix.xlsx
│   ├── 05_BRD.docx
│   ├── 07_TRD.docx
│   ├── 08_Database_Design.xlsx
│   ├── 09_ER_Diagram.docx
│   ├── 09_ER_Diagram.png
│   ├── 10_Data_Validation_Report.docx
│   ├── 11_User_Stories.docx
│   ├── 12_UI_Framework.docx
│   ├── 13_Test_Cases.docx
│   ├── 14_BUILD_PLAN.docx
│   ├── 16_Cloud_Deployment.docx
│   ├── PRJ-DA-01_Presentation.pptx
│   └── PRJ-DA-01_Project_Document.docx
│
├── pages/
│   ├── 01_Overview.py
│   ├── 02_Longitudinal_Trends.py
│   ├── 03_Regional_Comparison.py
│   ├── 04_Product_Pareto.py
│   ├── 05_Profitability_Insights.py
│   ├── 06_Statistical_Testing.py
│   ├── 07_Data_Quality_Export.py
│   └── 08_About.py
│
├── src/
│   ├── analytics/
│   │   ├── __init__.py
│   │   ├── elasticity.py
│   │   ├── kpis.py
│   │   ├── pareto.py
│   │   └── statistics.py
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   ├── cleaner.py
│   │   └── loader.py
│   │
│   ├── __init__.py
│   ├── generate_data.py
│   └── ui.py
│
├── tests/
│   ├── test_analysis.py
│   ├── test_app.py
│   └── test_data.py
│
├── .gitattributes
├── .gitignore
├── BUILD_PLAN.md
├── CLAUDE.md
├── README.md
├── app.py
├── requirements-dev.txt
└── requirements.txt
```

### Directory Overview

| Directory/File | Description |
|---|---|
| `.streamlit/` | Streamlit application configuration |
| `data/` | SQLite database and project datasets |
| `docs/` | Project reports, requirements, design documents and presentation |
| `pages/` | Eight interactive dashboard pages |
| `src/analytics/` | KPI calculations, Pareto analysis, statistical testing and discount analysis |
| `src/data/` | Data loading and cleaning modules |
| `tests/` | Automated application, data and analytics tests |
| `app.py` | Main Streamlit application entry point |
| `generate_data.py` | Generates project datasets and database |
| `requirements.txt` | Application dependencies |
| `requirements-dev.txt` | Development and testing dependencies |


## 📌 Project Overview

| Attribute | Details |
| :--- | :--- |
| **Project ID** | `P056` |
| **Project Title** | Regionwise Revenue Collection Analysis |
| **Domain** | Commercial Sales Analytics / Python Data Analytics |
| **Institution** | ABES Engineering College |
| **Programme** | MCA – Second Year (Data Analytics) |
| **Batch ID** | `ABES_OND26_MCA 2nd Year_Data Analytics_Batch 01` |
| **Learner Name** | **Abhishek Kumar Mishra** |
| **University Roll Number** | `2500320140006` |
| **Project Mentor** | **Mr. Dinesh Sereno** |
| **Data Analytics Mentor** | Mr. Dinesh |
| **FSD Java Mentor** | Ms. Charsini |
| **FSD Python Mentor** | Mr. Madana |
| **Release Version** | v1.0.0 (Production Release — November 2026) |

---


## 🚀 Key Business Findings & Diagnostics

* **Revenue Concentration (62.1% Skew)**: The **North** (32.2%) and **West** (29.9%) zones account for 62.1% of national commercial revenue, powered by enterprise IT Hardware and Cloud SaaS contracts in Delhi NCR, Mumbai, and Bengaluru.
* **Severe Margin Erosion in Central & East (<15% GM)**: While North delivers 41.2% gross margin, Central (14.2%) and East (12.8%) suffer from heavy freight penalization (2.5× national average) and excessive discounting (>20%).
* **Statistical Significance Confirmed**: Kruskal-Wallis non-parametric testing ($H = 28.64, p = 0.000009 < 0.001$) confirms territorial gross margin variance is statistically significant, necessitating distinct regional pricing tiers rather than uniform national price sheets.
* **Pareto 80/20 Distribution**: 20% of SKU offerings (principally Enterprise Server Racks and Enterprise CRM Seats) generate 78.4% of aggregate gross profit.

---

