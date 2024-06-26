# n개의 통 , m번 반복
n, m = map(int,input().split())
li = []
# 1~n번 1~n의 숫자를 한개씩 리스트에 추가
for i in range(1, n+1):
    li.append(i)
# m번 반복
for _ in range(m):
    # 교환하는 통 번호를 입력 받기
    i,j = map(int,input().split())
    # 번호 -> index에 변경
    i -= 1 
    # 만약 마지막 원소면 -1
    if j == n:
        j = -1
    else:
        j -= 1
    # index[i]의 번호를 num 
    num = li[i]
    # 바꾸는 원소의 뒤에 num를 추가
    li[i] = li[j]
    li[j] = num
for value in li:
    print(value, end = " ")