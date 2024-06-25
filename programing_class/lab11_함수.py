# 함수 구현 – 섭씨(C) → 화씨(F) 온도 변환
# 온도 변화 함수
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
    
# 사용자로부터 섭씨 온도를 입력받는다    
input_celsius = float(input("섭씨 온도를 입력하세요: "))

# 함수에 대입
fahrenheit = convert_celsius_to_fahrenheit(input_celsius)

#  변환된 화씨 온도를 출력
print("화씨 온도는 " , str(fahrenheit) + "입니다.")