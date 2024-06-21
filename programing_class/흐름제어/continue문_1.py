# 구구단 중 3의 배수단만 출력하는 프로그램을 
# continue문을 이용하여 작성
for i in range(2,10):
    if i % 3 != 0 :
        continue
    for c in range(1,10):
        print(f"{i} X {c} = {i * c }")