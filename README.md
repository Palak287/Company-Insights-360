# 📊 Company Insights 360°

### End-to-End Business Analytics Project using Python, SQL & Power BI

> An end-to-end Data Analytics project that transforms Superstore sales data into actionable business insights using Python for data analysis, MySQL for business-driven SQL analysis, and Power BI for interactive executive reporting.

---

## 📌 Project Overview

**Company Insights 360°** is an end-to-end Business Intelligence and Data Analytics project designed to help management understand the company's sales, profitability, customer, product, category, and regional performance.

The project follows a complete analytics workflow:

**Raw Data → Data Inspection → Python Analysis → SQL Business Analysis → KPI Development → Power BI Dashboard → Business Insights**

The objective is not only to analyze historical data, but also to identify areas of strong performance, low profitability, customer-level opportunities, and areas requiring management attention.

---

# 🎯 Business Problem

Management needs a centralized view of business performance to answer important questions such as:

- How much revenue and profit is the company generating?
- How is business performance changing over time?
- Which regions generate the highest sales and profit?
- Which product categories and sub-categories are most profitable?
- Which products generate high sales but low profit?
- Which customers contribute the most revenue?
- Which customers are generating losses?
- How does profitability vary across customer segments?
- How are discounts associated with profitability?
- Which areas of the business require further investigation?

The project addresses these questions through **Python, SQL and Power BI**.

---

# 🎯 Project Objectives

The major objectives of this project are:

- Analyze overall business performance.
- Calculate important business KPIs.
- Identify high-performing and underperforming regions.
- Analyze category and sub-category profitability.
- Identify high-value and loss-making customers.
- Analyze product-level sales and profitability.
- Analyze state and city-level performance.
- Study year-wise sales and profit trends.
- Analyze customer segment performance.
- Examine the relationship between discounts and profitability.
- Build an interactive executive dashboard using Power BI.
- Convert analytical findings into business recommendations.

---

# 🛠️ Tools & Technologies

| Tool / Technology | Purpose |
|---|---|
| Python | Data inspection, cleaning and exploratory analysis |
| Pandas | Data manipulation and analysis |
| MySQL | SQL business analysis and KPI calculations |
| Power BI | Interactive dashboard and visualization |
| DAX | KPI measures and calculations |
| GitHub | Version control and portfolio presentation |

---

# 📂 Dataset

The project uses the **Sample Superstore dataset** containing sales transactions across customers, products, categories, regions and time periods.

### Dataset Information

| Attribute | Value |
|---|---:|
| Total Rows | 9,994 |
| Total Columns | 21 |
| Start Date | January 3, 2014 |
| End Date | December 30, 2017 |
| Total Orders | 5,009 |
| Total Customers | 793 |

### Important Columns

- Row ID
- Order ID
- Order Date
- Ship Date
- Ship Mode
- Customer ID
- Customer Name
- Segment
- Country
- City
- State
- Postal Code
- Region
- Product ID
- Category
- Sub-Category
- Product Name
- Sales
- Quantity
- Discount
- Profit

---

# 📁 Project Structure

```text
Company-Insights-360/
│
├── data/
│   └── Sample_Superstore.csv
│
├── Power BI/
│   └── Company_Insights_360.pbix
│
├── python/
│   ├── 01_data_inspection.py
│   └── 02_create_sql_import.py
│
├── SCREENSHOTS/
│   ├── Executive_Overview.png
│   ├── Profitability_Product_Analysis.png
│   └── Customer_Regional_Insights.png
│
├── sql/
│   ├── 01_business_analysis.sql
│   └── superstore_import.sql
│
└── README.md