# 리스트 생성
my_list = [10, 20, 30, 40, 50]
print("Initial list:", my_list)

# 리스트의 특정 요소 접근
print("Element at index 2:", my_list[2])

# 전체 리스트 출력
print("Full list:", my_list)

# 리스트의 특정 요소를 업데이트
my_list[1] = 25
print("Updated list:", my_list)

# 리스트에 요소 추가
my_list.append(60) # 원소 -> 마지막에 추가
print("List after adding element:", my_list)

# 리스트 내 요소를 지정된 위치에 삽입
my_list.insert(2,15) # 인덱스, 원소
print("List after inserting element at index 2:", my_list)

# 리스트의 특정 요소 제거 
my_list.remove(25) # 원소 
print("List after removing element '25':", my_list)

# 리스트의 특정 인덱스에 있는 요소 제거
del my_list[0]
print("List after deleting element at index 0:", my_list)

# 리스트의 마지막 요소 제거
popped_element = my_list.pop() # 마지막 요소 제거 및 변환
print("List after popping the last element:", my_list)
print("Popped element:", popped_element)

# 리스트 전체를 비우기
my_list.clear()
print("List after clearing all elements:", my_list)
