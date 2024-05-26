msg = list(set(input().upper()))

li = []
count = 0
for char in msg:
    for i in msg:
        if char == i:
            count += 1
    li.append(count)
    count = 0
maxvalue = li[0]
for value in li:
    if maxvalue < value:
        maxvalue = value

count = 0
test = []
for i in li:
    count += 1
    if i == maxvalue:
        char = "".join(msg[count-1])
        test.append(char)
flag = True
for i in test:
    for j in test:
        if i != j:
            flag = False

if flag:
    print(char)
else:
    print("?")



######
msg = input().upper()
count_dict = {char: msg.count(char) for char in set(msg)}
max_count = max(count_dict.values())
most_common_chars = [char for char, count in count_dict.items() if count == max_count]

if len(most_common_chars) == 1:
    print(most_common_chars[0])
else:
    print("?")
    



#########
word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
    count = word.count
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
    print("?")

else:
    print(word_list[(cnt.index(max(cnt)))])
    



""""""
word = input().upper()
char = list(set(word))
cnt = []

for i in char:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(char[cnt.index(max(cnt))])