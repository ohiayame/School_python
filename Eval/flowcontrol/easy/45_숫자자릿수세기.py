# 양의 정수를 입력받아 
# 몇 자리 수인지 (N은(는) C자리 수입니다.) 형식(f-string)으로 출력하시오.
# 원본 값을 따로 보관하고, while num > 0: num //= 10; count += 1 로 자릿수를 세세요.
num = int(input())
# 원본 num 저장
origin_num = num
# 자리 수 저장 변수
count = 0

# 자리 수가 남아있으면 반복
while num > 0:
    # 1자리 지우기
    num //= 10
    # count에 1추가
    count += 1

# (N은(는) C자리 수입니다.) 형식으로 결과 값을 출력
print(f"{origin_num}은(는) {count}자리 수입니다.")