# literal 사용한 생성
my_dict = {'name': 'Alice', 'age': 25}


# 키보드 인자 사용
my_dict = dict(name="Alice", age=25, country="USA")
print(my_dict)
# 출력 : {'name': 'Alice', 'age': 25, 'country': 'USA'}


# 튜플 리스트 사용
pairs = [("name","Alice"), ("age", 25), ("country", "USA")]
my_dict = dict(pairs)
print(my_dict)
# 출력 : {'name': 'Alice', 'age': 25, 'country': 'USA'}


# 키 리스트와 zip사용
keys = ["name", "age", "country"]
values = ["Alice", 25, "USA"]
my_dict = dict(zip(keys, values))
print(my_dict)
# 출력 : {'name': 'Alice', 'age': 25, 'country': 'USA'}

