import numpy as np

def swirl_list(length, step):
    #length行length列の正方0行列を作成
    queue = np.zeros((length, length))
    
    #各ループ用の範囲を設定
    I = [0, length]
    J = [1, length]
    K = [0, length-1]
    L = [1, length-1]
    number1 = 0
    number2 = length - 1
    
    value = 0
    while True:
        for i in range(I[0], I[1]):
            #最初は1を格納するため最初のループのみ1を格納するようにしている
            if value == 0:
                value = 1
            else:
                #格納する変数valueに1ループごとにstepの値を追加する
                value += step
            queue[number1, i] = value
        for j in range(J[0], J[1]):
            value += step
            queue[j, number2] = value
        for k in reversed(range(K[0], K[1])):
            value += step
            queue[number2, k] = value
        for l in reversed(range(L[0], L[1])):
            value += step
            queue[l, number1] = value
        
        #次ループ用の範囲を設定
        for List in (I, J, K, L):
            List[0] += 1
            List[1] -= 1

        number1 += 1
        number2 -= 1
        
        
        #lengthが偶数の場合と奇数の場合それぞれの場合で渦巻リスト完成の判定をしてループを抜ける
        if length % 2 == 0:
            center = int(length / 2)
            if queue[center, center - 1] != 0:
                break
        else:
            center = int(length / 2)
            if queue[center, center] != 0:
                break
    
    print(queue)

