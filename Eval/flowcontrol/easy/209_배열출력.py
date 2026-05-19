# N을 입력받아 1~N*N 숫자를 N열씩 탭 구분으로 출력하세요.
n = int(input())

# 결과 값 저장 변수
result = ""

# 1 ~ n*n 번 순회 -> for 두번 안하고 실행
for num in range(1, n * n + 1):
    # "\t"인지 "\n"인지 정의 (n의 배수면 "\n")
    tab_or_newline = "\t" if num % n != 0 else "\n"
    
    # 결과 문자열에 추가
    result += str(num) + tab_or_newline

# 결과 값 출력
print(result)