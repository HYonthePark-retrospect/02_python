# tuple
# - 변경 불가(immutable)한 list
# - sequence type (indexing[인덱싱], slicing[자르기], iterable[순회]) 가능
# - 주로 함수 반환 값, 안전한 데이터 집합을 만들 때 사용

print('--- tuple ---')
t1 = () # 비어있는 튜플(empty tuple)
t2 = (10) # == 10 (int)10과 같은 int도 immutable하기 때문에 자료형도 int로 나옴
t3 = (10,) # (tuple)(10)과 같음. 여러개가 있는것처럼
t4 = (10, 20)
t5 = 10, 20 #()를 생략한 형태 -> 자동으로 packing

print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))
print(t4, type(t4))
print(t5, type(t5))

# tuple 인덱싱, 읽기 전용(수정불가)
tpl = ('a', 'b', 'c', 'd')
print(tpl[0], tpl[1], tpl[2], tpl[3])

# 변경 및 수정 불가 확인
# tpl[0] = 'A'
# print(tpl[0], tpl[1], tpl[2], tpl[3])

# tuple slicing
print('--- tuple slicing ---')
print(tpl[0:2]) # 0,1만 0번부터 2번 미만까지 ('a', 'b')
print(tpl[1::2]) #1번부터 끝까지 2계단씩 건너뛰며 출력 ('b', 'd')

# tuple unpacking
print('--- tuple unpacking ---')
q, w, e, r = tpl
print(q, w, e, r)

*r, t = tpl #t라는 일반 변수가 있으니 끝에 하나만 남기고 나머지는 list 형태로 packing
print(r, t) # ['a', 'b', 'c'] d
# list랑 똑같으나 수정이 안되는것입니다

# tuple을 이용한 변수 값 할당
print('--- tuple을 이용한 변수 값 할당 ---')
num1, num2 = 100, 200 # 괄호 생략된 튜플
print('num1: ', num1) # 100
print('num2: ', num2) # 200

print("--- tuple을 이용한 값 교환(swap) ---")
num1, num2 = num2, num1 # 대입 연산은 항상 오른쪽부터 해석한다
print('num1: ', num1) # 200
print('num2: ', num2) # 100
