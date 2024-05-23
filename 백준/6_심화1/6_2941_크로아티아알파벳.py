li = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()  
charcount = len(word)
for i in li:
    if i in word:
        word = word.replace(i, '*')
        
count = len(word)
print(count)
