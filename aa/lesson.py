while True:
    gender = input('성별을 한글로 입력하세요(남지/여자): ')
    if  gender == '남자' :
        print('MAN')
        break
    elif gender == '여자' :
        print("WOMAN")
        break
    else:
        print("잘못된 입력입니다.")
    
