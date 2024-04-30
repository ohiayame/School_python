# 1제곱미터 (m²) = 10.7639 평방피트 (ft²) 
# 1에이커 (ac) = 4046.86 제곱미터 (m²)

# 제공된 변환 공식을 사용하여 면적을 평방피트(ft²)와 에이커(ac)로 변환
# convert_to_square_feet: 제곱미터를 평방피트로 변환합니다. 
def convert_to_square_feet(square_meters):
    feet = square_meters * 10.7639 
    return feet

# convert_to_acres: 제곱미터를 에이커로
def convert_to_acres(square_meters) :
    acres = square_meters / 4046.86
    return acres

# 사용자로부터 토지의 면적을 제곱미터(m²) 단위로 입력 받는다
input_square_meters = float(input("토지의 면적을 제곱미터(m²)단위로 입력하세요: "))

feet = convert_to_square_feet(input_square_meters)
acres = convert_to_acres(input_square_meters)

# 입력받은 면적이 음수일 경우, 변환 대신 "잘못된 입력입니다"를 출력
if input_square_meters > 0 :
    print(input_square_meters,"제곱미터는",feet, "평방피트입니다.")
    print(input_square_meters,"제곱미터는",acres, "에이커입니다.")
else :
    print("잘못된 입력입니다")    