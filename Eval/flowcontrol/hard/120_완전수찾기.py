# 2부터 N까지 완전수를 찾아 출력하세요.
n = int(input())

# n까지 순회
for num in range(2, n + 1):
    # 수 저장 배열
    values = []

    # sqrt(num)까지만 순회해 약수 쌍을 동시에 수집 (O(√num)으로 효율 개선)
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            values.append(i)
            if i != num // i and num // i != num:  # 쌍이 되는 약수 추가 (자기 자신 제외)
                values.append(num // i)

    values.sort()  # 약수를 오름차순 정렬

    # 총합과 입력 값이 같으면 완전수 -> 바로 출력
    if sum(values) == num:
        print(num, "=", " + ".join(map(str, values)))