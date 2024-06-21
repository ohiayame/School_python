# convert_to_square_feet: 제곱미터를 평방피트로 변환합니다.
# convert_to_acres: 제곱미터를 에이커로 
def convert_to_(square_meters) :
    feet = square_meters * 10.7639 
    acres = square_meters / 4046.86
    print(square_meters,"제곱미터는",feet, "평방피트입니다.")
    print(square_meters,"제곱미터는",acres, "에이커입니다.")

# 사용자로부터 토지의 면적을 제곱미터(m²) 단위로 입력 받는다
input_square_meters = float(input("토지의 면적을 제곱미터(m²)단위로 입력하세요: "))

# 입력받은 면적이 음수일 경우, 변환 대신 "잘못된 입력입니다"를 출력
if input_square_meters > 0 :
    convert_to_(input_square_meters)
else:    
    print("잘못된 입력입니다")    
