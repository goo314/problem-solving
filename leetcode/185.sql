"""LeetCode

Algorithm : 
    Database
Level :
    Hard
Status :
    Accepted

Wed Dec 11 01:36:06 KST 2024
"""

# Write your MySQL query statement below

with o1 as (
    select departmentId, salary from
    (
        select 
            row_number() over (partition by departmentId order by salary desc) as r,
            departmentId,
            salary
        from (select distinct departmentId, salary from Employee) as e
    ) as s
    where r <= 3
), o2 as (
    select e.departmentId, e.name, e.salary from Employee as e
    join o1 on e.departmentId = o1.departmentId and e.salary = o1.salary
)

select d.name as Department, o2.name as Employee, o2.salary as Salary
from o2
join Department as d on o2.departmentId = d.id