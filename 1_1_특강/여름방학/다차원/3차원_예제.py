# 1) 생성 및 초기화

# 작업 선언
# 2x3x3 -> 3차원 리스트 생성
bar = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# List Comprehension
# 2x3x4 -> 3차원 리스트 생성
bar = [[[0 for col in range(4)]for row in range(3)] for depth in range(2)]


# 2) 데이터 접근 및 수정
# bar [Matrix 번호][Matrix Row][Matrix Col]

# 2x3x3 크기의 3차원 리스트를 생성하고 초기
# 이 리스트는 2개의 Matrix를 포함하여,
# 각 Matrix는 2x3 구조를 가진다
bar = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # 첫 번째 Matrix
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]]  # 두 번째 Matrix
]

# 첫 번째 Matrix의 두 번째 행의 세 번째 항목(6)의 값을 10으로 변경
bar[0][1][2] = 10

# 리스트의 현재 상태를 출력 -> 변경된 요소가 포함된 상태로 출력
print(bar)

# 두 번째 Matrix 첫 번째 행의 세 번째 항목(12)의 값을 출력
print(bar[1][0][2])


# 3) 데이터순회

# 외부 루프는 각 Matrix를 반복
for matrix in bar:
    # 중간 루프는 각 Matrix 내의 행을 반복
    for row in matrix:
        # 내부 루프는 행 내의 각 항목을 반복
        for item in row:
            # 각 항목을 탭으로 구분하여 출력하고, 줄 바꿈은 하지 않음
            print(item, "\t", end="")
        # 한 행의 모든 항목이 출력되면, 다음 행으로 넘어가기 전에 줄바꿈을 추가
        print()
    # 한 Matrix의 모든 행이 출력된 후, 구분선을 출력
    print("-"*20)