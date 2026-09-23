#Which hospitals have the highest operational activity
SELECT h.hospital_id,h.hospital_name,COUNT(a.appointment_id) AS total_appointments,COUNT(ad.admission_id) AS total_admissions
FROM hospitals h
LEFT JOIN appointments a
ON h.hospital_id = a.hospital_id
LEFT JOIN admissions ad
ON h.hospital_id = ad.hospital_id
GROUP BY h.hospital_id, h.hospital_name
order by total_appointments desc;

#Which departments have the highest workload
SELECT d.department_id,h.hospital_name,d.department_name,COUNT(DISTINCT a.appointment_id) AS total_appointments,COUNT(DISTINCT ad.admission_id) AS total_admissions
FROM departments d
LEFT JOIN appointments a
ON d.hospital_id = a.hospital_id
LEFT JOIN admissions ad
ON d.department_id = ad.department_id
LEFT JOIN hospitals h
ON d.hospital_id = h.hospital_id
GROUP BY d.department_id,d.department_name;


#Which doctors have the highest workload
SELECT d.doctor_id,d.first_name,h.hospital_name,COUNT(a.appointment_id) AS total_appointments
FROM doctors d
LEFT JOIN appointments a
ON d.doctor_id = a.doctor_id
LEFT JOIN hospitals h
ON d.hospital_id = h.hospital_id
GROUP BY d.doctor_id,d.first_name
order by total_appointments desc;
 

SELECT d.doctor_id,d.first_name, h.hospital_name,COUNT(a.appointment_id) AS total_appointments,RANK() OVER (ORDER BY COUNT(a.appointment_id) DESC) AS doctor_rank
FROM doctors d
LEFT JOIN appointments a
ON d.doctor_id = a.doctor_id
LEFT JOIN hospitals h
ON d.hospital_id = h.hospital_id 
GROUP BY d.doctor_id,d.first_name;

# Which patients have the highest healthcare activity
SELECT p.patient_id,p.first_name,h.hospital_name,h.city,COUNT(DISTINCT a.appointment_id) AS total_appointments,COUNT(DISTINCT ad.admission_id) AS total_admissions
FROM patients p
LEFT JOIN appointments a
ON p.patient_id = a.patient_id
LEFT JOIN admissions ad
ON p.patient_id = ad.patient_id
LEFT JOIN hospitals h
ON a.hospital_id = h.hospital_id
GROUP BY p.patient_id,p.first_name,h.hospital_name,h.city;
 
# Which hospitals have the highest number of admissions?
SELECT h.hospital_name,COUNT(DISTINCT ad.admission_id) AS total_admissions
FROM hospitals h
JOIN admissions ad
ON h.hospital_id = ad.hospital_id
GROUP BY h.hospital_id, h.hospital_name
ORDER BY total_admissions DESC
LIMIT 5;

# What are the admission patterns?
SELECT admission_status,COUNT(*) AS total_admissions
FROM admissions
GROUP BY admission_status;


# Find the next admission for each patient
SELECT patient_id,admission_id,admission_date,LEAD(admission_date) OVER (PARTITION BY patient_id ORDER BY admission_date) AS next_admission
FROM admissions
ORDER BY patient_id, admission_date;

# Are rooms being utilized effectively
SELECT h.hospital_id,h.hospital_name,COUNT(*) AS total_rooms,SUM(r.room_status = 'Occupied') AS occupied_rooms,SUM(r.room_status = 'Vacant') AS available_rooms
FROM rooms r
LEFT JOIN hospitals h
ON h.hospital_id = r.hospital_id
GROUP BY hospital_id;

# Which treatments have the highest cost
SELECT treatment_name,COUNT(*) AS treatment_count,SUM(treatment_cost) AS total_cost
FROM treatments
GROUP BY treatment_name
ORDER BY total_cost DESC
LIMIT 10;

# Which laboratory tests have the highest count and cost
SELECT test_name,COUNT(*) AS test_count,SUM(test_cost) AS total_test_cost
FROM laboratory 
GROUP BY test_name
order by total_test_cost desc;

# Which medicines generate the highest pharmacy revenue
SELECT m.medicine_name,SUM(p.quantity) AS quantity_sold,SUM(p.total_price) AS total_revenue
FROM medicines m
JOIN pharmacy p
ON m.medicine_id = p.medicine_id
GROUP BY m.medicine_name
ORDER BY total_revenue DESC;

# MediCare total billed revenue
SELECT SUM(total_amount) AS total_billed_revenue
FROM billing;

# Bill Status revenue
SELECT bill_status,COUNT(*) AS bill_count,SUM(total_amount) AS billed_amount
FROM billing
GROUP BY bill_status;

# Which payment methods perform best
SELECT payment_status,COUNT(payment_id) AS transaction_count,SUM(payment_amount) AS payment_amount
FROM payments
GROUP BY payment_status;

# Compare payment with previous payment
SELECT payment_id,patient_id,payment_date,payment_amount,LAG(payment_amount) OVER(ORDER BY payment_date) AS previous_payment
FROM payments  
ORDER BY payment_date;
