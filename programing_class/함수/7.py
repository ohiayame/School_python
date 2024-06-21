def contains(li, num):
    for i in li:
        if i == num:
            return True
    return False
print(contains([1,2,3,4], 3))
print(contains([1,2,3,4], 8))