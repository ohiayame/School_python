# step 인자에 -1을 주어 역순 사본을 만듭니다.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [1, 2, 3],
    [42],
]
t = int(input())
scores = data_sets[t]

# lst[::-1]로 역순으로 출력
print(" ".join(map(str, scores[::-1])))