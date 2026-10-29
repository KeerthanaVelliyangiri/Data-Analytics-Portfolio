
# Novitech Manufacturing Performance Dashboard

## Business Problem

### How can Novitech Manufacturing improve production performance and reduce operational costs?

Novitech Manufacturing needs to monitor production output, product defects, machine downtime, procurement spending, and supplier performance. Without a centralized dashboard, identifying production issues and potential financial risks becomes difficult.

**Business Objective**
- Compare planned and actual production performance.
- Monitor product defects and machine downtime.
- Identify potential financial exposure caused by defects.
- Analyze procurement spending and supplier performance.
- Support data-driven operational decisions.

**Solution**

Developed an interactive Power BI dashboard to monitor manufacturing performance, quality, operations, and financial indicators in one place.

---

## Dataset / Source Details

| Dataset / Table | Purpose |
|---|---|
| `fact_production_runs` | Analyze production output |
| `fact_purchase_orders` | Analyze procurement spending |
| `dim_plants` | Compare manufacturing plants |
| `dim_products` | Analyze product performance |
| `dim_suppliers` | Evaluate supplier performance |
| `dim_raw_materials` | Monitor raw materials |
| `bridge_bill_of_materials` | Connect products with required materials |
| `dim_operators` | Support operator-related analysis |

---


## Dashboard

![Novitech Manufacturing Dashboard](/Screenshot/screenshot.png)


### Business Questions and Dashboard Solutions

| Business Question | Dashboard Solution | Business Use |
|---|---|---|
| How much production was completed? | Production KPI cards and trend charts | Monitor production output |
| How many defects occurred? | Defect rate and quality charts | Identify quality issues |
| How much downtime occurred? | Downtime KPI and charts | Monitor operational interruptions |
| What is the potential financial impact of defects? | Estimated defect cost exposure | Monitor potential quality-related costs |
| How much was spent on procurement? | Procurement spending KPI and chart | Monitor purchasing expenses |
| How can supplier performance be monitored? | Supplier performance charts | Identify supply-chain risks |

---

## KPIs

### 1. Total Production
Measures the total quantity produced during the selected period.

### 2. Defect Rate
Shows the proportion of defective units compared with total production.

### 3. Total Downtime
Measures the total recorded machine downtime.

### 4. Total Procurement Spend
Shows the procurement spending recorded in purchase-order data.

### 5. Estimated Defect Cost Exposure
Estimates the potential financial exposure associated with product defects. This is an estimate, not a confirmed actual loss.

---

## Dashboard Features

1. **Production Performance Analysis** – Monitors production output across plants and periods.
2. **Quality Analysis** – Examines defective units and defect rates.
3. **Downtime Analysis** – Helps identify machine downtime patterns.
4. **Financial Exposure Analysis** – Displays estimated defect-related cost exposure.
5. **Procurement Analysis** – Tracks purchasing expenditure.
6. **Supplier Performance Analysis** – Supports analysis of supplier delays and supply-chain risks.

---

## Tools / Power BI Techniques Used

- Power BI Desktop
- Power Query for data cleaning and transformation
- DAX for calculated measures and KPIs
- Data modeling and table relationships
- Interactive slicers and filters
- KPI cards and data visualizations
- Dashboard formatting and layout design

---

## Key Measures

### Total Production

```DAX
Total_Production =
SUM(fact_production_runs[quantity_produced])
```

### Defect Rate

Use the defect-rate measure created in your Power BI model to calculate the percentage of defective units.

### Total Downtime

Use your downtime measure to summarize recorded machine downtime.

### Total Procurement Spend

Use your procurement-spend measure to summarize purchase-order expenditure.

### Estimated Defect Cost Exposure

Use your estimated defect-cost measure to monitor potential quality-related financial exposure.

---

## Dashboard Filters

- **Plant:** Filter manufacturing performance by plant.
- **Product:** Analyze performance for selected products.
- **Date:** View data for a selected period.

---

## Key Insights

1. **Production Performance:** Compare production output across periods and plants.
2. **Quality Performance:** Identify products or plants with higher defect rates.
3. **Downtime Monitoring:** Examine downtime patterns that may affect production.
4. **Financial Exposure:** Identify areas with higher estimated defect-related cost exposure.
5. **Procurement Spending:** Compare procurement expenditure across available categories and periods.
6. **Supplier Performance:** Identify delayed purchase orders and potential supply-chain risks.

---

## Recommendations / Conclusion

### Recommendations

- Monitor production output regularly to identify production gaps.
- Investigate plants or products with higher defect rates.
- Review machine downtime to identify opportunities for improvement.
- Track estimated defect cost exposure and investigate its main contributors.
- Monitor procurement spending to support cost control.
- Review delayed purchase orders and supplier performance.

### Conclusion

The Novitech Manufacturing Performance Dashboard provides a centralized view of production, quality, downtime, procurement, and potential financial exposure. It helps stakeholders monitor manufacturing performance and make data-driven decisions.

---

## Project Outcome

- Developed an interactive Power BI dashboard for manufacturing performance analysis.
- Created KPI measures to monitor business indicators.
- Used Power Query, DAX, and data modeling techniques.
- Presented manufacturing and procurement information in a business-focused format.
- Designed the dashboard to help identify operational issues and potential risks.
