import random

while True:
    li = ["ぐー", "ちょき", "ぱー"]
    li2 = [["あいこ","勝ち","負け"],["負け","あいこ","勝ち"],["勝ち","負け","あいこ"]]

    input_choice = input("my: ")
    
    cp_choice = random.choice(li)
    print("cp:",cp_choice)
    
    myindex = li.index(input_choice)
    cpindex = li.index(cp_choice)
    result = li2[myindex][cpindex]
    print(result)    
    if result == " 勝ち":
        break