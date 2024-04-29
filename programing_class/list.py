import random
n = 5
max_num = 6

sample_list = [ value for value in range(1, max_num) ]
# sample_list -> [1, 2, 3, 4, 5]

# 삭제한 원소의 리스트
random_list = []
# 5번 반복
for trial_count in range(0, n):
    # random으로 0~4의 값을 생성 ( len(sample_list) -> 5 )
    random_index = random.randint(0, len(sample_list) - 1)    
    print("random index:", random_index)
    
    # random으로 생성한 index의 원소를 sample_list에서 삭제
    random_num = sample_list.pop(random_index)
    # 삭제한 index의 원소를 random_list에 추가
    random_list.append(random_num)    
    
    print("이번에 삭제할 원소",random_num)
    print("삭제한 원소 리스트", random_list)
    print("원소가 삭제된 sample list", sample_list)
    print()
    
print(random_list)
