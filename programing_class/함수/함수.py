def avg(sum, cou):
    avg = sum / cou
    print(sum, avg)

def get_num(i):
    sumnum = 0
    for _ in range(i):
        input_num = int(input())
        sumnum += input_num
    avg(sumnum, i)

# get_num(3)    


def get_num(num):
    print("짝수" if num % 2 == 0 else "짝수")

#get_num(int(input()))

def get_num(num):
    sum = 0
    for _ in range(num):
        input_num = int(input())
        sum += input_num
    avg = sum / num
    return sum, avg

sum, avg = get_num(4)
print(sum, avg)