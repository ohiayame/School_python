# 사용자로부터 "남자" 또는 "여자"라는 문자열 입력 받는다
gender = input('성별을 한글로 입력하세요(남지/여자): ')

# 입력 값이 “남자” 이면 “MAN” 출력
if gender == '남자' :
    print( "MAN" )

# 입력 값이 “여자” 이면 “WOMAN” 출력
elif gender == '여자' :
    print( "WOMAN" )
    
# 이외의 입력에 대해서는 오류 메시지 출력    
else :
    print("잘못된 입력입니다.")