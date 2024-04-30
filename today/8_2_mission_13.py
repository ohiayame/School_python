# 사용자로부터 초기값(baseValue)을 입력받아 전역 변수로 선언
baseValue = float(input("기본값을 입력하세요: "))

def select0peration():
    global baseValue
    # 더하기, 빼기, 곱하기, 나누기 중 하나의 연산을 수행
    print("1.더하기")
    print("2.빼기")
    print("3.곱하기")
    print("4.나누기")
    #  사용자가 연산을 선택하고 숫자를 입력
    num = int(input("선택"))
    value = int(input("숫자 입력"))
    
    # 분모가 0 : "에러: 0으로 나눌 수 없습니다."
    if num == 4 and value == 0:
        print("에러: 0으로 나눌 수 없습니다." )
        return
    # 더하기
    if num == 1:
        baseValue += value
    # 빼기, 곱하기, 나누기    
    elif num == 2:
        baseValue -= value  
    elif num == 3:
        baseValue *= value
    elif num == 4:    
        baseValue /= value   
                
    print("연산 결과: ", baseValue)  
    return  

select0peration()           
