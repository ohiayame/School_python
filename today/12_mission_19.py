import random

def saishohagu(jannkenn):
    
    choices = ['ぐー','ちょき','ぱー']
    computer_choice = random.choice(choices)
    print('わたしがえらんだのは・・・',computer_choice,'!')
    
    if computer_choice == 'ぐー':
        if jannkenn == "ぐー":
            msg = 'あいこ！'
        elif jannkenn == "ちょき":
            msg = 'あなたの負けだよ！' 
        else:
            msg = 'あなたの勝ちだよ！' 
            
    elif computer_choice == 'ちょき':
        if jannkenn == "ぐー":
            msg = 'あなたの勝ちだよ！'
        elif jannkenn == "ちょき":
            msg =  'あいこ！' 
        else:
            msg = 'あなたの負けだよ！'

    elif computer_choice == 'ぱー':
        if jannkenn == "ぐー":
            msg = 'あなたの負けだよ！'
        elif jannkenn == "ちょき":
            msg = 'あなたの勝ちだよ！'
        else:
            msg =  'あいこ！' 
            
    return msg        

while True: 

    jannkenn = input("ぐーちょきぱーの中から一つ選んで入力してね！ ->　")        
    
    if jannkenn == 'ぐー' or jannkenn == 'ちょき' or jannkenn == 'ぱー':
        msg = saishohagu(jannkenn)
        print('けっかはっぴょ～！',msg) 
        if msg == 'あいこ！':
            print('もういちどあそべるよ！')
            continue
        elif msg == 'あなたの勝ちだよ！':
            print('おめでとう！！！')
            break
        else:
            print('負けたらばっきん！100円はらってね!')
            break
    else:
        print("間違った入力だよ！ぐーちょきぱーの中から一つ選んでね！")    
