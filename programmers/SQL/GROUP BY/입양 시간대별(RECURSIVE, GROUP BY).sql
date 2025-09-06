--https://school.programmers.co.kr/learn/courses/30/lessons/59413
WITH RECURSIVE hours AS (
    SELECT 0 AS h
    UNION ALL
    SELECT h + 1 FROM hours WHERE h < 23
)

SELECT h AS HOUR, COUNT(a.DATETIME) AS COUNT
FROM hours
LEFT JOIN ANIMAL_OUTS AS a ON h = HOUR(a.DATETIME)
GROUP BY HOUR
ORDER BY HOUR