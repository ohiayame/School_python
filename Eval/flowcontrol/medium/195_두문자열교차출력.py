# while 또는 for + range를 사용하여 인덱스로 접근하세요.
s1 = input()
s2 = input()
result = ""
# 더 긴 문자열의 길이를 정의
max_len = max(len(s1), len(s2))

# max_len만큼 순회
for idx in range(max_len):
    # 각각 문자가 남아있으면 추가
    if len(s1) > idx:
        result += s1[idx]
    
    if len(s2) > idx:
        result += s2[idx]

# 결과 값 출력  
print(result)