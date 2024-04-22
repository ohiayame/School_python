# 주어진 점수 리스트에서 각 학기별 최고 점수를 찾아 출력
# 두 학기의 점수를 연속해서 포함
# 리스트의 앞부분은 1학기, 뒷부분은 2학기 점수
scores = [88, 92, 75, 65, 79, 84, 91, 87, 90, 88]
scores2 =[]
# 뒷부분을 반복해서 원서를 scores2리스트에 추가
for scr in scores[6:10]:
    scores2.append(scr)
# scores2리스트에 추가한 부분을 삭제
del scores[6:10]
# max() 함수를 사용해 최고 점수를 출력
print("1학기 최고 점수:", max(scores))
print("1학기 최고 점수:", max(scores2))
