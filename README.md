# Programmers Python 문제풀이 저장소

프로그래머스 문제들을 파이썬으로 풀이한 코드 저장소입니다.  
유형별로 정리하여 체계적으로 연습하고 있습니다.  
하루 5문제씩 꾸준히 풀이하고 기록합니다.

# Python 문법 정리
## ord() vs chr()
ord(): 문자를 유니코드로 변환
chr(): 유니코드를 문자로 전환

``` python
    for char in string: 
        idx = ord(char) - ord('a')
    ...
    chr(idx + ord('a')) //문자변환
```
### ord('a')를 빼는 이유
`ord('a')`를 빼는 것은 **문자를 0부터 시작하는 인덱스로 변환**하기 위해서입니다.

### 알파벳을 배열 인덱스로 매핑
```python
print(ord('a') - ord('a'))  # 0  (a는 인덱스 0)
print(ord('b') - ord('a'))  # 1  (b는 인덱스 1)
print(ord('c') - ord('a'))  # 2  (c는 인덱스 2)
print(ord('z') - ord('a'))  # 25 (z는 인덱스 25)
```

## isalpha()  
: 해당 문자가 알파벳인 지 유무를 판단

```python
    if s[i].isalpha():
        return False
```

## 정규표현식 
```python
1. new_id_low = re.sub(r'[^a-z0-9\-_.]', '', new_id_low)

    - [^a-z0-9\-_.] : 괄호 안의 문자들을 제외한 나머지를 의미
    - a-z: 알파벳 소문자
    - 0-9: 숫자
    - \-_.: -, _, .를 포함
    - re.sub(...)은 해당 패턴에 매칭되는 문자를 '' (빈 문자열)로 치환함 = 제거 
```

```python
2. new_id_step3 = re.sub(r'\.+', '.', new_id_step2)

    - \. : 마침표(.) 자체를 의미

    - + : 1개 이상 반복되는 것

    - \.+ : 마침표가 1개 이상 반복되는 부분을 찾는다

    - '.' : 그 부분을 마침표 하나로 치환
```

## .strip('.')
: 문자열 양쪽 끝에 있는 마침표(.)만 제거  
ex) .aaa. => aaa

## sorted(), sorted(arr, reverse=True)
: 리스트 오름차순/ 내림차순 정렬
ex) 1) sorted(arr, reverse=True) : [1,2,3,4,5] -> [5,4,3,2,1]
    2) sorted(arr) : [3,4,2,1,6] => [1,2,3,4,5]

## set()
: 리스트 중복 제거  

```python
list = [1, 1, 2, 2, 3, 4]
print(list(set(list)))
# set을 하면 object로 반환되기 때문에 list로 변환 후  return
=> [1,2,3,4]
```

## dic.get("key", defaultValue)
: 딕셔너리에 해당 key 값이 있으면 값을 가져오고, 없으면 defaultValue로 설정
ex)

```pyhon
participant = ["leo", "kiki", "eden", "leo"]
dic = {}

for p in participant:
    dic[p] = dic.get(p, 0) + 1
    print(dic)
```

```python
{'leo': 1}
{'leo': 1, 'kiki': 1}
{'leo': 1, 'kiki': 1, 'eden': 1}
{'leo': 2, 'kiki': 1, 'eden': 1}

```
## dic.items()
: 딕셔너리의 key, value 값을 불러올 수 있음
ex)

```python
dic = dict({"A":0, "B":0})

for key,val in dic.items():
    print(key) 
    print(val)
``` 

