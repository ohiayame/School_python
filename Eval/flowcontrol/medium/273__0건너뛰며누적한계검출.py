# 누적합 변수와 발견 플래그를 둡니다.
# 한 원소를 살필 때 0이면 즉시 continue, 그 외에는 누적합에 더한 직후 K 도달 여부를 검사하세요.
# 반복문 종료 후 플래그로 "한계 미달" 여부를 판정합니다.
nums = [4, 0, 3, 0, 0, 7, 2, 0, 8, 1]
k = int(input())

total = 0

for i, val in enumerate(nums):  # enumerate 사용으로 인덱스와 값을 동시에 참조
    # 0 원소를 만나면 continue로 다음 원소로 넘어가기
    if val == 0:
        print(f"무시한 위치: {i}")
        continue

    # total 계산
    total += val

    # 누적합이 K 이상이 되는 순간 break
    if total >= k:
        print(f"종료 위치: {i}")
        print(f"최종 누적합: {total}")
        break

# 끝까지 누적합이 K 미만이면 마지막 줄에 한계 미달, 누적합: S 출력
if total < k:
    print(f"한계 미달, 누적합: {total}")