import sys
# li = []
num = int(sys.stdin.readline())
# char = 0

input_value = map(int,input().split())

# for i in input_value:
#     if i == " ":
#         li.append(char)
#         char = 0
#     else:
#         char += int(i)

value = int(input())
count = 0
for test in input_value :
    if test == value:
        count += 1
print(count)