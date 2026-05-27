# 본 사람 set + 중복 set 두 개를 운용. 처음 보면 seen 에, 다시 보면 dups 에 추가.
n = int(input())

seen = set() # 본 사람 set
dups = set() # 중복 set

for _ in range(n):
    # 입력 받기
    name = input()

    # 처음 보면 seen 에 추가
    if name not in seen:
        seen.add(name)
    # 다시 보면 dups 에 추가
    else:
        dups.add(name)

# dups가 있으면 이름을 정렬하여 출력
if len(dups) > 0:
    print(*sorted(dups))
# 중복이 없으면 중복 없음 을 출력
else:
    print("중복 없음")