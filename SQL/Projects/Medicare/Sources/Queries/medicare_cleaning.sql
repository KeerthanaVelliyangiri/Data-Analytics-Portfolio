/*  Departments data profiling */

SELECT * from Departments where head_doctor_id is null;

/*  Doctors data profiling */

select distinct gender
from doctors;

select gender,count(*)
from doctors
group by gender;

select count(distinct gender) as uni_gc
from doctors;

SELECT * FROM Doctors where department_id IS NULL;

SELECT * FROM Doctors where email IS NULL;

SELECT * FROM Doctors where email NOT REGEXP '^[A-Za-z0-9_%.-]+@[A-Za-z0-9-_.]+\\.[A-Za-z]{2,}$';


/*  Doctors data Cleaning */

select gender,
case 
when lower(TRIM(gender)) in ('male','m') then 'Male'
when lower(TRIM(gender)) in ('female','f') then 'Female'
else gender
end as gender_clean
from doctors;

SET  session SQL_SAFE_UPDATES = 0;

update doctors
set gender=
case
when lower(trim(gender)) in ('male','m') then 'Male'
when lower(TRIM(gender)) in ('female','f') then 'Female'
else gender
end;

SELECT 
email AS old_email,
CASE
WHEN email LIKE '%gmail.com' AND email NOT LIKE '%@%'
THEN REPLACE(email,'gmail.com','@gmail.com') 
WHEN email LIKE '%@gmail'
THEN REPLACE(email,'@gmail','@gmail.com') # THEN CONCAT(email,'.com')
WHEN email LIKE '%@@gmail.com' 
THEN REPLACE(email,'@@gmail.com','@gmail.com')
ELSE email
END AS new_email
FROM Doctors;

update Doctors 
SET email=
CASE
WHEN email LIKE '%gmail.com' AND email NOT LIKE '%@%'
THEN REPLACE(email,'gmail.com','@gmail.com') 
WHEN email LIKE '%@gmail'
THEN REPLACE(email,'@gmail','@gmail.com') # THEN CONCAT(email,'.com')
WHEN email LIKE '%@@gmail.com' 
THEN REPLACE(email,'@@gmail.com','@gmail.com')
ELSE email
END 
WHERE email not like '%@%.%' or
	email like '%@@%.%';

/* Patients data profiling */

SELECT * from Patients where first_name <> ltrim(first_name);

SELECT gender, count(*) 
FROM Patients 
group by gender;

SELECT * FROM Patients where email is null;

SELECT * from Patients where email NOT like '%@%.%'; 

/* Patients data Cleaning */

UPDATE Patients 
SET first_name=ltrim(first_name)
WHERE first_name <> LTRIM(first_name);

SELECT DISTINCT gender from Patients;

SELECT gender ,
CASE
WHEN lower(trim(gender)) in ('m','male')
THEN 'Male'
WHEN lower(trim(gender)) in ('f','female')
THEN 'Female'
END
FROM Patients;
 
update Patients 
set gender =
CASE
WHEN lower(trim(gender)) in ('m','male')
THEN 'Male'
WHEN lower(trim(gender)) in ('f','female')
THEN 'Female'
ELSE gender
END;


SELECT email AS old_email, 
CASE
WHEN email LIKE '%gmail.com' AND email not like '%@%'
THEN REPLACE(email,'%gmail.com','%@gmail.com')
WHEN email like '%gmail'
then concat(email,'.com')
else email
end as new_email
FROM Patients;

 
UPDATE Patients 
set email=
CASE
WHEN email LIKE '%gmail.com' AND email not like '%@%'
THEN REPLACE(email,'gmail.com','@gmail.com')
WHEN email like '%gmail'
then concat(email,'.com')
else email
end
where email not like '%@%.%';

/* Admission Data Profilling */

SELECT * from Admissions where department_id is null;

SELECT * from Admissions where discharge_date is null;

/* Treatments Data Profilling */

SELECT  * FROM Treatments where Admission_id is null;

/* Insurance Data Profilling */

SELECT  * FROM Insurance where insurance_provider is null;

/* Employees Data Profilling */

SELECT gender, count(*) 
from Employee
group by gender;

SELECT * FROM Employees where department_id is null;

/* Employees Data Cleanimg */

select distinct gender from Employees;

UPDATE Employees
set gender =
CASE
when lower(trim(gender)) in ('male','m')
then 'Male'
when lower(trim(gender)) in ('female','f')
then 'Female'
else gender
end;

/* Billing Data Profilling */

SELECT * FROM Billing where admission_id is null;

SELECT * FROM Billing where appointment_id is null;