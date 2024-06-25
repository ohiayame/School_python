# 1~20의 수 중에서 3의 배수X or 짝수X 수를 출력하는 프로그램

# 1~20의 정수를 반복
for value in range(1,21):
    # 만약에 3의 배수 or 짝수면 pass
    if value % 3 == 0 or value % 2 == 0:
        pass
    # 아니면출력
    else:      
        print(value)