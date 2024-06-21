shopping_list = []
# 품목들을 쇼핑 리스트에 추가
#  'milk', 'bread', 'eggs', 'apple'
shopping_list.append('milk')
shopping_list.append('bread')
shopping_list.append('eggs')
shopping_list.append('apple')

print(shopping_list)

# toilet paper'가 빠져 있는 것을 발견하고 리스트의 맨 앞에 추가
shopping_list.insert(0,"toilet paper")

# 'orange juice'를 리스트의 두 번째 위치에 추가
shopping_list.insert(1,"orange juice")

# 'chicken', 'rice'를 리스트에 추가해야 하는데, 이 두 품목을 한 번의 연산으로 리스트에 추가하세요. (extend()함수 또는 ‘+’ 연산 사용)
shopping_list += ['chicken', 'rice']

print(shopping_list)