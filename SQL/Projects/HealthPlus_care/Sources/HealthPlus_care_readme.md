# HealthPlus Healthcare Database Analysis

## Business Problem

### How can HealthPlus gain a consolidated view of healthcare operations, patient service utilization, resource usage, and financial performance?

HealthPlus maintains data across members, consultations, specialists, clinics, telemedicine, chronic-care programs, health packages, corporate members, prescriptions, laboratory services, insurance claims, billing, payments, staff, and patient feedback.

The business challenge is that these data areas need to be analyzed together to understand:

* How healthcare services are being utilized across clinics
* How consultation workload is distributed among specialists
* Which members are actively using healthcare services
* How effectively telemedicine services are performing
* How chronic-care programs are being utilized
* Which health packages have higher adoption
* How corporate healthcare programs are being utilized
* Which medicines and laboratory services have higher demand
* How insurance claims are performing
* Whether billed amounts are being successfully collected
* How patients are experiencing healthcare services
* How staff resources are distributed across clinics

Without consolidated analysis, management may find it difficult to identify workload concentration, service utilization patterns, operational gaps, and financial collection issues.

---

## Business Objective

**Analyze healthcare operations, member activity, service utilization, resource allocation, patient experience, and financial transactions to support data-driven healthcare management decisions.**

---

## Business Solution

HealthPlus can use SQL-based analysis to:

1. **Monitor clinic and specialist workload**

   * Compare consultation volumes across clinics
   * Measure specialist consultation activity
   * Identify workload concentration
   * Support workload and resource planning

2. **Understand member engagement**

   * Analyze consultations per member
   * Identify highly active members
   * Identify members with no consultation activity
   * Understand healthcare service utilization

3. **Evaluate telemedicine performance**

   * Analyze session status
   * Measure average session duration
   * Monitor connection quality
   * Identify dropped-session patterns

4. **Monitor chronic-care programs**

   * Analyze chronic conditions
   * Track active and inactive programs
   * Monitor specialist involvement
   * Identify conditions with higher program enrollment

5. **Analyze health package adoption**

   * Measure package subscriptions
   * Compare package popularity
   * Monitor active and expired subscriptions
   * Understand package utilization

6. **Measure corporate healthcare engagement**

   * Analyze corporate member enrollment
   * Calculate enrollment penetration
   * Compare corporate participation
   * Support corporate healthcare planning

7. **Analyze prescriptions and laboratory services**

   * Identify frequently prescribed medicines
   * Measure specialist prescription workload
   * Analyze laboratory test volume
   * Compare laboratory service costs

8. **Monitor insurance claims**

   * Analyze claim volume
   * Compare claim amounts
   * Monitor claim status
   * Analyze insurance-provider patterns

9. **Monitor billing and payment collection**

   * Calculate total billed amount
   * Analyze payment status
   * Measure successful collections
   * Identify collection gaps

10. **Evaluate patient experience**

    * Analyze feedback ratings
    * Compare clinic satisfaction
    * Identify missing feedback
    * Monitor service-quality patterns

11. **Analyze workforce distribution**

    * Measure staff count by clinic
    * Analyze employment types and designations
    * Compare staff availability with consultation workload
    * Support workforce planning

---

# Database Structure

The HealthPlus database contains interconnected healthcare tables covering members, healthcare services, specialists, clinics, telemedicine, chronic care, packages, corporate programs, prescriptions, laboratory services, insurance, billing, payments, staff, and feedback.

## Main Tables

| Table                   | Purpose                                                                          |
| ----------------------- | -------------------------------------------------------------------------------- |
| `Members`               | Stores member registration and membership information                            |
| `Clinics`               | Stores clinic information and locations                                          |
| `Specialists`           | Stores specialist information, specialization, experience, and consultation fees |
| `Consultations`         | Stores member consultation and service activity                                  |
| `Telemedicine_Sessions` | Stores online consultation sessions and connection information                   |
| `Chronic_Care_Programs` | Stores chronic-care enrollment and program status                                |
| `Health_Packages`       | Stores healthcare package details                                                |
| `Package_Subscriptions` | Stores member package subscriptions                                              |
| `Corporates`            | Stores corporate client information                                              |
| `Corporate_Members`     | Stores corporate member enrollment                                               |
| `Prescriptions`         | Stores medicines prescribed during consultations                                 |
| `Lab_Tests`             | Stores laboratory test activity and cost                                         |
| `Claims`                | Stores insurance claim information                                               |
| `Staff`                 | Stores clinic staff and employment information                                   |
| `Billing`               | Stores healthcare billing information                                            |
| `Payments`              | Stores payment transactions                                                      |
| `Feedback`              | Stores member feedback and ratings                                               |

---

# Healthcare Process

The major healthcare service flow can be understood as:

**Member → Consultation → Specialist / Clinic → Telemedicine / Prescription / Lab Test → Billing / Claim → Payment → Feedback**

The database also connects members with chronic-care programs, health packages, and corporate healthcare programs.

---

# SQL Business Analysis

## 1. Clinic Workload Analysis

### Business Problem

HealthPlus needs to understand how consultation workload is distributed across clinics.

### SQL Analysis

* Count consultations by clinic
* Compare clinic consultation volumes
* Identify clinics with higher workloads
* Use joins to connect clinics and consultations
* Rank clinics based on consultation activity

### Key Insight

**HealthPlus Diagnostic Clinic - Kozhikode (C001)** recorded the highest consultation workload with **945 consultations**.

### Business Recommendation

Monitor high-workload clinics and review staffing and resource allocation to maintain service efficiency.

---

# 2. Specialist Workload Analysis

### Business Problem

Consultation workload may not be evenly distributed among specialists.

### SQL Analysis

* Count consultations by specialist
* Compare specialist workload
* Use `HAVING` to identify specialists above a workload threshold
* Rank specialists using window functions

### Key Insight

**Charu Rao (SP0004), ENT Specialist**, recorded **391 consultations**.

### Business Recommendation

Monitor specialist workload concentration and consider workload balancing where service demand is consistently high.

---

# 3. Member Engagement Analysis

### Business Problem

HealthPlus needs to identify how actively registered members are using healthcare services.

### SQL Analysis

* Count consultations per member
* Identify members with repeated consultations
* Identify members without consultation activity
* Use `LEFT JOIN` to retain members without consultations
* Use `ROW_NUMBER()`, `LAG()`, and `LEAD()` for member consultation sequences

### Key Insight

**224 registered members had no consultation activity.**

### Business Recommendation

Analyze inactive members and consider suitable engagement strategies to improve healthcare-service utilization.

---

# 4. Telemedicine Performance Analysis

### Business Problem

HealthPlus needs to monitor the quality and reliability of telemedicine services.

### SQL Analysis

* Count total telemedicine sessions
* Analyze completed and dropped sessions
* Calculate average session duration
* Analyze connection quality
* Calculate drop rates by connection quality

### Key Insight

The database contains **2,200 telemedicine sessions**:

* **1,465 completed**
* **735 dropped**
* Average session duration: approximately **21.43 minutes**

Poor connection quality recorded the highest observed drop rate at approximately **38.30%**.

### Business Recommendation

Monitor connection-quality issues and investigate technical factors contributing to dropped telemedicine sessions.

---

# 5. Chronic Care Program Analysis

### Business Problem

HealthPlus needs to monitor chronic-care enrollment and active program status.

### SQL Analysis

* Count programs by condition
* Count active programs
* Analyze specialist involvement
* Compare program status
* Rank conditions based on enrollment

### Key Insight

**Hypertension** had **120 chronic-care programs**, including **79 active programs**.

### Business Recommendation

Monitor high-enrollment chronic conditions and ensure active programs receive appropriate follow-up and specialist support.

---

# 6. Health Package Adoption Analysis

### Business Problem

HealthPlus needs to understand which healthcare packages are being adopted by members.

### SQL Analysis

* Join `Health_Packages` with `Package_Subscriptions`
* Count subscriptions by package
* Compare package types
* Analyze active and expired subscriptions
* Rank packages based on subscription volume

### Key Insight

**PK002 – Full Body Checkup Premium v2** recorded the highest subscription volume with **92 subscriptions**.

### Business Recommendation

Monitor package adoption and subscription lifecycle to understand which packages are receiving higher member interest.

---

# 7. Corporate Healthcare Engagement

### Business Problem

HealthPlus needs to measure how effectively corporate healthcare programs are reaching employees.

### SQL Analysis

* Join `Corporates` and `Corporate_Members`
* Count enrolled members
* Calculate enrollment penetration
* Compare corporate participation
* Analyze corporate healthcare utilization

### Key Insight

**ZenIndustries Pvt Ltd** recorded approximately **9.52% enrollment penetration**, with 10 enrolled members out of 105 employees.

### Business Recommendation

Monitor corporate enrollment levels and identify opportunities to increase participation in corporate healthcare programs.

---

# 8. Prescription and Laboratory Analysis

### Business Problem

HealthPlus needs to understand medicine demand and laboratory service utilization.

### SQL Analysis

* Count prescriptions by medicine
* Identify frequently prescribed medicines
* Analyze specialist prescription workload
* Count laboratory tests
* Calculate laboratory costs
* Compare laboratory workload by clinic

### Key Insights

**Paracetamol 650mg** was the most frequently prescribed medicine with **554 prescriptions**.

**C001** recorded the highest laboratory workload with **515 tests**.

### Business Recommendation

Use prescription and laboratory demand patterns to support service planning and resource allocation.

---

# 9. Insurance Claim Analysis

### Business Problem

HealthPlus needs to monitor insurance claim volumes, amounts, and provider-level patterns.

### SQL Analysis

* Count claims
* Calculate total claim amount
* Compare insurance providers
* Analyze claim status
* Calculate average claim amount
* Rank insurance providers

### Key Insight

**Niva Bupa Health Insurance** recorded the highest total claim amount at approximately **2.52 million**, across **315 claims**.

### Business Recommendation

Monitor claim volume and financial exposure by insurance provider and review unusual claim patterns where required.

---

# 10. Billing and Payment Collection Analysis

### Business Problem

HealthPlus needs to understand the difference between billed amounts and successfully collected payments.

### SQL Analysis

* Calculate total billed amount
* Aggregate payments at bill level
* Analyze successful, failed, and refunded payments
* Compare billing and payment status
* Calculate collection gap

### Important Data Consideration

Billing and Payments have a **one-to-many relationship**, meaning a single bill can have multiple payment records.

Therefore, payment data should be aggregated by `bill_id` before joining with billing data to avoid duplicate financial totals.

### Key Insight

Total billed amount:

**18,690,854.89**

Successful collected amount:

**16,895,590.20**

Collection gap:

**1,795,264.69**

### Business Recommendation

Regularly reconcile billing and payment transactions at the bill level and monitor unpaid, partially paid, failed, and refunded transactions.

---

# 11. Patient Feedback and Service Quality

### Business Problem

HealthPlus needs to understand patient satisfaction across clinics and identify areas requiring service improvement.

### SQL Analysis

* Calculate average feedback rating
* Compare ratings across clinics
* Analyze feedback volume
* Identify consultations without feedback
* Rank clinics and specialists based on feedback metrics

### Key Insights

Among clinics with at least 50 feedback records, **C005 – HealthPlus Diagnostic Clinic - Pune** had an average rating of approximately **3.62**.

There were also **3,942 consultations without feedback**.

### Business Recommendation

Monitor patient feedback regularly and improve feedback collection to obtain better visibility into service quality.

---

# 12. Workforce and Clinic Capacity Analysis

### Business Problem

HealthPlus needs to understand whether workforce distribution is aligned with clinic consultation workload.

### SQL Analysis

* Count staff by clinic
* Analyze employment type and designation
* Count consultations by clinic
* Calculate consultations per staff member
* Rank clinics based on workload-to-staff ratio

### Key Insight

C001 recorded:

* **27 staff members**
* **945 consultations**
* Approximately **35 consultations per staff member**

### Business Recommendation

Compare workforce capacity with service demand to support staffing and resource-planning decisions.

---

# Key KPIs

| KPI                            | Business Purpose                                              |
| ------------------------------ | ------------------------------------------------------------- |
| Total Members                  | Measures registered member base                               |
| Total Consultations            | Measures healthcare service activity                          |
| Consultation Status Mix        | Understands consultation outcomes                             |
| Consultations per Member       | Measures member engagement                                    |
| Consultations per Specialist   | Measures specialist workload                                  |
| Telemedicine Sessions          | Measures digital healthcare usage                             |
| Average Telemedicine Duration  | Measures session duration                                     |
| Active Chronic Care Programs   | Measures chronic-care activity                                |
| Package Subscriptions          | Measures package adoption                                     |
| Active / Expired Subscriptions | Measures subscription lifecycle                               |
| Total Lab Tests                | Measures laboratory activity                                  |
| Total Lab Test Cost            | Measures laboratory expenditure                               |
| Total Claims                   | Measures insurance claim volume                               |
| Total Claim Amount             | Measures insurance financial exposure                         |
| Total Billed Amount            | Measures healthcare billing                                   |
| Successful Payment Amount      | Measures collected revenue                                    |
| Collection Gap                 | Measures difference between billing and successful collection |
| Average Feedback Rating        | Measures patient satisfaction                                 |
| Corporate Member Enrollment    | Measures corporate healthcare participation                   |
| Staff per Clinic               | Supports workforce planning                                   |

---

# SQL Techniques Used

The project demonstrates practical SQL techniques including:

* `SELECT`
* `DISTINCT`
* `WHERE`
* `GROUP BY`
* `HAVING`
* `ORDER BY`
* `LIMIT`
* `COUNT()`
* `COUNT(DISTINCT)`
* `SUM()`
* `AVG()`
* `MIN()`
* `MAX()`
* `CASE`
* `COALESCE()`
* `NULLIF()`
* `ROUND()`
* `CONCAT()`
* `LOWER()`
* `TRIM()`
* `INNER JOIN`
* `LEFT JOIN`
* Subqueries
* Common Table Expressions
* `STR_TO_DATE()`
* `TIMESTAMPDIFF()`
* `RANK()`
* `DENSE_RANK()`
* `ROW_NUMBER()`
* `LAG()`
* `LEAD()`
* `PARTITION BY`

---

# Window Function Analysis

Window functions were used to perform advanced business analysis without collapsing individual records.

### `RANK()`

Used to rank:

* Clinics by consultation workload
* Specialists by consultation workload
* Insurance providers by claim amount
* Packages by subscription volume

### `DENSE_RANK()`

Used where business analysis requires ranking without gaps between ranking values.

### `ROW_NUMBER()`

Used to identify the sequence of consultations or records within each member or business group.

### `LAG()`

Used to compare a member's current consultation with the previous consultation.

### `LEAD()`

Used to identify the next consultation or upcoming activity.

### `PARTITION BY`

Used to perform analysis separately for each member, specialist, clinic, or other business group.

---

# Data Preparation and Quality Checks

Before performing the business analysis, the database was reviewed for data quality and consistency.

The analysis includes:

* Checking table structures
* Reviewing relationships between tables
* Checking missing values
* Identifying inconsistent categorical values
* Removing unnecessary spaces using `TRIM()`
* Standardizing text values
* Converting date values where required
* Validating financial fields
* Handling null values
* Avoiding duplicate financial calculations
* Aggregating one-to-many relationships at the correct level

---

# Business Insights Summary

The analysis identified several important patterns:

### Clinic Utilization

C001 recorded the highest consultation volume with **945 consultations**.

### Specialist Workload

SP0004 – Charu Rao, ENT Specialist, recorded **391 consultations**.

### Member Engagement

**224 members** had no consultation activity.

### Telemedicine

There were **2,200 telemedicine sessions**, with **735 dropped sessions**.

### Connection Quality

Poor connection quality showed an observed drop rate of approximately **38.30%**.

### Chronic Care

Hypertension had **120 programs**, including **79 active programs**.

### Package Adoption

PK002 – Full Body Checkup Premium v2 recorded **92 subscriptions**.

### Corporate Engagement

ZenIndustries Pvt Ltd had approximately **9.52% enrollment penetration**.

### Prescription Activity

Paracetamol 650mg recorded **554 prescriptions**.

### Laboratory Activity

C001 recorded **515 laboratory tests**.

### Insurance Claims

Niva Bupa Health Insurance recorded approximately **2.52 million** in total claim amount.

### Financial Collection

The total billed amount was **18,690,854.89**, while successful collections were **16,895,590.20**, resulting in a collection gap of **1,795,264.69**.

### Patient Feedback

C005 recorded an average rating of approximately **3.62** among clinics with at least 50 feedback records.

### Missing Feedback

**3,942 consultations** had no feedback records.

---

# Recommendations

Based on the SQL analysis, HealthPlus should:

* Monitor clinics with consistently high consultation workloads.
* Review specialist workload concentration for better capacity planning.
* Identify members with low or no healthcare activity.
* Monitor telemedicine drop rates and connection-quality issues.
* Track active chronic-care programs and upcoming reviews.
* Monitor health package adoption and subscription expiry.
* Improve corporate healthcare program participation.
* Monitor frequently prescribed medicines and laboratory demand.
* Review insurance claim patterns by provider and claim status.
* Reconcile billing and payment transactions at the correct bill level.
* Monitor unpaid and partially paid bills.
* Improve patient feedback collection.
* Compare clinic workload with available staff capacity.
* Continue using SQL-based KPIs for regular healthcare performance monitoring.

---

# Project Outcome

This project demonstrates how healthcare data can be transformed into meaningful business insights using SQL.

The analysis connects multiple healthcare functions including:

**Members → Consultations → Specialists → Clinics → Telemedicine → Chronic Care → Packages → Corporate Programs → Prescriptions → Laboratory → Claims → Billing → Payments → Feedback → Staff**

The project demonstrates practical skills in:

* SQL database analysis
* Relational database analysis
* Data profiling
* Data cleaning
* Data validation
* Multi-table joins
* Aggregation
* Business KPI development
* Window functions
* Ranking analysis
* Member activity analysis
* Healthcare operational analysis
* Financial analysis
* Business insight generation
* Recommendation development

---

# Conclusion

The HealthPlus Healthcare Database Analysis provides a consolidated business view of healthcare operations, member engagement, service utilization, resource allocation, patient experience, and financial performance.

By applying SQL techniques such as **joins, aggregations, filtering, subqueries, CTEs, and window functions**, the project converts raw healthcare data into actionable business insights.

The analysis can support management in **workload planning, service monitoring, resource allocation, patient engagement, financial monitoring, and operational decision-making**.

---


