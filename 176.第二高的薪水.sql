--
-- @lc app=leetcode.cn id=176 lang=mysql
--
-- [176] 第二高的薪水
--

-- @lc code=start
# Write your MySQL query statement below

-- 法一
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee 
WHERE salary != (
    SELECT MAX(salary)
    FROM Employee
)


-- 法二
-- limit n子句表示查询结果返回前n条数据
-- offset n表示跳过x条语句
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        -- DESC: descending
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
        -- 或者写成LIMIT 1, 1也行
;


-- @lc code=end

