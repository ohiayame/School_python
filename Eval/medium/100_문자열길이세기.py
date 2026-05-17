# for char in text: 로 한 글자씩 순회
text = input()
count = 0

# len() 함수를 사용하지 않고 for문으로 한 글자씩 +1
for _ in text:
    count += 1 

# 출력
print("문자열 길이:", count)