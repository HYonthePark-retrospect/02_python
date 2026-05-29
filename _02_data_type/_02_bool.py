# 논리형 boolean

a = True
b = False
print(a, type(a))
print(b, type(b))

# 비교연산
# A > B : A가 B 보다 크면 Ture, 아니면 False
# A >= B : A가 B 이상이면 True, 아니면 False
# A < B
# A <= B
# A == B : A, B가 같으면 True, 아니면 False
# A != B : A, B가 같지 않으면 True   !은 부정의 의미로 쓰임

print("1 > 0.5:", 1 > 0.5) # True
print("1 < 0.5:", 1 < 0.5) # False
print("1 >= 0.5:", 1 >= 0.5) #True
print("1 <= 0.5:", 1 <= 0.5) #False
print("1 == 1:", 1 == 1) #True
print("1 != 1:", 1 != 1) #False

# 논리 부정 연산(not)
print(True)
print(not True)
print(not not True)