# f-string 정렬: `:<폭` 왼쪽, `:>폭` 오른쪽, `:^폭` 가운데
name = input()
opt = input()  # 입력은 항상 (L / R / C) 중 하나

# L: 왼쪽 정렬 → f"|{name:<10}|"
if opt == "L":
    print(f"|{name:<10}|")
# R: 오른쪽 정렬 → f"|{name:>10}|"
elif opt == "R":
    print(f"|{name:>10}|")
# C: 가운데 정렬 → f"|{name:^10}|"
else:
    print(f"|{name:^10}|")