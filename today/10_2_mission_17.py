menus = ["피자", "파스타", "샐러드", "스시", "버거"]

# 사용지에게 인덱스를 입력받습니다.
index = int(input("메뉴의 인덱스를 선택하세요(0부터 시작): "))

# 여기에 선택된 인덱스의 메뉴를 출력하는 코드를 작성하세요
# 유효하지 않은 인덱스에 대해서는 오류 메시지를 출력해야 합니다
print(menus[index] if index < 5 else "유효하지 않은 선택입니다.")
