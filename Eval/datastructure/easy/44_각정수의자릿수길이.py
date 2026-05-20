# 문자열 변환 후 len 으로 자릿수 산출.
data_sets = [
    [1, 23, 456, 7890, 5, 100, 9999],
    [1, 5, 9],
    [10000],
]
t = int(input())
nums = data_sets[t]

# 리스트 컴프리헨션으로 각 정수의 자릿수(문자열 길이)를 구해 공백 구분으로 한 줄에 출력
digit_counts = [len(str(num)) for num in nums]
print(*digit_counts)