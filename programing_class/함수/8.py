def calculate_average(*li):
    sum = 0
    for i in li:
        sum += i
    avg = sum / len(li)
    return avg
print(calculate_average(1, 2, 3, 4, 5))
print(calculate_average(6, 7, 8))
print(calculate_average(10, 20))