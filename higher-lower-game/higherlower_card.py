import random
import re

#52枚のトランプカードを作成
card = [
    '♠1', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠11', '♠12', '♠13',
    '♥1', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥11', '♥12', '♥13',
    '♦1', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦11', '♦12', '♦13',
    '♣1', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣11', '♣12', '♣13',
]

score = 0
print('Game start')

while True:
    #現在のスコアを表示
    print('You current score: ' + str(score))
    
    #プレイヤーに見せるカードを選択しcardリストから選んだカードを削除
    choice_card = random.choice(card)
    print('The current card: ' + choice_card)
    card.remove(choice_card)
    
    #プレイヤーに見せないカードを選択しリストから削除
    judge_card = random.choice(card)
    card.remove(judge_card)
    
    print('current card は judge_card よりも数字の大きさは High or Low ?')
    print('Please input H or L')
    #プレイヤーにhighかlowか予測させる入力ミスがあった場合やり直させる
    while True:
        forecast = input()
        if forecast == 'H' or forecast == 'L':
            break
        else:
            print('入力ミスです')
            continue
    
    #それぞれカードの数字のみを抽出して変数に格納
    choice_card_number = int(re.sub(r'\D', "", choice_card))
    judge_card_number = int(re.sub(r'\D', "", judge_card))
    
    #カードの数字を比べてhighのときdrawのときlowのときの条件分岐をそれぞれ作成
    if choice_card_number > judge_card_number:
        if forecast == 'H':
            #正解の場合のみスコア加算
            score += 1
            print('Correct')
        else:
            print('Wrong')
            #不正解だった場合ループを抜ける
            break
    elif choice_card_number == judge_card_number:
        print('Draw')
    else:
        if forecast == 'L':
            score += 1
            print('Correct')
        else:
            print('Wrong')
            break
    
    print('The judge card: ' + judge_card)
    print('')

print('The judge card: ' + judge_card)
print('Game over')
print('your final score: ' + str(score))
