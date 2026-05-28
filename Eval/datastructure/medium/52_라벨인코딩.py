# `enumerate(labels[:n])` 으로 (인덱스, 이름) 쌍을 얻고, dict comp 로 {이름: 인덱스} 를 만드세요.
# 알고리즘 흐름: 1) labels[:n] 슬라이싱 → 2) dict 컴프리헨션으로 매핑 생성 → 3) 순회 출력
labels = ["cat", "dog", "bird", "fish", "lion"]
n = int(input())

# 문제 요구사항인 dict 컴프리헨션으로 {이름: 인덱스} 매핑 생성
label_to_idx = {name: idx for idx, name in enumerate(labels[:n])}

# 딕셔너리를 순회하며 출력 (Python 3.7+ 삽입 순서 보장)
for name, idx in label_to_idx.items():
    print(f"{name}: {idx}")