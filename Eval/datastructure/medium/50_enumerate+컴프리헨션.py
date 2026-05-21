# enumerate 가 (인덱스, 값) 쌍을 반환하므로 두 변수로 한 번에 받을 수 있습니다.
data_sets = [
    ["red", "green", "blue", "yellow", "purple"],
    ["apple", "banana", "cherry"],
    ["single"],
]
t = int(input())
items = data_sets[t]

# enumerate 와 리스트 컴프리헨션을 함께 사용해 각 원소를 "인덱스:값" 형태 문자열로 변환해 공백 구분 한 줄에 출력
print(" ".join(f"{i}:{name}" for i, name in enumerate(items)))