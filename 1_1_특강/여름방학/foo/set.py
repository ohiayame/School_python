my_set = set()

my_set.add(1)
my_set.add(2)
my_set.add(1)  # 중복 요소는 추가되지 않음

# 출력 결과 {1, 2}
print(my_set)

# 다른 집합과의 연산
another_set = {2, 3, 4}
union_set = my_set.union(another_set)   # 합집합 {1, 2, 3, 4}
intersection_set = my_set.intersection(another_set)  # 교집합 {2}

# 출력 결과
print(union_set)
print(intersection_set)