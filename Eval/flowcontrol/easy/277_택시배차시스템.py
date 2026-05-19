# 바깥 if는 배차 가능 여부, 안쪽 if는 목적지 유무로 작성하세요.
available:bool = input() == "True"
destination = input()

# 1. 배차 가능하면
if available:
    # 1-1. destination이 존재하면 
    if destination:
        print("운행 시작")
    # 1-2 비어있으면 목적지를 입력하세요 출력
    else:
        print("목적지를 입력하세요")
# 2. 배차 불가능하면 차량 대기 중 출력
else:
    print("차량 대기 중")