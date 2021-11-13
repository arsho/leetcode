/*
Title     : 176. Second Highest Salary
Category  : SQL
URL       : https://leetcode.com/problems/second-highest-salary/
Author    : arsho
Created   : 09 March 2020
*/

SELECT IFNULL((Select distinct(Salary)
FROM Employee
ORDER BY SALARY DESC
LIMIT 1
OFFSET 1), NULL) AS "SecondHighestSalary";