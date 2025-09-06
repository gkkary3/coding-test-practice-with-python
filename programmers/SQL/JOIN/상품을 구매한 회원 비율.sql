--https://school.programmers.co.kr/learn/courses/30/lessons/131534
-- 2021년에 가입한 전체 회원들 중 상품을 구매한 회원수와
-- 상품을 구매한 회원의 비율(=2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수)

-- 코드를 입력하세요
WITH sales_2021 AS (
    SELECT DISTINCT O.USER_ID, YEAR(O.SALES_DATE) AS Y, MONTH(O.SALES_DATE) AS M
    FROM ONLINE_SALE AS O
    INNER JOIN USER_INFO AS U ON O.USER_ID = U.USER_ID
    WHERE U.JOINED LIKE '2021%'
)

SELECT
    S.Y AS YEAR,
    S.M AS MONTH,
    COUNT(DISTINCT S.USER_ID) AS PURCHASED_USERS,
    ROUND(COUNT(DISTINCT S.USER_ID) / (SELECT COUNT(*) FROM USER_INFO WHERE JOINED LIKE '2021%'  ),1) AS PUCHASED_RATIO
FROM sales_2021 AS S
GROUP BY S.Y, S.M
ORDER BY S.Y, S.M