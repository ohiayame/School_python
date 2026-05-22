# 문자열의 `count(sub)` 메서드는 sub이 몇 번 등장하는지 셉니다.
text = input()
target = input()

# text에서 target이 몇 번 등장하는지 계산
count = text.count(target)  # 겹치는 구간은 제외하고 셈
print(count)