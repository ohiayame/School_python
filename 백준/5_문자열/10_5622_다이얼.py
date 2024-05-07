dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
msg = input()
timer = 0
for msg_index in range(len(msg)):
    for dial_index in dial:
        if msg[msg_index] in dial_index:
            timer += dial.index(dial_index) + 3
            
print(timer)