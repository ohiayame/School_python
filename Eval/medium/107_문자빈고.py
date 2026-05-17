# 바깥 for는 선택, 안쪽 for는 개수 세기
text = input()

# 글 반복
for char in text:
    # 개수 세기
    count = 0 
    for c in text:
        if c == char:
            count += 1
    # 글자 개수 출력
    print(f"{char}: {count}개")