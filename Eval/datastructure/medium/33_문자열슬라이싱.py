# 문자열은 리스트와 동일한 슬라이싱 문법을 지원합니다.
text = input() # 입력: programming
SLICE_SIZE = 3

# 처음 3: pro
print(f"처음 {SLICE_SIZE}: {text[:SLICE_SIZE]}")
# 끝 3: ing
print(f"끝 {SLICE_SIZE}: {text[-SLICE_SIZE:]}")
# 가운데: gramm
print(f"가운데: {text[SLICE_SIZE:-SLICE_SIZE]}")