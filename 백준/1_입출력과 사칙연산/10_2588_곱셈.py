value = int(input())
value2 = list(input())

num_1 = int(value2[2]) * value
num_2 = int(value2[1]) * value
num_3 = int(value2[0]) * value
print(num_1)
print(num_2)
print(num_3)
    
print(num_1 + num_2*10 + num_3*100)


A = int(input())
B = int(input())

print(A * (B % 10))
print(A * (B % 100 // 10))
print(A * (B // 100))
print(A * B)