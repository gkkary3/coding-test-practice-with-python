--https://school.programmers.co.kr/learn/courses/30/lessons/59414

-- 코드를 입력하세요
SELECT
ROW_NUMBER() OVER (ORDER BY ANIMAL_ID) AS 순번,
ANIMAL_ID, NAME, DATE_FORMAT(DATETIME,'%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
LIMIT 5 OFFSET 5