# 구매한 각 물건의 가격과 개수
# 구매한 물건들의 총 금액

# 영수증에 적힌 총 금액
cost_X = int(input())
# 물건의 종류의 수
value_N = int(input())

result_cost = 0
# 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.
for _ in range(value_N):
    a,b = map(int,input().split())
    result_cost += a * b
    
if result_cost == cost_X:
    print("Yes")
else:
    print("No")