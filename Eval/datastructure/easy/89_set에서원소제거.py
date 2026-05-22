# `s.discard(x)` 는 원소가 없어도 오류를 내지 않습니다 (반면 `s.remove(x)` 는 KeyError).
fruits = {"apple", "banana", "cherry", "date", "fig"}
item = input()

# set에서 제거
fruits.discard(item)

# 제거 후 남은 원소를 정렬
print(*sorted(fruits))