# 주사위 さいころ
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

num1,num2,num3 = map(int,input().split())

if num1 == num2 == num3:
    value = 10000 + (num1 * 1000)
elif num1 == num2 or num1 == num3 :
    value = 1000 + (num1 * 100)
elif  num2 == num3:
    value = 1000 + (num2 * 100)
else:
    max = ""
    if num1 >= num2 and num1 >= num3:
        max = num1
    elif num2 >= num1 and num2 >= num3:
        max = num2
    else:
        max = num3     
    value = max * 100
print(value)