# `text.split(",")` 으로 분리 → `new_sep.join(parts)` 으로 다시 결합.
parts = input().split(",")  # 콤마로 분리
new_sep = input()

# 새 구분자로 모두 바꾼 결과를 출력
print(new_sep.join(parts))