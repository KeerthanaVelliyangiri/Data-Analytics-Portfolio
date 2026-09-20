# MediCare Healthcare Database Analysis

## Business Problem

### How can MediCare gain a consolidated view of hospital operations, patient services, resource utilization and financial performance across multiple hospitals?

MediCare's healthcare database contains information about hospitals, departments, doctors, patients, appointments, admissions, treatments, laboratory services, pharmacy sales, billing, payments and insurance.

The business problem is that healthcare management needs a consolidated view of operational activity and financial performance across multiple hospitals. Without proper analysis, it becomes difficult to understand hospital workload, doctor utilization, patient service activity, room occupancy, treatment costs, laboratory workload, pharmacy revenue, billing status and payment performance.

The SQL analysis focuses on transforming the relational healthcare data into meaningful business insights that can support hospital operations, resource planning and financial monitoring.

### Business Objective

**Analyze hospital operations, patient service activity, resource utilization and financial transactions to support data-driven healthcare management decisions.**

### Solution

MediCare can use the analysis to:

1. **Analyze hospital activity**
   - Compare appointment and admission volumes across hospitals.
   - Identify hospitals with higher operational activity.
   - Support hospital-level resource planning.

2. **Monitor department and doctor workload**
   - Analyze admission workload by department.
   - Measure doctor appointment activity.
   - Rank doctors based on workload.
   - Support staffing and workload balancing.

3. **Understand patient service activity**
   - Analyze patient appointments and admissions.
   - Track healthcare activity across treatments, laboratory services and pharmacy.
   - Identify patients with repeated service utilization.

4. **Evaluate hospital resource utilization**
   - Analyze admission patterns and statuses.
   - Calculate average length of stay.
   - Monitor room occupancy across hospitals.
   - Support capacity planning.

5. **Analyze treatment and laboratory services**
   - Identify high-volume treatments.
   - Compare treatment costs.
   - Analyze laboratory test volume and cost.
   - Monitor laboratory completion and pending status.

6. **Monitor pharmacy and financial performance**
   - Analyze medicine quantities and pharmacy revenue.
   - Calculate total billed amounts.
   - Compare billing status.
   - Analyze payment status and payment transactions.

7. **Improve data quality**
   - Identify inconsistent categorical values.
   - Validate email and demographic fields.
   - Handle date fields stored as text.
   - Identify negative financial values requiring investigation.

---

## Dataset / Database Structure

The MediCare project uses a relational healthcare database named `medicaredb` containing **15 interconnected tables**.

### Main Tables

| Table | Purpose |
|---|---|
| `Hospitals` | Hospital details, location, type and bed capacity |
| `Departments` | Department information and hospital association |
| `Doctors` | Doctor details, specialization, experience and consultation fee |
| `Patients` | Patient demographic and registration information |
| `Appointments` | Patient appointment and doctor service records |
| `Admissions` | Patient admission, discharge and admission status |
| `Rooms` | Hospital room details, charges and room status |
| `Treatments` | Treatments provided to admitted patients |
| `Laboratory` | Laboratory tests, results, costs and status |
| `Medicines` | Medicine information, pricing and stock |
| `Pharmacy` | Medicine sales, quantities and revenue |
| `Employees` | Hospital employee and department information |
| `Insurance` | Insurance provider and coverage information |
| `Billing` | Patient billing and bill status |
| `Payments` | Payment transactions, modes and payment status |

### Database Relationships

The major healthcare process follows:

**Patient → Appointment → Admission → Treatment / Laboratory / Pharmacy → Billing → Payment**

The database also connects hospitals with departments, doctors, rooms, employees, appointments, admissions, laboratory services and pharmacy transactions.

---

## SQL Analysis

The SQL analysis focuses on the following business areas:

### Hospital Analysis

- Analyze appointment activity by hospital.
- Analyze admission activity by hospital.
- Identify hospitals with higher operational activity.
- Compare appointment and admission volumes.
- Support hospital-level resource planning.

### Department Analysis

- Analyze admission workload by department.
- Compare workload across departments.
- Identify departments with higher admission activity.
- Support department-level staffing decisions.

### Doctor Analysis

- Analyze doctor appointment workload.
- Compare appointment volumes across doctors.
- Rank doctors based on appointment activity.
- Identify doctors with higher service utilization.

### Patient Activity Analysis

- Analyze patient appointment activity.
- Analyze patient admission activity.
- Identify patients with repeated appointments.
- Identify patients without appointment activity.
- Examine patient service utilization across healthcare operations.

### Admission Analysis

- Analyze admission types such as Emergency, Planned and Referral.
- Analyze admission status.
- Calculate average length of stay.
- Convert text-based admission and discharge dates using `STR_TO_DATE()`.
- Support hospital capacity planning.

### Room Utilization Analysis

- Analyze occupied, vacant and maintenance rooms.
- Calculate room occupancy percentage.
- Compare room utilization across hospitals.
- Identify hospitals with higher room utilization.

### Treatment Analysis

- Analyze treatment volume.
- Compare treatment costs.
- Identify treatments with higher total cost.
- Analyze treatment status such as Completed, Ongoing and Cancelled.

### Laboratory Analysis

- Analyze laboratory test volume.
- Compare total laboratory test costs.
- Identify frequently performed tests.
- Analyze laboratory test status.

### Pharmacy Analysis

- Analyze medicine quantities sold.
- Calculate pharmacy revenue.
- Identify medicines with higher sales volume.
- Identify medicines generating higher revenue.

### Billing Analysis

- Calculate total billed amount.
- Analyze bill count by billing status.
- Compare Paid, Partially Paid and Unpaid bills.
- Identify financial records requiring further validation.

### Payment Analysis

- Analyze payment transactions.
- Compare successful, failed and refunded payments.
- Analyze payment amounts by status.
- Compare payment activity across payment modes.

---

## Tools & Technologies

The project was developed using **MySQL** and SQL-based analytical techniques.

### Technologies

- MySQL
- SQL
- Relational Database Management System

### SQL Techniques

- `SELECT`
- `DISTINCT`
- `WHERE`
- `GROUP BY`
- `HAVING`
- `ORDER BY`
- `LIMIT`
- Aggregate Functions
- `COUNT()`
- `SUM()`
- `AVG()`
- `MIN()`
- `MAX()`
- `INNER JOIN`
- `LEFT JOIN`
- Subqueries
- `STR_TO_DATE()`
- `DATEDIFF()`
- `ROUND()`
- `CONCAT()`
- `TRIM()`
- Window Functions
- `ROW_NUMBER()`
- `RANK()`
- `DENSE_RANK()`
- `LAG()`
- `LEAD()`
- `PARTITION BY`

---

## Data Profiling / Preparation

Before performing the business analysis, the healthcare database was examined to understand the structure, relationships and quality of the available data.

The analysis included:

- Reviewing all 15 table structures.
- Checking primary and foreign key relationships.
- Reviewing table row counts.
- Checking distinct values in categorical columns.
- Identifying inconsistent categorical values.
- Checking missing values.
- Validating email formats.
- Reviewing patient and doctor demographic fields.
- Checking department and hospital relationships.
- Converting text-based dates for analysis.
- Identifying negative billing and payment values.
- Validating treatment and financial records before aggregation.

### Data Quality Findings

Some data-quality issues were identified during profiling:

- Appointment status contains different case variations such as `Completed`, `completed`, `COMPLETED`.
- Patient gender contains values such as `Male`, `MALE`, `M`, `m`, `Female`, `F`, `f` and `FEMALE`.
- Doctor gender also contains inconsistent representations.
- Patient and doctor email fields contain malformed and missing values.
- Some doctors have missing department assignments.
- Some admissions have missing department information.
- Some departments have no assigned head doctor.
- Several date fields are stored as text and require date conversion.
- Negative billing and payment records require further business validation.
- Some treatment records contain negative treatment costs.

These issues should be considered before using financial values for final management reporting.

---

## Key Metrics / Analysis Areas

The project evaluates several important healthcare metrics:

### Hospital Activity

Measures appointment and admission activity across hospitals.

**Key finding:**

- MediCare Belagavi North Campus recorded the highest appointment activity with **493 appointments**.
- The same hospital recorded **244 admissions**.
- Combined appointment and admission activity was **737**.

### Doctor Workload

Measures appointment activity to understand doctor workload.

**Key finding:**

- **Ramya Shetty (DR0008)** recorded the highest appointment activity with **409 appointments**.
- This represents approximately **8.02%** of all 5,100 appointment records.

### Patient Activity

Measures patient utilization of healthcare services.

**Key finding:**

- **185 patients** had no appointment activity.
- **257 patients** had at least 5 appointments.
- The highest appointment count for a single patient was **10 appointments**.

### Department Workload

Measures admissions handled by departments.

**Key finding:**

- **Ophthalmology (D006)** recorded the highest admission workload with **240 admissions**.

### Admission Pattern

Measures the type of patient admissions.

| Admission Type | Admissions | Percentage |
|---|---:|---:|
| Emergency | 1,165 | 46.60% |
| Planned | 981 | 39.24% |
| Referral | 354 | 14.16% |

Emergency admissions represent the largest share of admissions.

### Admission Status

| Admission Status | Admissions | Percentage |
|---|---:|---:|
| Discharged | 1,869 | 74.76% |
| Admitted | 371 | 14.84% |
| Under Observation | 260 | 10.40% |

### Average Length of Stay

The average length of stay for valid admission and discharge date records is approximately:

**7.44 days**

The calculation uses `STR_TO_DATE()` and `DATEDIFF()` because the date fields are stored as text.

### Room Utilization

The database contains:

- 426 occupied rooms
- 345 vacant rooms
- 29 rooms under maintenance

Overall observed room occupancy is approximately **53.25%**.

### Treatment Analysis

Treatment records show:

- 2,668 Completed
- 500 Ongoing
- 332 Cancelled

The highest treatment count was recorded for **Appendicitis Management** with **213 records**.

### Laboratory Analysis

The database contains **3,000 laboratory test records**.

The highest-volume test was:

**Ultrasound Abdomen – 204 tests**

### Pharmacy Analysis

Total pharmacy revenue in the dataset is approximately:

**₹1.93 crore**

The medicine with the highest revenue was:

**Atorvastatin 650mg – approximately ₹46.99 lakh**

### Billing Analysis

Total billed amount in the dataset is approximately:

**₹6.97 crore**

Billing status:

| Bill Status | Bills | Percentage |
|---|---:|---:|
| Paid | 3,267 | 65.34% |
| Partially Paid | 996 | 19.92% |
| Unpaid | 737 | 14.74% |

### Payment Analysis

Payment status:

| Payment Status | Transactions | Percentage |
|---|---:|---:|
| Success | 4,413 | 88.26% |
| Failed | 390 | 7.80% |
| Refunded | 197 | 3.94% |

Payment and billing records require careful reconciliation because multiple payment records can exist for the same bill.

---

## Key Insights

Based on the SQL analysis:

### 1. Hospital activity varies across locations

Appointment and admission volumes are not evenly distributed across hospitals. MediCare Belagavi North Campus recorded the highest appointment and admission activity in the analyzed dataset.

### 2. Doctor workload is concentrated

Doctor appointment volumes vary significantly. Ramya Shetty recorded 409 appointments, making doctor-level workload analysis useful for staffing and workload planning.

### 3. Ophthalmology has high admission workload

Ophthalmology recorded the highest department admission workload with 240 admissions. This indicates a higher level of admission activity within the analyzed data.

### 4. Emergency admissions represent a major workload

Emergency admissions account for 46.60% of the admission records, followed by planned admissions at 39.24%.

### 5. Patient utilization varies

Some patients have repeated appointment activity, while 185 patients have no appointment records. Patient-level analysis can therefore help understand service utilization patterns.

### 6. Hospital room utilization is moderate overall

Overall room occupancy is approximately 53.25%, while utilization differs between hospitals. This can support hospital capacity and room allocation analysis.

### 7. Treatment activity contributes significant operational cost

Treatment analysis shows differences in both treatment volume and total treatment cost. High-cost treatment categories require appropriate monitoring.

### 8. Laboratory services have measurable workload and cost

The database contains 3,000 laboratory records, allowing management to monitor test demand, cost and completion status.

### 9. Pharmacy contributes significant revenue

Pharmacy transactions generate approximately ₹1.93 crore in the analyzed dataset. Medicine-level revenue analysis helps identify major revenue-generating medicines.

### 10. Billing and payment data require reconciliation

Billing contains Paid, Partially Paid and Unpaid records, while payments contain Success, Failed and Refunded transactions.

Because multiple payment records may belong to the same bill, billing and payment analysis should be performed at the correct transaction level to avoid duplicate counting.

### 11. Data quality affects business reporting

Inconsistent categorical values, malformed emails, missing relationships, text-based dates and negative financial records can affect analysis if they are not validated before reporting.

---

## Recommendations / Conclusion

### Recommendations

Based on the analysis, MediCare should:

- Monitor hospitals with high appointment and admission activity.
- Review doctor workload to support balanced staffing.
- Monitor departments with high admission volumes.
- Use admission patterns to support emergency and planned-care resource planning.
- Monitor room occupancy across hospitals for better capacity utilization.
- Track average length of stay to support bed and resource planning.
- Monitor high-volume and high-cost treatments.
- Track laboratory workload and test costs.
- Monitor pharmacy revenue and high-performing medicines.
- Review unpaid and partially paid bills regularly.
- Reconcile billing and payment transactions at the correct bill level.
- Investigate negative billing, payment and treatment-cost records.
- Standardize categorical values before creating management reports.
- Improve data validation for emails, demographic fields and relationships.
- Continue using SQL-based KPIs for regular healthcare operational monitoring.

### Conclusion

The MediCare SQL analysis provides a consolidated view of healthcare operations across hospitals, departments, doctors, patients and financial services.

The analysis covers **hospital activity, doctor workload, patient activity, admissions, room utilization, treatments, laboratory services, pharmacy revenue, billing and payments**.

The project demonstrates how relational healthcare data can be transformed into meaningful business insights using SQL and can support **data-driven operational planning, resource utilization and financial monitoring**.

---

## Project Outcome

This project demonstrates practical skills in:

- SQL database analysis
- Relational database design
- Healthcare data analysis
- Data profiling
- Data validation
- Data cleaning
- Multi-table joins
- Aggregation
- Grouping and filtering
- Subqueries
- Window functions
- Ranking analysis
- Time-based analysis
- Financial analysis
- KPI development
- Business insight generation
- Data-driven recommendations

The final output is a SQL-based **MediCare Healthcare Database Analysis** designed to convert healthcare operational and financial data into meaningful insights for hospital management and resource planning.
