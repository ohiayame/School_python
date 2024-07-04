import random
def Make_List(start, end, N):
    li = random.sample(range(start, end+1), N)
    return li

def maxnum(smorl, big):
    if big > smorl:
        return True
    return False

print("난수를 생성할 범위와 개수를 입력하세요.")
# start값 입력 받기
while True:
    start = int(input("Sart (0 이상의 정수): "))
    if maxnum(0, start):
        break

# end값 입력 받기
while True:
    end = int(input(f"End (Start보다 큰 정수): "))
    if maxnum(start, end):
        break
    else:
        print(f"End는 Start({start})보다 커야 합니다")

# N값 입력 받기
while True:
    N = int(input("N(생성할 난수의 개수): "))
    if N <= end - start +1:
        break
    else:
        print(f"N은 {start}부터 {end} 사이의 정수여야 합니다.")
        
print(f"생성된 난수 리스트:\n{Make_List(start, end, N)}")