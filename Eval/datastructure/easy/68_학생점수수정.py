# 이미 있는 키에 다시 대입하면 값이 갱신됩니다.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()            # 학생 이름을 한 줄에 입력받기
new_score = int(input())  # 새 점수를 다음 줄에 입력받기

# 해당 학생의 점수를 갱신
scores[name] = new_score

# 갱신 후 그 학생의 점수를 <이름>: <새 점수> 형식으로 출력
print(f"{name}: {scores[name]}")