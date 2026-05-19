# 바깥 if는 파일명, 안쪽 if는 확장자 기준으로 작성하세요.
filename = input()
extension = input()

# 파일명과 확장자 -> 저장 가능 여부를 출력
# 1. 파일명이 빈 문자열이면 파일명을 입력하세요
if not filename:
    print("파일명을 입력하세요")
# 2. 파일명이 있으면
else:
    # 2-1. 확장자가 txt이면 텍스트 파일 저장
    if extension == "txt":
        print("텍스트 파일 저장")
    # 2-2. 아니면 지원되지 않는 형식
    else:
        print("지원되지 않는 형식")