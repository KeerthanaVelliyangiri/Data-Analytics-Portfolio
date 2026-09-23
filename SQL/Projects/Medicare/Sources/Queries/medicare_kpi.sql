# KPI---------------------------------------------

# Total Patients
SELECT COUNT(*) AS total_patients
FROM patients;

# Total Appointments
SELECT COUNT(appointment_id) AS total_appointments
FROM appointments;

# Total Admissions
SELECT COUNT(admission_id) AS total_admissions
FROM admissions;

# Total Treatments
SELECT COUNT(treatment_id) AS total_treatments
FROM treatments;

# Total Treatment Cost
SELECT SUM(treatment_cost) AS total_treatment_cost
FROM treatments;

# Total Lab Activity
SELECT COUNT(lab_test_id) AS total_lab_activity
FROM laboratory;

# Total Lab Cost
SELECT SUM(test_cost) AS total_lab_cost
FROM laboratory;

# Total Pharmacy Activity
SELECT COUNT(pharmacy_sale_id) AS total_pharmacy_activity
FROM pharmacy;

# Pharmacy Revenue
SELECT SUM(total_price) AS pharmacy_revenue
FROM pharmacy;

# Total Billed Amount
SELECT SUM(total_amount) AS total_billed_amount
FROM billing;

# Total Payment Collected
SELECT SUM(payment_amount) AS total_payment_collected
FROM payments;
