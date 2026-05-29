#변수(variable)
# - 값(literal - 데이터가 정확한 뜻이나 데이터라는 언어가 활용되는 곳이 많기에 리터럴이라고함)을 저장하는 메모리 상의 공간
# - 각 변수마다 이름이 지정되어 있다
# [변수 선언 방법]
# 변수명 = 값
from ftplib import print_line

a = 10 # a라는 메모리 상의 공간에 10이라는 데이터(리터럴값)를 대입하겠다
b = '홍길동' # b라는 메모리 상의 공간에 홍길동이라는 리터럴값을 대입한다

print("a =", a)
print("b =", b)

# 대입 연산(=)
# - 우항(오른쪽값)의 값을 좌항(왼쪽의 값)의 변수에 대입을 한다
#  ----- 무조건 위의것을 지킨다 우항 --> 좌항 --------

num = 100
print("num =", num)

#변수는 저장된 값이 변할 수 있다

num = 999
print("num =", num)

num = 'ParkKihyun'
print("num =", num)


# 변수 명명 규칙
# 1. 의미 있는 변수 이름을 사용 리터럴값이 어떤것인지 알 수 있도록
# 2. 변수명은 snake case를 사용( 소문자 + _)
# - 단, 대문자도 사용은 가능하나, 소문자와는 다른 변수이기에 구분이 된

team_name = "오지라퍼스"
print(team_name)    # 오지라퍼스

Team_name = "Ohgiraffers"
print(team_name)    # 오지라퍼스
print(Team_name)    # Ohgiraffers

# 한글이 사용은 가능하나 내수용으로만 가능함, 다 깨짐 그러니 잘 쓰지 마삼
밥조 = "7조"
print("밥조 :", 밥조)

# 변수명은 숫자로 시작은 안된다 -> (문법 오류가 발생함 == 빨간줄)

name_1 = "장원영"
#1_name = ("카리나") # 문법에러, 정하고 싶으면 프로젝트 제목처럼 맨 앞에 _ 사용
print("출력이 되는건 : " + name_1)

# 특수 문자는 언더스코어(_)를 제외하고는 사용 불가
# team-name = '오지랖' 이런 느낌 # error
# rlgusqkr102@gmail.com = '될까요?' #error
# 오로지 _ 만 가능함

# 예약어는 변수명으로 사용 불가 (if, for, else, while 등등)

# 파이썬 예약어 종류 확인
import keyword
print(keyword.kwlist)

