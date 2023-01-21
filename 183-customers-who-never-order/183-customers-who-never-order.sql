# Write your MySQL query statement below
SELECT 
    cus.name as Customers
FROM Customers as cus
    LEFT JOIN Orders ON cus.id = Orders.customerId
GROUP BY cus.id
HAVING count(Orders.customerId) = 0;