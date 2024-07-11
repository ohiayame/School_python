# 딕셔너리 정의 
person = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# 키와 값을 순회
for key in person:
    print(f"key: {key}, Value: {person[key]}")

# items() 메서드를 사용한 순회
for key, value in person.items():
    print(f'Key: {key}, Value: {value}')

# keys() 메서드를 사용한 순회
for key in person.keys():
    print(f'Key: {key}')

# values() 메서드를 사용한 순회
for value in person.values():
    print(f'Value: {value}')