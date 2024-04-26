# 정수를 입력 받아서 짝수면 "짝수"를 출력 홀수면 "홀수"를 출력
# 둘중 한개를 선택 -> 조건은 한개만 나모지는 그 외에 속함
value = int(input("입력"))

if value % 2 == 0:
    print("짝수")

else:       # elif value % 2 == 1 X 굳이 조건을 만들 필요가 없읍 
    print("홀수") 