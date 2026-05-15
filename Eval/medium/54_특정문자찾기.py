# for i in range(len(text)): 조건 만족 시 출력 후 break. found 플래그로 미발견 처리.
text = "hello python"
target = "p"

found = False   # 찾았는지 found 플래그로 미발견 상태로 정의

# 문자열의 길이 만큼 반복
for i in range(len(text)):
    # 만약에 해당 위치의 글자와 target이 동일하면 
    if text[i] == target:
        # 처음으로 찾은 위치(인덱스)에서 ('p'을(를) I번째 위치에서 찾았습니다!) 형식으로 출력
        print(f"'{target}'을(를) {i}번째 위치에서 찾았습니다!")
        # found 발견 처리 후 즉시 종료
        found = True
        break

# found 플래그가 False 상태면 "찾지 못했습니다" 출력
if not found:
    print("찾지 못했습니다")