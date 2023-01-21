# Write your MySQL query statement below
SELECT 
    e.name as Employee
FROM Employee e
    JOIN Employee manager ON e.managerId = manager.id
WHERE e.salary > manager.salary;