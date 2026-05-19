# 정렬이 아니라 단순 역순임에 유의.
data_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤", "예준"],
    ["red", "green", "blue"],
    ["혼자"],
]
t = int(input())
names = data_sets[t]

#  해당 리스트 순서를 뒤집어 공백 구분으로 한 줄에 출력
print(" ".join(names[::-1]))