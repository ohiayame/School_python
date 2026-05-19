# 리스트의 길이는 `len()` 으로 구할 수 있습니다.
branches = [
    ["윤서", "지우", "민준", "서윤"],
    ["도윤", "예준", "하준"],
    ["A", "B", "C", "D", "E", "F"]
]
t = int(input())
# t 입력은 무조건 (0~2)임
# 총 몇명인지 len()으로 확인
people = len(branches[t])
# 결과 값 출력
print(f"총 {people}명")