# MediCare Healthcare Database Analysis

## Project Overview

The MediCare Healthcare Database Analysis is a SQL project developed using MySQL to manage and analyze healthcare operations. The database contains information about hospitals, departments, doctors, patients, and appointments. This project demonstrates how SQL can be used to generate business insights for healthcare resource planning and hospital management.

Medicare_README.md

## Business Problem

Healthcare organizations often struggle to balance doctor availability, hospital capacity, and patient demand. Without proper analysis, it is difficult to identify high-demand specializations, optimize staffing, and efficiently utilize hospital resources.

Medicare_README.md

## Business Objective

The objective of this project is to:

* Analyze hospital and doctor distribution

* Identify high-demand medical specializations

* Evaluate hospital staffing and bed capacity

* Compare consultation fees across doctors

* Support data-driven healthcare resource planning

  Medicare_README.md

## Database Structure

This project uses a relational database named `medicaredb` with five main tables connected through primary and foreign keys.

medicare_Final.sql

|
Table

|

Description

|
| --- | --- |
|

Hospitals

|

Hospital details, city, state, region, bed capacity

|
|

Departments

|

Department information for each hospital

|
|

Doctors

|

Doctor profile, specialization, experience, consultation fee

|
|

Patients

|

Patient demographic information

|
|

Appointments

|

Appointment records between doctors and patients

|

## Tools & Technologies

* Database: MySQL

* Language: SQL

* Concepts: Relational Database, Joins, Aggregation, Window Functions

  Medicare_README.md

## SQL Techniques Used

* SELECT, DISTINCT, WHERE

* GROUP BY, HAVING, ORDER BY

* COUNT(), SUM(), AVG(), MIN(), MAX()

* INNER JOIN & LEFT JOIN

* Subqueries

* ROW_NUMBER(), RANK()

* LAG() & LEAD()

  Medicare_README.md

## Analysis Performed

### Hospital Analysis

* Total hospitals and regional distribution

* Hospital bed capacity comparison

* Doctor availability across hospitals

### Doctor Analysis

* Doctors by specialization

* Experienced doctors (10+ years)

* Doctor count by hospital

* Consultation fee ranking

### Department Analysis

* Department distribution across hospitals

* Department availability

### Appointment Analysis

* Appointment volume by doctor

* Hospital workload analysis

### Consultation Fee Analysis

* Average consultation fee by specialization

* Fee comparison across doctors

  Medicare_README.md

## Key Insights

* Doctor availability differs across medical specializations.

* Hospital staffing is not evenly distributed.

* Experienced doctors are an important healthcare resource.

* Consultation fees vary by specialization and doctor.

* Appointment activity helps measure doctor workload.

  Medicare_README.md

## Recommendations

* Increase staffing in high-demand specializations.

* Balance doctor allocation between hospitals.

* Use bed capacity and appointment trends for resource planning.

* Monitor consultation fee patterns for pricing consistency.

* Utilize experienced doctors for mentoring and specialized care.

  Medicare_README.md

## Project Outcome

This project demonstrates practical SQL skills including relational database design, multi-table joins, aggregation, subqueries, window functions, and business insight generation. The final database supports data-driven decision-making for healthcare workforce and hospital capacity planning.

Medicare_README.md

## Project Files

* medicare_Final.sql – Complete database schema, data insertion, and SQL analysis queries.

* Medicare_README.md – Project documentation and business explanation.

