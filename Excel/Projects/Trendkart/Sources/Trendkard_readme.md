# 👗 TrendMart Fashion Enterprise 

## 📌 Project Overview

TrendMart Fashion Enterprise –  is an **Excel-based data analytics project** developed to provide a consolidated view of TrendMart's commercial and profitability performance.

The project analyzes **sales, cost, profit, profit margin, discounts, returns, product categories, sales channels, cities, stores, and transaction performance** to help management understand where sales are being generated and where potential profitability requires further investigation.

---

## 🎯 Business Problem

TrendMart is generating sales across multiple products, categories, stores, and sales channels. However, management does not have a consolidated analytical view to understand whether strong sales activity is translating into strong and sustainable profitability.

Potential profitability pressure may be associated with:

- Product costs
- Discount levels
- Returns
- Product/category performance
- Store and regional performance
- Sales channel differences

The key business question is:

> **Where is TrendMart losing potential profitability despite generating sales, and which business areas require management attention?**

The analysis investigates:

- Sales and profit performance
- Cost and profitability
- Discount levels and profit
- Return activity
- Category performance
- Online vs Offline performance
- City and regional performance
- Monthly sales and profit trends

The project focuses on understanding **both sales and profitability**, since high sales do not always indicate strong profitability.

---

## 🎯 Business Objectives

- Monitor overall sales, cost, profit, and profit margin performance
- Identify major sales and profitability patterns
- Compare sales against cost and profit
- Investigate discount levels alongside profitability
- Identify return patterns
- Compare product category performance
- Compare Online and Offline sales-channel performance
- Compare city and regional performance
- Identify areas requiring further investigation
- Support data-driven business decisions
- Provide management with a consolidated profitability view

---

## 🛠️ Tools & Excel Techniques Used

### Tools

- Microsoft Excel

### Excel Techniques

- Data Cleaning
- Excel Tables
- Calculated Columns
- Excel Formulas
- PivotTables
- PivotCharts
- Slicers
- KPI Cards
- Conditional Formatting
- Percentage Calculations
- Date Grouping
- Business KPI Calculation
- Dashboard Design
- Interactive Filtering

---

## 🧹 Data Cleaning & Analysis

The TrendMart dataset was reviewed and prepared for analysis based on the documented Data Quality Log.

The data preparation included:

- Checking duplicate invoice numbers
- Reviewing blank Customer IDs
- Reviewing blank Product IDs
- Reviewing blank Employee IDs
- Standardizing mixed date formats
- Converting numeric values stored as text
- Removing unnecessary spaces
- Standardizing payment mode values
- Reviewing negative profit records
- Reviewing zero-quantity records
- Standardizing Return Status values
- Reviewing duplicate customer phone numbers
- Reviewing invalid email values
- Standardizing customer membership values
- Reviewing duplicate product names
- Standardizing category spellings
- Reviewing blank product brands
- Reviewing store manager information
- Standardizing employee and store status values

The analysis also included:

- Creating Invoice Year and Invoice Month fields
- Calculating Profit Margin
- Calculating business KPIs
- Creating PivotTables
- Creating PivotCharts
- Connecting dashboard visuals with slicers
- Comparing sales, cost, and profit across business dimensions

---

# 📊 Dashboard

The Excel dashboard provides an interactive management-level view of TrendMart's commercial and profitability performance.

### Dashboard Features

- Total Sales
- Total Profit
- Total Profit Margin
- Average Discount %
- Monthly Sales & Profit Trend
- Discount-level Sales & Profit
- Return Status Analysis
- Online vs Offline Performance
- City Performance
- Category Sales, Cost & Profit
- Invoice Year Filter
- Discount % Filter

### Dashboard Questions

The dashboard is designed around business questions:

- **Why did Sales & Profit decline?**
- **Which Discount Works Best?**
- **How Many Orders Were Returned?**
- **Online or Offline: Who Wins?**
- **Which Cities Perform Best?**
- **How Do Categories Perform?**

The dashboard focuses on helping management move from simply asking **"How much did we sell?"** to understanding **where sales and profitability patterns require further investigation.**

---

# 📌 KPIs

The dashboard contains four major KPI cards:

| KPI | Value | Purpose |
|---|---:|---|
| 💰 Total Sales | ₹92.27 L | Measures overall sales generated |
| 📈 Total Profit | ₹18.01 L | Measures total profit generated |
| 📊 Profit Margin | 19.52% | Measures profitability relative to sales |
| 💸 Average Discount | 12.57% | Measures average discount applied |

### Additional Business Measures

The dataset also supports:

- Total Cost
- Total Transactions
- Total Quantity Sold
- Discount Amount
- Return Status
- Sales Channel
- Category Performance
- City Performance

### KPI Interpretation

**Total Sales:**  
Shows the overall revenue generated by TrendMart.

**Total Profit:**  
Shows the profit generated from the analyzed transactions.

**Profit Margin:**  
Shows profit relative to sales and provides a profitability view beyond revenue alone.

**Average Discount:**  
Shows the average discount level applied across transactions.

---

# 🔍 Key Insights

## 1. 📉 Sales and Profit Show a Significant Decline in 2025

The monthly analysis shows strong sales and profit activity during several months of 2024, with **October 2024 recording the highest monthly sales and profit** in the analyzed period.

Sales and profit then decline substantially during several months of 2025.

### Business Impact

The decline indicates a period that requires further investigation.

Management can investigate:

- Discount levels
- Product/category mix
- Sales channel performance
- City and regional performance
- Return activity
- Transaction activity

The dashboard identifies the decline but does not assume a single cause without additional analysis.

---

## 2. 💸 Higher Discount Levels Show Lower Observed Profit

The discount analysis compares sales and profit across discount levels from 0% to 30%.

The analysis shows that:

- 0% discount records generate the highest sales and profit contribution.
- Profit contribution decreases substantially at higher discount levels.
- The 30% discount level shows very low profit compared with lower discount levels.

### Business Impact

Higher discount levels are associated with lower observed profit in the analyzed data.

However, this is an **observed relationship and does not by itself prove that discounting caused the profit decline**.

### Opportunity

Management can further investigate discount performance by:

- Category
- Product
- Store
- Sales Channel
- Customer segment

This can help identify where discounting is associated with weaker profitability.

---

## 3. 🔄 Returned Orders Require Monitoring

The dataset contains both Returned and Not Returned transactions.

The analysis identifies:

- Returned records: **146**
- Not Returned records: **2,854**

This represents approximately **4.87% of transaction records marked as Returned**.

### Business Impact

Returns can affect commercial performance and should be monitored across different business dimensions.

### Opportunity

TrendMart can further analyze return activity by:

- Product
- Category
- Store
- City
- Sales Channel
- Customer segment

This can help identify areas requiring further investigation.

---

## 4. 👗 Category Performance Differs Across Sales, Cost and Profit

The category analysis compares:

- Sales Amount
- Cost Amount
- Profit

The analysis shows that category performance differs across these measures.

For example:

- **Women Sarees** has the highest sales contribution among the analyzed categories.
- **Handbags** records a high sales contribution and strong profit contribution.
- **Watches** also contributes significantly to sales and profit.
- Cost varies considerably across categories.

### Business Impact

High sales alone do not provide a complete view of category performance.

Management should consider:

> **Sales + Cost + Profit**

when evaluating category performance.

### Opportunity

TrendMart can investigate category performance further at:

- Subcategory level
- Brand level
- Product level
- Discount level
- Return level

---

## 5. 🛒 Offline Sales Contribute More Than Online Sales

The dashboard compares the two major sales channels.

### Observed Performance

- **Offline Sales:** ₹60.49 L
- **Online Sales:** ₹31.78 L

Profit contribution is also higher for Offline sales in absolute value.

### Business Impact

The analysis shows that Offline is the larger sales channel in the current dataset.

### Opportunity

Management can compare Online and Offline performance using:

- Profit Margin
- Discount levels
- Product mix
- Return activity
- Category performance

This can help identify differences between the two channels.

---

## 6. 🌆 City Performance Varies Across Locations

The city-level analysis compares sales and profit across different TrendMart locations.

The dashboard allows management to compare city-level performance and identify locations that contribute strongly to sales and profit.

### Business Impact

Different city locations contribute differently to overall commercial performance.

### Opportunity

Management can drill down from:

> **Region → State → City → Store**

to identify areas requiring further investigation.

---

## 7. 📊 Sales, Cost and Profit Should Be Evaluated Together

The category chart combines:

- Sales Amount
- Cost Amount
- Profit

This provides a broader profitability view than looking at sales alone.

### Business Impact

A category can generate strong sales while also carrying a high cost base.

Therefore, management should evaluate category performance using both revenue and profitability measures.

### Opportunity

Further analysis can identify:

- High-sales / low-profit categories
- High-cost categories
- High-margin categories
- Categories with higher return activity
- Categories affected by higher discount levels

---

## 8. 📅 Monthly Performance Requires Further Investigation

The monthly trend shows significant variation in sales and profit across the analyzed period.

The dashboard highlights periods of stronger and weaker performance.

### Business Impact

Large changes in monthly performance require investigation rather than being treated as a single business cause.

### Opportunity

Management can compare weaker months against:

- Discount levels
- Product categories
- Sales channels
- Returns
- Cities
- Transaction volume

to understand the patterns associated with the change.

---

# 💡 Recommendations

Based on the analysis, the following actions are recommended for TrendMart:

### 1. Monitor Sales and Profit Trends

Track monthly sales and profit regularly to identify significant changes and investigate weaker periods.

### 2. Evaluate Discounts Alongside Profitability

Monitor discount levels together with profit and profit margin rather than evaluating discounts using sales alone.

### 3. Monitor Returns

Track return activity by:

- Product
- Category
- Store
- City
- Sales Channel

to identify areas requiring further investigation.

### 4. Balance Sales and Profitability

Evaluate categories and products using:

- Sales
- Cost
- Profit
- Profit Margin

instead of focusing only on sales volume.

### 5. Review Category Performance

Identify categories with:

- High sales
- High cost
- Low profit
- Strong profit contribution

to support better product and merchandising decisions.

### 6. Compare Online and Offline Performance

Continue monitoring both sales channels and investigate differences in:

- Discount levels
- Product mix
- Profitability
- Return activity

### 7. Monitor City and Regional Performance

Compare city and regional performance regularly and drill down to individual stores where required.

### 8. Investigate Potential Profitability Leakage

Use the dashboard to identify combinations of:

- High sales
- High cost
- High discount
- Low profit
- Higher return activity

that require deeper business investigation.

---

# 🎯 Conclusion

The TrendMart Profitability Leakage Analysis dashboard provides a consolidated view of business performance across **sales, profit, profit margin, discounts, returns, categories, sales channels, and city performance**.

The analysis shows that TrendMart should not evaluate performance using sales alone.

**Cost, profit, discount levels, return activity, product/category performance, channel performance, and regional performance** should also be considered when evaluating commercial performance.

The dashboard helps management identify important business patterns and areas requiring further investigation, supporting **data-driven business decisions**.

---

## 🚀 Project Outcome

This project demonstrates practical skills in:

- Excel Data Analysis
- Data Cleaning
- Business Problem Solving
- Business Requirement Analysis
- KPI Development
- PivotTable Analysis
- PivotChart Development
- Data Visualization
- Interactive Dashboard Development
- Profitability Analysis
- Business Insight Generation
- Data-Driven Recommendations
