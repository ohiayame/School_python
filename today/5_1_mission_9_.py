# 사용자로부터 입력을 받는다
value1 = int(input("첫 번째 수 입력: "))
value2 = int(input("두 번째 수 입력: "))
value3 = int(input("세 번째 수 입력: "))

# 모든 수가 다른경우
if value1 != value2 != value3:
    if value1 > value2 and value1 > value3 :
        print("모든 수가 다릅니다. 가장 큰 숫자는",value1, "입니다.")
    elif value2 > value1 and value2 > value3:
        print("모든 수가 다릅니다. 가장 큰 숫자는",value2, "입니다.") 
    else :
        print("모든 수가 다릅니다. 가장 큰 숫자는",value3, "입니다.")    

# 두 수가 같은 경우    
elif value1 == value2 != value3 :
    print("두 수가 같습니다.({}와 {})".format(value1,value2))    
elif  value2 == value3 != value1 :
    print("두 수가 같습니다.({}와 {})".format(value2,value3))
elif value1 == value3 != value2:    
    print("두 수가 같습니다.({}와 {})".format(value1,value3))
    
# 모든 수가 같은 경우    
else:
    print("모든 수가 같습니다.")    