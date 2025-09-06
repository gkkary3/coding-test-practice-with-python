--https://school.programmers.co.kr/learn/courses/30/lessons/59042# ADMIN_OUTS ANIMAL_ID(Foregin Key) # 입양보낸 테이블
# ADMIN_INS  ADMIN_ID(Primary Key) # 입양된 테이블

# 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회

-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS AS O
LEFT JOIN ANIMAL_INS AS I ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY O.ANIMAL_ID;


