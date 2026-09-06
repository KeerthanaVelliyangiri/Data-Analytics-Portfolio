# MediCare Healthcare Database Analysis

## Business Problem

### How effectively is MediCare managing hospital operations, patient activity, healthcare services, and revenue collection across its hospital network?

MediCare's healthcare database contains information about hospitals, departments, doctors, patients, appointments, admissions, rooms, treatments, laboratory services, pharmacy transactions, employees, insurance, billing, and payments.

The SQL analysis focuses on understanding hospital and doctor workload, patient healthcare activity, admission patterns, room utilization, treatment and laboratory costs, pharmacy revenue, billing performance, and payment collection.

The analysis also identifies data-quality issues such as inconsistent gender values, invalid email formats, missing department relationships, and different date formats.

### Business Objective

**Analyze MediCare's healthcare operations and financial transactions to identify workload, resource utilization, service activity, billing, and payment collection patterns.**

### Solution

MediCare can use the SQL analysis to:

1. **Monitor hospital activity**

   * Compare appointments and admissions across hospitals.
   * Identify hospitals with higher operational activity.
   * Support hospital-level resource planning.

2. **Analyze doctor workload**

   * Count appointments handled by each doctor.
   * Rank doctors based on appointment activity.
   * Understand workload distribution across doctors.

3. **Evaluate department workload**

   * Analyze admission activity by department.
   * Compare workload across departments.
   * Identify departments requiring closer operational monitoring.

4. **Understand patient activity**

   * Identify patients with higher appointment and admission activity.
   * Understand patient-level healthcare service usage.

5. **Monitor admissions and hospital stay**

   * Analyze admission types and admission statuses.
   * Calculate average length of stay using valid admission and discharge dates.
   * Identify hospitals and departments with higher admission activity.

6. **Monitor room utilization**

   * Compare occupied and vacant rooms.
   * Analyze room availability across hospitals.
   * Support hospital capacity planning.

7. **Analyze healthcare services**

   * Identify treatments with higher activity and cost.
   * Analyze laboratory test volume and cost.
   * Identify medicines generating higher pharmacy revenue.

8. **Monitor billing and payments**

   * Calculate total billed amount.
   * Analyze billing status.
   * Compare payment status and payment amounts.
   * Identify potential gaps between billed and collected amounts.

9. **Improve data quality**

   * Standardize inconsistent gender values.
   * Investigate invalid email formats.

---

## Dataset / Database Structure

The MediCare project uses a relational MySQL database containing interconnected healthcare and financial entities.

### Main Tables

| Table          | Purpose                                                         |
| -------------- | --------------------------------------------------------------- |
| `hospitals`    | Hospital information, location, type and bed capacity           |
| `departments`  | Department information and hospital association                 |
| `doctors`      | Doctor details, specialization, experience and consultation fee |
| `patients`     | Patient demographic and registration information                |
| `appointments` | Patient-doctor appointment activity                             |
| `admissions`   | Patient inpatient admission and discharge information           |
| `rooms`        | Hospital room information and room status                       |
| `treatments`   | Treatment activity and treatment cost                           |
| `laboratory`   | Laboratory tests, status and test cost                          |
| `medicines`    | Medicine information, category, price and stock                 |
| `pharmacy`     | Pharmacy transactions, quantity and revenue                     |
| `employees`    | Hospital employee and workforce information                     |
| `insurance`    | Patient insurance and coverage information                      |
| `billing`      | Patient bills, charge components and total billed amount        |
| `payments`     | Payment transactions, payment status and payment mode           |

The main analytical flow is:

**Patient → Appointment → Admission → Treatment / Laboratory / Pharmacy → Billing → Payment**

The SQL database implements relationships between these healthcare entities using primary and foreign keys.

---

## SQL Analysis

The SQL analysis focuses on the following business areas:

### Hospital Analysis

* Count total hospitals.
* Analyze hospital-level information.
* Compare hospital appointment activity.
* Compare hospital admission activity.
* Identify hospitals with higher operational activity.
* Analyze hospital capacity and room availability.

### Doctor Analysis

* Count doctors.
* Analyze doctors by specialization.
* Analyze doctor experience.
* Compare doctors across hospitals and departments.
* Calculate appointment workload for each doctor.
* Rank doctors based on appointment activity.

The project uses `RANK()` to identify doctor workload rankings.

### Department Analysis

* Count and analyze departments.
* Compare departments across hospitals.
* Analyze department admission workload.
* Identify departments with higher admission activity.
* Review departments with missing head-doctor information.

### Patient Analysis

* Count total patients.
* Analyze patient appointment activity.
* Analyze patient admission activity.
* Identify patients with higher healthcare activity.
* Compare patient-level appointments and admissions.

The SQL analysis uses `COUNT(DISTINCT ...)` when combining appointment and admission activity to avoid incorrectly multiplying records.

### Appointment Analysis

* Count total appointments.
* Analyze appointments by doctor.
* Identify doctors with higher appointment workload.
* Compare appointment activity across hospitals.
* Use appointment activity as an operational workload indicator.

### Admission Analysis

* Count total admissions.
* Compare admissions across hospitals.
* Analyze admission status.
* Analyze admission types.
* Calculate average length of stay where valid dates are available.
* Use `LEAD()` to identify the next admission for a patient.

The project specifically includes hospital admission ranking, admission-status analysis, and next-admission analysis.

### Room Analysis

* Count rooms by hospital.
* Identify occupied rooms.
* Identify vacant/available rooms.
* Compare room utilization across hospitals.

The SQL analysis directly compares total, occupied, and available rooms by hospital.

### Treatment Analysis

* Count treatment activity.
* Calculate treatment cost.
* Identify treatments with higher total cost.
* Compare treatment volume and cost.

The project identifies the highest-cost treatments using `COUNT()` and `SUM()` with grouping and sorting.

### Laboratory Analysis

* Count laboratory tests.
* Calculate total laboratory cost.
* Compare test volume.
* Identify laboratory tests with higher activity and cost.
* Analyze laboratory service status where applicable.

The SQL includes test-level count and cost analysis.

### Pharmacy Analysis

* Analyze medicine-level transactions.
* Calculate quantity sold.
* Calculate pharmacy revenue.
* Identify medicines generating higher revenue.
* Compare medicine activity using pharmacy transactions.

The SQL calculates medicine quantity sold and total pharmacy revenue.

### Billing Analysis

* Calculate total billed revenue.
* Analyze billing status.
* Compare billed amounts by bill status.
* Analyze room, doctor, medicine, laboratory and other charge components.

The `billing` table stores these individual charge components together with `total_amount` and `bill_status`.

### Payment Analysis

* Analyze payment transactions.
* Compare payment status.
* Analyze payment amount.
* Analyze payment methods.
* Compare payments over time.
* Use `LAG()` to compare a payment with the previous payment.

The SQL uses `LAG(payment_amount)` ordered by payment date for payment comparison.

### KPI Analysis

The project includes SQL-based KPIs such as:

* Total Patients
* Total Appointments
* Total Admissions
* Total Treatments
* Total Laboratory Activity
* Total Pharmacy Activity
* Total Billed Amount
* Total Payment Collected
* Collection Gap
* Collection Rate
* Hospital Activity
* Department Workload
* Doctor Workload
* Room Utilization

The project requirements define collection gap as the difference between billed amount and collected payment, with careful aggregation required to avoid duplicate counting.

---

## Tools & Technologies

The project was developed using **MySQL and SQL**.

### Technologies

* MySQL
* SQL
* Relational Database Management System

### SQL Techniques

* `CREATE DATABASE`
* `CREATE TABLE`
* `ALTER TABLE`
* `PRIMARY KEY`
* `FOREIGN KEY`
* `INSERT`
* `UPDATE`
* `SELECT`
* `DISTINCT`
* `WHERE`
* `ORDER BY`
* `LIMIT`
* `GROUP BY`
* `HAVING`
* Aggregate Functions
* `COUNT()`
* `SUM()`
* `AVG()`
* `MIN()`
* `MAX()`
* `INNER JOIN`
* `LEFT JOIN`
* Subqueries
* `CASE`
* `REGEXP`
* `ROW_NUMBER()`
* `RANK()`
* `LAG()`
* `LEAD()`

The project scope specifically includes aggregation, joins, and meaningful window-function analysis.

---

## Data Profiling / Preparation

Before performing the final analysis, the SQL project includes data profiling and cleaning activities.

The analysis checks:

* Distinct gender values.
* Gender frequency.
* Doctors with missing department IDs.
* Doctors with missing email addresses.
* Invalid email formats.
* Departments without head doctors.
* Inconsistent date formats.
* Missing values.
* Data consistency across related tables.

For example, the SQL identifies inconsistent gender values and invalid email formats using `DISTINCT`, `GROUP BY`, `IS NULL`, and `REGEXP`.

The project also standardizes gender values such as `Male`, `MALE`, `m`, `Female`, and `FEMALE` using `TRIM()`, `LOWER()`, and `CASE`.

Email-format issues are also investigated and cleaned using conditional logic.

---

## Key Metrics / Analysis Areas

The project evaluates the following healthcare and financial metrics:

### Hospital Activity

Measures hospital-level appointments and admissions to understand operational activity.

### Doctor Workload

Measures appointment activity per doctor and ranks doctors based on workload.

### Department Workload

Measures admission activity by department to identify differences in operational workload.

### Patient Activity

Measures patient appointments and admissions to understand healthcare service usage.

### Admission Pattern

Analyzes admission type and admission status.

### Average Length of Stay

Measures the average number of days between admission and discharge where valid dates are available.

### Room Utilization

Compares occupied and vacant rooms to understand room availability.

### Treatment Activity and Cost

Measures treatment volume and total treatment cost.

### Laboratory Activity and Cost

Measures laboratory test volume and associated cost.

### Pharmacy Revenue

Measures medicine quantity sold and pharmacy revenue.

### Total Billed Amount

Measures the total amount recorded in the billing table.

### Payment Collection

Measures payment amount and payment status.

### Collection Gap

Compares billed amounts with collected payments using the correct billing/payment level.

### Doctor Ranking

Uses `RANK()` to compare doctors based on appointment workload.

### Payment Trend Comparison

Uses `LAG()` to compare a payment with the previous payment.

### Patient Admission Sequence

Uses `LEAD()` to identify the next admission for each patient.

---

## Key Insights

Based on the SQL analysis performed in the project:

### 1. Doctor workload can be compared using appointment activity

The project calculates appointment counts for individual doctors and ranks them, providing a measurable view of doctor workload.

### 2. Patient healthcare activity differs across patients

The analysis combines appointment and admission activity at the patient level to identify patients with higher healthcare activity.

### 3. Hospital admission activity can be compared

The project ranks hospitals according to the number of admissions, helping management understand differences in inpatient activity.

### 4. Admission patterns can be monitored

Admission status and admission sequence analysis help understand how inpatient activity is distributed and whether patients have subsequent admissions.

### 5. Room availability can support capacity planning

Comparing occupied and vacant rooms provides a basic operational view of room utilization across hospitals.

### 6. Treatment costs vary across treatment types

Treatment-level aggregation allows MediCare to identify treatments with higher total cost and activity.

### 7. Laboratory services contribute measurable activity and cost

The analysis compares laboratory tests based on test count and total cost, helping identify higher-volume and higher-cost laboratory services.

### 8. Pharmacy transactions provide a revenue view

Medicine-level analysis identifies quantity sold and pharmacy revenue, supporting pharmacy activity monitoring.

### 9. Billing and payment should be analyzed separately

Billing represents the amount charged, while payment records represent collection activity. Therefore, both should be analyzed separately before calculating collection performance.

### 10. Data quality can affect analytical accuracy

The SQL identifies inconsistent gender values, invalid email formats, missing department relationships, and other data-quality issues. These should be investigated before using the affected fields for final reporting.

---

## Recommendations / Conclusion

### Recommendations

Based on the analysis performed in this project, MediCare should:

1. **Monitor doctor workload**

   * Regularly review appointment volume by doctor.
   * Identify consistently high-workload doctors.
   * Consider workload balancing when assigning appointments and resources.

2. **Review department workload**

   * Monitor departments with higher admission activity.
   * Compare workload across departments and hospitals.
   * Use this information for operational resource planning.

3. **Improve hospital capacity planning**

   * Compare hospital admissions with available bed capacity.
   * Monitor occupied and vacant rooms.
   * Review hospitals where resource utilization requires attention.

4. **Monitor patient activity**

   * Identify patients with repeated appointments or admissions.
   * Use patient activity information to understand service demand patterns.

5. **Monitor admission and length of stay**

   * Track admission types and statuses.
   * Monitor average length of stay using valid admission and discharge dates.
   * Investigate unusually long stays from an operational planning perspective.

6. **Review high-cost treatments**

   * Monitor treatments with higher total costs.
   * Compare treatment volume with treatment cost.
   * Investigate unusual financial values before using them in final financial reporting.

7. **Monitor laboratory services**

   * Identify high-volume and high-cost laboratory tests.
   * Review laboratory activity and cost together for better service planning.

8. **Improve pharmacy planning**

   * Monitor medicines with high sales quantity and revenue.
   * Compare pharmacy demand with medicine stock quantity.
   * Use this information to support inventory planning.

9. **Strengthen billing and collection monitoring**

   * Monitor total billed amount and payment collection separately.
   * Track paid, unpaid, and partially paid bills.
   * Calculate collection gaps carefully.

### Conclusion

The MediCare SQL project provides a relational and analytical view of healthcare operations, patient activity, hospital resources, healthcare services, billing, and payment collection.

The analysis helps MediCare understand **doctor workload, department workload, hospital admissions, room utilization, treatment costs, laboratory activity, pharmacy revenue, billing status, and payment activity**.

By combining data-quality validation with SQL-based operational and financial analysis, MediCare can use its healthcare data to support **better resource planning, workload monitoring, service management, and financial collection monitoring**.

---

## Project Outcome

This project demonstrates practical skills in:

* SQL database design
* Relational database concepts
* Healthcare data analysis
* Primary and foreign keys
* Data profiling
* Data cleaning and validation
* Data aggregation
* Multi-table joins
* Filtering and sorting
* Subqueries
* KPI analysis
* Hospital operational analysis
* Patient activity analysis
* Doctor workload analysis
* Admission analysis
* Room utilization analysis
* Treatment cost analysis
* Laboratory analysis
* Pharmacy revenue analysis
* Billing analysis
* Payment analysis
* Window functions
* Ranking analysis
* Business insight generation
* Data-driven recommendations

The final output is a SQL-based **MediCare Healthcare Database Analysis** designed to convert relational healthcare data into meaningful operational and financial insights and support better healthcare resource and collection planning.
