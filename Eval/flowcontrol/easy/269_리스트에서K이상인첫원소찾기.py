# # 발견 여부를 추적하는 플래그 변수를 사용합니다. 조건을 만족하는 첫 원소에서 break.
# nums = [4, 7, 15, 3, 22, 9]
# k = int(input())
# found = False       # 발견 여부(불리언)와 위치를 분리해 falsy 인덱스 0 버그 방지
# found_index = -1    # 찾은 위치 저장용 변수

# # nums 반복
# for i in range(len(nums)):
#     # k 이상인 첫 원소를 찾으면 인덱스 저장 후 break
#     if nums[i] >= k:
#         found = True
#         found_index = i
#         break

# # 결과 출력
# if found:
#     print("위치:", found_index)
#     print("값:", nums[found_index])
# # found 없으면 찾지 못했습니다 출력
# else:
#     print("찾지 못했습니다")


# 발견 여부를 추적하는 플래그 변수를 사용합니다. 조건을 만족하는 첫 원소에서 break.
nums = [4, 7, 15, 3, 22, 9]
k = int(input())
found = False       # 발견 여부(불리언)와 위치를 분리해 falsy 인덱스 0 버그 방지
found_index = -1    # 찾은 위치 저장용 변수
found_val = None    # val을 함께 저장해 출력 시 리스트 재접근 제거

# enumerate로 인덱스와 값을 동시에 받아 nums[i] 중복 접근 제거
for i, val in enumerate(nums):
    # k 이상인 첫 원소를 찾으면 인덱스·값 저장 후 break
    if val >= k:
        found = True
        found_index = i
        found_val = val  # 루프에서 이미 가진 val을 재활용
        break

# 결과 출력
if found:
    print("위치:", found_index)
    print("값:", found_val)  # nums[found_index] 대신 저장된 val 사용
# found 없으면 찾지 못했습니다 출력
else:
    print("찾지 못했습니다")