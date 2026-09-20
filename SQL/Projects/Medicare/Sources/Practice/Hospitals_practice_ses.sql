/* practice */

select hospital_name
from hospitals
where state='Tamil Nadu';

select distinct(bed_capacity)
from hospitals
order by  bed_capacity desc;

Select Doctors_name 
from Doctors 
where Specialization='Cardialogy';

select count(*) as total_hos
from hospitals;

select count(*) as doc_count
from doctors;

select count(*) as dep_count
from departments;

select count(*)
from doctors
where experience_years > 10;

select sum(bed_capacity)
from hospitals;

select round(avg(consultation_fee),2)
from doctors;

#lowest consultation fee - KPI
select min(consultation_fee)
from doctors;

#highest hospital bed capacity -KPI
select max(bed_capacity)
from hospitals;

#How many doctors are there in each specialization -KPI
select  specialization,count(doctor_id) as doc_count
from doctors
group by specialization;

select specialization,count(*) as doc_count
from doctors
group by specialization;

#How many beds does each hospital have - KPI
select hospital_name ,sum(bed_capacity)
from hospitals
group by hospital_name;

#Which hospitals have more than 300 beds
select hospital_name ,sum(bed_capacity) as bed_cap_count
from hospitals
group by hospital_name
having bed_cap_count > 300;

#Show only specializations that have more than 20 doctors
select specialization,count(*) as doc_count
from doctors
group by specialization
having doc_count > 20;

#Show me the top 5 specializations based on number of doctors - KPI
select specialization,count(*) as doc_count
from doctors
group by specialization
order by  doc_count desc limit 5;

select specialization,count(doctor_id) as doc_count
from doctors
group by specialization
order by  doc_count desc limit 5;

#Show only specializations having more than 20 doctors, ranked highest first
select specialization,count(*) as doc_count
from doctors
group by specialization
having doc_count > 20
limit 1;

#Give me each department along with the hospital it belongs to
select d.department_name,h.hospital_name
from departments d
inner join hospitals h
on d.hospital_id = h.hospital_id;

#Show hospitals along with their departments
select d.department_name,h.hospital_name
from  hospitals h
inner join departments d
on d.hospital_id = h.hospital_id;

#How many doctors are associated with each hospital
select h.hospital_name,Count(d.doctor_id)
from doctors d
inner join hospitals h
on d.hospital_id = h.hospital_id
group by h.hospital_name;

select h.hospital_name,Count(d.doctor_id)
from doctors d
inner join hospitals h
on d.hospital_id = h.hospital_id
group by d.hospital_id;

select h.hospital_name,count(d.doctor_id) as doc_count
from hospitals h
inner join doctors d
on  h.hospital_id = d.hospital_id 
group by d.hospital_id;

#How many doctors does each hospital have, including hospitals that currently have no doctors
select h.hospital_name,count(d.doctor_id) as doc_count
from hospitals h
left join doctors d
on  h.hospital_id = d.hospital_id 
group by d.hospital_id;

#Which hospitals have more than 20 doctors
select h.hospital_name,count(d.doctor_id) as doc_count
from hospitals h
left join doctors d
on  h.hospital_id = d.hospital_id 
group by h.hospital_id
having doc_count > 20;


select specialization,count(doctor_id) as doctor_cnt
from doctors
group by specialization
order by doctor_cnt desc limit 5;

#average consultation fee for each specialization - KPI
select specialization,round(avg(consultation_fee),2) as avg_cfee
from doctors
group by specialization;

#How many appointments does each doctor have - KPI
select d.doctor_id,d.first_name,count(appointment_id)
from doctors d
left join appointments a
on d.doctor_id = a.doctor_id
group by d.doctor_id;

#Rank doctors by consultation fee
select first_name,consultation_fee,row_number()over(order by consultation_fee desc) as rnk
from doctors;

#Doctors within departments
select d.department_name,t.first_name,t.consultation_fee,row_number()over(order by consultation_fee desc) as rnk
from departments d
left join doctors t
on d.department_id = t.department_id;

#Ranking within specialization
select d.department_name,t.first_name,t.consultation_fee,t.specialization,row_number()over(partition by t.specialization order by consultation_fee desc) as rnk
from departments d
left join doctors t
on d.department_id = t.department_id;

#Overall ranking
select d.department_name,t.first_name,t.consultation_fee,rank()over(order by consultation_fee desc) as rnk
from departments d
left join doctors t
on d.department_id = t.department_id;

#Previous doctor's fee
select d.department_name,t.first_name,t.consultation_fee,lag(consultation_fee)over(order by consultation_fee desc) as rnk
from departments d
left join doctors t
on d.department_id = t.department_id;

#Next doctor's fee
select d.department_name,t.first_name,t.consultation_fee,lead(consultation_fee) over(order by consultation_fee desc) as rnk
from departments d
left join doctors t
on d.department_id = t.department_id;

#Rank doctors based on consultation fee within each department
select d.department_name,t.first_name,t.consultation_fee,rank()over(partition by department_name order by consultation_fee desc) as rnk
from departments d
left join doctors t
on d.department_id = t.department_id;
