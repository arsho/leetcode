# Write your MySQL query statement below
SELECT Email from Person GROUP BY Email Having Count(*)>1;
