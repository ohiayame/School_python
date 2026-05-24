# 카운터 변수를 두고 for 순회하며 cutoff 이상이면 +1 (또는 컴프리헨션 + len/sum 활용)
scores = [85, 92, 65, 78, 95]
cutoff = int(input())

# 제너레이터 표현식으로 cutoff 이상인 점수의 개수를 합산 (중간 리스트 생성 없이 메모리 효율적)
print(sum(1 for score in scores if score >= cutoff))