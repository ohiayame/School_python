# pop 의 반환값을 변수에 저장해두면 출력에 활용할 수 있습니다.
data_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["혼자"],
]
t = int(input())
applicants = data_sets[t]

# 지울 사람 이름 복사/ 마지막 원소 삭제
pop_name = applicants.pop()

# 결과 값 출력
print(f"취소된 사람: {pop_name}")
print("남은 명단:", " ".join(applicants))