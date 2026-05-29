# `students[name]` 자체가 점수 리스트 입니다. sum() 과 len() 으로 평균을 구하세요.
students = {
    "윤서": [85, 90, 78],
    "지우": [92, 88, 95],
    "민준": [65, 70],
    "서윤": [80, 80, 80, 80],
}
name = input()

# 존재하지 않는 이름 입력 시 안내 메시지 출력 (방어적 코드)
if name not in students:
    print("해당 학생을 찾을 수 없습니다.")
else:
    scores = students[name]

    # sum() 과 len() 으로 평균 계산 후 출력
    avg = sum(scores) / len(scores)
    print(f"평균: {avg:.1f}")