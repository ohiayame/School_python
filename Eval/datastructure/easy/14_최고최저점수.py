# 두 함수 호출만으로 한 줄씩 출력하면 됩니다.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [50, 60, 40],
    [42],
]
t = int(input())
scores = data_sets[t]

# max(seq): 시퀀스에서 최댓값 반환
# min(seq): 시퀀스에서 최솟값 반환
# 결과 값 출력 — f-string으로 포맷 의도를 명시적으로 표현
print(f"최고: {max(scores)}")
print(f"최저: {min(scores)}")