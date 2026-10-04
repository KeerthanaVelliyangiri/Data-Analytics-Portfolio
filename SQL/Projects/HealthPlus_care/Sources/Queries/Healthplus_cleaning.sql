# DATA PROFILING AND CLEANING

# Members data profiling

SELECT distinct gender from Members;

SELECT * from Members where email is null;

SELECT * from Members where email not like '%@%.%';

# Members data cleaning

UPDATE Members
set gender=
CASE
WHEN lower(trim(gender)) in ('male','m')
THEN 'Male'
WHEN lower(trim(gender)) in ('female','f')
THEN 'Female'
ELSE gender
END;

set sql_safe_updates=0;

update Members 
set email=
CASE
WHEN email like '%gmail' and email not like '%@%'
THEN REPLACE(email,'gmail','@gmail')
END
where email not like '%@%.%';

# Claims data profiling

SELECT * from Claims where consultation_id is null;

SELECT * from Claims where insurance_provider is null;

# Billing data profiling

SELECT * from Billing where consultation_id is null;

# Payments data profiling

SELECT * FROM Payments where payment_mode is null;