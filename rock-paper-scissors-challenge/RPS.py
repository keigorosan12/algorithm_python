import random

def main():
    print('じゃんけんを開始します')
    while True:
        print('r,p,sの中から選んでください')
        user = input("")
        rps = ["r", "p", "s"]
        
        if not user in rps:
            print('入力ミスです')
            continue
        
        pc_choice = random.choice(rps)
        
        result = Judgment(user, pc_choice)
        
        print('Your choice: ' + user)
        print("PC's choice: " + pc_choice)
        print('You ' + result)
        
        if result == 'Win' or result == 'Lose':
            break

def Judgment(user, pc_choice):
    if user == 'r':
        result = Rock(pc_choice)
    elif user == 'p':
        result = Paper(pc_choice)
    else:
        result = Scissors(pc_choice)
    return result

def Rock(pc_choice):
    if pc_choice == 'r':
        result = 'Draw'
    elif pc_choice == 'p':
        result = 'Lose'
    else:
        result = 'Win'
    return result

def Paper(pc_choice):
    if pc_choice == 'r':
        result = 'Win'
    elif pc_choice == 'p':
        result = 'Draw'
    else:
        result = 'Lose'
    return result

def Scissors(pc_choice):
    if pc_choice == 'r':
        result = 'Lose'
    elif pc_choice == 'p':
        result = 'Win'
    else:
        result = 'Draw'
    return result