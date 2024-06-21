# 자연수 N을 입력 받는다
value = int(input("N 입력:"))

# 첫 번째 줄부터 N번째 줄까지 별의 개수를 1씩 증가
for i in range(1, value):
    print("*" * i)
    
# N번째 줄 이후부터는 별의 개수를 감소시켜 마지막 줄에는 별 1개를 출력    
for i in range(value, 0 , -1):
    print("*" * i)