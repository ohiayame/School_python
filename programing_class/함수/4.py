def max_of_three(num_a, num_b, num_c):
    max_num = num_a
    if max_num < num_b:
        max_num = num_b
    if max_num < num_c:
        max_num = num_c
    return max_num
print(max_of_three(10, 20, 15))