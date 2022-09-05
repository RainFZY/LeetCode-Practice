--
-- @lc app=leetcode.cn id=177 lang=mysql
--
-- [177] 第N高的薪水
--

-- @lc code=start
-- 法一，self join

-- 法二，改176
-- CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
-- BEGIN
-- SET N = N - 1; 
-- -- LIMIT语句不能使用N-1只能用整数，所以重新赋一下值
--   RETURN (
--       # Write your MySQL query statement below.
--     SELECT
--     IFNULL(
--       (SELECT DISTINCT Salary
--        FROM Employee
--        ORDER BY Salary DESC
--         LIMIT N, 1),
--         -- N: offset，跳过几条语句
--         -- 1: row_count，选几条语句
--     NULL) AS getNthHighestSalary
--   );
-- END


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N - 1; 
-- LIMIT语句不能使用N-1只能用整数，所以重新赋一下值
  RETURN (
      # Write your MySQL query statement below.
      SELECT
          (SELECT DISTINCT
                  Salary
              FROM
                  Employee
              -- DESC: descending
              ORDER BY Salary DESC
              LIMIT N, 1) AS SecondHighestSalary
        );
END




-- @lc code=end

