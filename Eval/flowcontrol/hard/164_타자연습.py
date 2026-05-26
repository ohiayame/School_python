def count_result(input_text, original):
    """입력 문자열과 원본 문자열을 글자별 비교해 맞은 글자 수를 반환합니다."""
    # 두 문장 길이가 다르면 짧은 쪽만 비교
    text_len = min(len(input_text), len(original))
    count = 0
    for idx in range(text_len):
        if input_text[idx] == original[idx]:
            count += 1
    return count

# 3개 문장을 라운드별로 처리하세요.
texts = ["Hello Python", "I love coding", "Practice makes perfect"]

total_correct = 0      # 맞춘 글자 수의 합
texts_total_chars = 0  # 원본 총 글자 수

print("=== 타자 연습 ===")
print("표시된 문장을 정확히 입력하세요!")
print()

for num in range(len(texts)):
    # 각 라운드마다 해당 문장을 표시하고 사용자 입력을 받아 글자별 비교
    print(f"[{num + 1}번 문장] {texts[num]}")
    input_text = input()

    # 카운터
    count = count_result(input_text, texts[num])
    # 정확도 = (맞은 글자 수 / 원본 글자 수) * 100, 소수점 첫째 자리까지 (int(acc*10)/10으로 계산)
    accuracy = int((count / len(texts[num])) * 100 * 10) / 10

    # 맞춘 문자 수 / 총 글자 수 누적
    total_correct += count
    texts_total_chars += len(texts[num])  # 하드코딩 대신 변수로 누적

    # 정확도: A.A% (C/O 글자) 형식으로 출력
    print(f"정확도: {accuracy:.1f}% ({count}/{len(texts[num])} 글자)")
    print()

# 마지막에:
# === 최종 결과 ===
# 전체 정확도: A.A% (C/T 글자) 출력
# 전체 정확도를 총 글자 기준으로 직접 계산 (정확도 평균 대신 글자 비율로 계산)
final_accuracy = int((total_correct / texts_total_chars) * 100 * 10) / 10
print("=== 최종 결과 ===")
print(f"전체 정확도: {final_accuracy:.1f}% ({total_correct}/{texts_total_chars} 글자)")