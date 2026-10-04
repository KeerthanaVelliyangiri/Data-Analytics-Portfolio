# BUSINESS ANALYSIS

use healthplus;

# 1.which clinics have the highest consultation workload
SELECT c.clinic_id,c.clinic_name,c.clinic_type,COUNT(co.consultation_id) AS consultation_count
FROM Clinics c
LEFT JOIN Consultations co
ON c.clinic_id = co.clinic_id
GROUP BY c.clinic_id
ORDER BY consultation_count DESC;

# 2.Specialist Workload
SELECT s.specialist_id,s.first_name,s.specialization,COUNT(c.consultation_id) AS consultation_count
FROM Specialists s
LEFT JOIN Consultations c
ON s.specialist_id = c.specialist_id
GROUP BY s.specialist_id
ORDER BY consultation_count DESC;

# 3.Member Engagement and Repeat Visits
SELECT m.member_id,m.first_name,m.membership_type,COUNT(c.consultation_id) AS consultation_count
FROM Members m
LEFT JOIN Consultations c
ON m.member_id = c.member_id
GROUP BY m.member_id
ORDER BY consultation_count DESC;

# 4. Telemedicine sessions by status
SELECT session_status,COUNT(*) AS session_count
FROM Telemedicine_Sessions
GROUP BY session_status
ORDER BY session_count DESC;

# 5. Telemedicine - Condition and program-status distribution
SELECT condition_name,program_status,COUNT(*) AS program_count
FROM Chronic_Care_Programs
GROUP BY condition_name, program_status
ORDER BY program_count DESC;

 # 6.Specialist chronic-care workload
SELECT s.specialist_id,CONCAT(s.first_name, ' ', s.last_name) AS specialist_name,s.specialization,COUNT(cc.program_id) AS chronic_program_count
FROM Specialists s
INNER JOIN Chronic_Care_Programs cc
ON s.specialist_id = cc.specialist_id
GROUP BY s.specialist_id,s.first_name,s.last_name,s.specialization
HAVING COUNT(cc.program_id) >= 5
ORDER BY chronic_program_count DESC;

# 7. Health Package-level subscription volume
SELECT hp.package_id,hp.package_name,hp.package_type,hp.price,hp.validity_days,COUNT(ps.subscription_id) AS subscription_count
FROM Health_Packages hp
LEFT JOIN Package_Subscriptions ps
ON hp.package_id = ps.package_id
GROUP BY hp.package_id,hp.package_name,hp.package_type,hp.price,hp.validity_days
ORDER BY subscription_count DESC;

# 8. Corporate enrollment and penetration
SELECT co.corporate_id,co.company_name,co.industry,co.employee_count,COUNT(cm.corporate_member_id) AS enrolled_members
FROM Corporates co
LEFT JOIN Corporate_Members cm
ON co.corporate_id = cm.corporate_id
GROUP BY co.corporate_id,co.company_name,co.industry,co.employee_count
ORDER BY enrolled_members DESC;

# 9. Most frequently prescribed medicines
SELECT medicine_name,COUNT(*) AS prescription_count
FROM Prescriptions
GROUP BY medicine_name
HAVING COUNT(*) >= 50
ORDER BY prescription_count DESC;

# 10. Diagnostic cost by test type
SELECT test_name,COUNT(*) AS test_count,SUM(test_cost) AS total_test_cost
FROM Lab_Tests
GROUP BY test_name
ORDER BY total_test_cost DESC;

# 11. Insurance Claim status distribution
SELECT claim_status,COUNT(*) AS claim_count,SUM(claim_amount) AS total_claim_amount
FROM Claims
GROUP BY claim_status
ORDER BY claim_count DESC;

# 12. Clinic satisfaction
SELECT cl.clinic_id,cl.clinic_name,COUNT(f.feedback_id) AS feedback_count,ROUND(AVG(f.rating), 2) AS average_rating
FROM Clinics cl
INNER JOIN Consultations c
ON cl.clinic_id = c.clinic_id
INNER JOIN Feedback f
ON c.consultation_id = f.consultation_id
GROUP BY cl.clinic_id, cl.clinic_name
ORDER BY average_rating DESC;

# 13. Staff distribution by clinic
SELECT c.clinic_id,c.clinic_name,s.designation,s.employment_type,COUNT(s.staff_id) AS staff_count,ROUND(AVG(s.salary), 2) AS average_salary
FROM Clinics c
LEFT JOIN Staff s
ON c.clinic_id = s.clinic_id
GROUP BY c.clinic_id, c.clinic_name,s.designation,s.employment_type
ORDER BY c.clinic_id;