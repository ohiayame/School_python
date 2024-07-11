# 생성
# 연락처 정보를 저장하는 딕셔너리를 생성
# 각 키는 연락처의 속성을 나타내고, 각 값은 해당 속성의 데이터
contact = {
    "name": "John Doe",                 # 이름 필드
    "email": "John.doe@example.com",    # 이메일 필드
    "phone": "123-456-7890"             # 전화번호 필드
}


# 읽기
# 딕셔너리에서 각 키를 사용하여 연락처 정보를 읽고 출력
print("Name:", contact["name"])   # Jhon Doe
print("Email:", contact["email"]) # John.doe@example.com
print('Phone:', contact["phone"]) # 123-456-7890


# 업데이트
# 딕셔너리의 키에 새로운 값들을 할당하여 기존의 데이터를 업데이트
contact["email"] = "new.email@example.com"  # 'email' 키의 값을 새 이메일 주소로 업데이트
contact["phone"] = "987-654-3210"           # 'phone' 키의 값을 새 전화번호로 업데이트
contact["address"] = "1234 Main St"         # 새 키 'address'를 추가하고 주소 정보를 할당
print("\nUpdated:", contact)                # 업데이트된 전체 딕셔너리를 출력
#{'name': 'Jhon Doe', 'email': 'new.email@example.com'
# 'phone': '987-654-3210', 'address': '1234 Main St'}


# 삭제
# 'phone'키와 해당 값이 딕셔너리에서 삭제
del contact["phone"]
print("\nDeleated phone:", contact)   # 전화번호가 삭제된 후의 딕셔너리를 출력합니다


contact.clear()   # 모든 키와 해당 값 삭제