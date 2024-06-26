li = []

while True:
    try:       
        msg = input()
        
        li.append(msg)
        
    except:
        break
    
for message in li:
    print(message) 