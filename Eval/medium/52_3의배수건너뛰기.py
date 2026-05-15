# for i in range(1, 21): if i % 3 == 0: continue; print(i)
# 반드시 continue를 사용하세요.
start = 1    # 시작 수 -> 1
end = 20     # 종료 수 -> 20
drainage = 3 # 건너뛰기 하는 수

# 1부터 20까지 반복
for i in range(start, end + 1): 
    # 3의 배수는 건너뛰기
    if i % drainage == 0: 
        continue
    # 3의 배수 아니면 출력
    print(i)