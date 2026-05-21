# 슬라이스 할당은 `lst[a:b] = 새로운_시퀀스` 형태로 사용합니다. 길이가 달라도 OK.
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start = int(input())
end = int(input())

# data[start:end] 구간을 단일 원소 [0] 으로 교체
data[start:end] = [0]

# 교체된 최종 리스트를 공백으로 구분하여 한 줄에 출력
print(*data)