# sequence type(시퀀스 자료형)
# - str, list, tuple
# - 저장된 값의 순서가 유지됨
# - 인덱싱과 슬라이싱이 가능하다
# - 순회(iterable) 가능

# List
# - 여러 값(lieral)을 묶어서 관리(aka. 컨테이너 자료형)
# - 특징: 동적으로 list 크기가 변할 수 있다(수정 가능)

print("--- list ---")
lst = [1, 2, 3, 4, 5]
print("lst:", lst)
print("lst(lst):", len(lst))
print("lst[0]:", lst[0])
print("lst[1]:", lst[1])
print("lst[4]:", lst[4])

# list 저장 요수 추가/수정/삭제
# - list는 동적으로 크기 변경이 가능한 mutable 자료형이다
# - mutable: list, set, dict
# - inmutable: int, float, bool, str, tuple
print('--- list mutable check ---')
print("lst", lst)
print("추가 전 id:", id(lst))

before_id = id(lst) # 이전 id, int 타입이기에 불변 형태t

# list.append(값): list 끝에 값 추가
lst.append(999)
print('append 후 lst:', lst)
print('append 후 lst id:', id(lst))
print('append 전후 같은 List인가?', before_id == id(lst))

# list.insert(index, 값)
# - index에 값을 삽입하는 메서드
# - 지정된 index부터 뒤에 있는
# 모든 list 값의 index가 1씩 증가(밀려남)

print('--- list.insert ---')
lst.insert(1, 1.5)
lst.insert(0, 0)
print("insert 후 lst:", lst)
print("insert 후 lst id:", id(lst))
print("insert 후 id 비교:", before_id == id(lst))

# list.update(수정)
# list[인덱스] = 값 (변수에 값 대입해서 변경)
print('--- list update ---')
lst[0] = -10
print('lst:', lst)

# 특정 인덱스 값 제거(삭제라고 안한대)
# List.pop(index): 해당 인덱스 값이 제거
# 제거된 index 뒤 요소들을 한 칸씩 당김
print('--- list.remove ---')
lst.pop(2)
print('lst:', lst)
print('id(lst):', id(lst))
print("insert 후 id 비교:", before_id == id(lst))

# 1차원 list는 변수가 늘어나는 것을 의미함 / tmi : 변수는 값을 1개만 저장할 수 있다
# 2차원 list ex) 트리 구조
student = [
    ['홍길동', 30],
    ['이순신', 80],
    ['세종대왕', 100 ]
]

print("student:", student) # 행 열 순서 / 행 : 가로 열 : 세로
print(student[0][0]) # 홍길동
print(student[1][1]) # 80
print(student[2]) # 2행 전체출력
print(len(student)) # 3(행): 3개의 list가 있으니까 student가 참조하는 칸이 0,1,2 이니까 3
print(len(student[0])) # 2(열): 0행이 가르키는 열의 길이(칸수)는 홍길동, 30 2개이니까 2
print(len(student[0][0])) #3(글자수) : 0,0은 홍길동 -> 홍길동의 글자수는 3개이기 때문에 3

# str.split(구분자)
# - str을 구분자를 기준으로 나누어서 List 형태로 반환
data = '박기현,26,인천시,서구' # CSV(Comma Separated Value) == 콤마로만 이루어진 데이터다 라는 뜻
data_ = data.split(',')
print("data_", data_, type(data_))

name = data_[0]
age = data_[1]
addr1 = data_[2]
addr2 = data_[3]
print(name, age, addr1, addr2)

# list 슬라이싱 (str 슬라이싱과 동일한 방법)
print("--- list slicing ---")
texts = ['hello', '안녕', '곤니찌와', '아가리또고자이마스' ]

# ['hello', '안녕']
# print(texts[0:2:1]) 시작: 끝 : 간격
print(texts[:2])

# ['안녕', '곤니찌와']
# print(texts[1:3])
print(texts[1:3:1]) # 1은 생략 가능

# ['hello'', '곤니찌와']
# print(texts[::2])
print(texts[::2])

# ['곤니찌와', '아가리또고자이마스']
print(texts[2:])

# slicing을 이용한 list 값 변경
print(texts)
texts[:2] = ["ㅁㅁㅁ","ㅠㅠㅠ"] # 0번부터 1번까지 각각의 값으로 바꿔라 라는 뜻
print(texts)

texts[1:3:1] = ["🤗🤗🤗","🤔🤔🤔"] # 1번부터 3번 전까지 1칸 간격씩 수를 가져와라
print(texts)

# list 끼리 더하기(+) 연산
print("--- list 더하기 연산 ---")
a = [10,20]
b = [30,40]

a = a+b
print(a) # [10, 20, 30, 40]

b = b+a
print(b) # [30, 40, 10, 20, 30, 40]

# list 순회(순차 접근, 순차 반복)
# - iterable(반복될 수 있는 : 개발에서의 의미) 특징을 가지는 자료형만 가능
print('--- list 순회 ---')
lst = ['a', 'b', 'c']

# list 요소 순회 == list를 하나씩 접근한다는 말 / 작은 index부터 차례대로 이동
for v in lst:
    print(v)
# 계속 돌아감 index를 하나씩 옮겨감 끝날때까지


# list 인덱스, 요소 순회 / enumerate(열거하다(나열하다))
for index, v in enumerate(lst):
    print(f'lst[{index}]: {v}')