# 누적합 변수와 발견 플래그를 두고, 매 원소를 더한 직후 K 초과 여부를 검사합니다.
nums = [3, 5, 2, 8, 1, 4, 6, 7]
k = int(input())

total = 0
found = False  # K 초과 시점을 발견했는지 나타내는 플래그

# enumerate로 인덱스와 값을 동시에 얻어 Pythonic하게 순회
for idx, val in enumerate(nums):
    # 누적 계산
    total += val

    # total이 입력값을 초과하면 위치 출력 후 종료
    if total > k:
        print("위치:", idx)
        print("누적합:", total)
        found = True
        break

# 끝까지 K를 초과하지 못한 경우
if not found:
    print("한계 미달")