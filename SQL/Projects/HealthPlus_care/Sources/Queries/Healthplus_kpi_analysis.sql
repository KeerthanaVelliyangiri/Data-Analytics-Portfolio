# KPI ANALYSIS

# 1. Total Members
SELECT COUNT(*) AS total_members
FROM Members;

# 2. Total Specialists
SELECT COUNT(*) AS total_specialists
FROM Specialists;

# 3. Total Clinics
SELECT COUNT(*) AS total_clinics
FROM Clinics;

# 4. Total Consultations
SELECT COUNT(*) AS total_consultations
FROM Consultations;

# 5. Highest Consultation Fee
SELECT MAX(consultation_fee) AS highest_consultation_fee
FROM Specialists;

# 6. Total Telemedicine Sessions
SELECT COUNT(*) AS total_telemedicine_sessions
FROM Telemedicine_Sessions;

# 7. Total Package Subscriptions
SELECT COUNT(*) AS total_package_subscriptions
FROM Package_Subscriptions;

# 8. Active Package Subscriptions
SELECT COUNT(*) AS active_package_subscriptions
FROM Package_Subscriptions
WHERE expiry_date >= CURDATE();

# 9. Expired Package Subscriptions
SELECT COUNT(*) AS expired_package_subscriptions
FROM Package_Subscriptions
WHERE expiry_date < CURDATE();

# 10. Total Prescriptions
SELECT COUNT(*) AS total_prescriptions
FROM Prescriptions;

# 11. Total Laboratory Tests
SELECT COUNT(*) AS total_lab_tests
FROM Lab_Tests;

# 12. Total Laboratory Cost
SELECT ROUND(SUM(test_cost), 2) AS total_lab_cost
FROM Lab_Tests;

# 13. Total Insurance Claims
SELECT COUNT(*) AS total_claims
FROM Claims;

# 14. Total Insurance Claim Amount
SELECT ROUND(SUM(claim_amount), 2) AS total_claim_amount
FROM Claims;

# 15. Total Billed Amount
SELECT ROUND(SUM(total_amount), 2) AS total_billed_amount
FROM Billing;

# 16. Total Corporate Members
SELECT COUNT(DISTINCT member_id) AS corporate_members
FROM Corporate_Members;