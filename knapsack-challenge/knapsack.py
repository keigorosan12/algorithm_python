import numpy as np

num = 10 #道具数
capacity = 2000 #最大キャパ
gram_value = [[100, 6], [130, 9], [150, 11], [200, 21], [160, 18], [210, 24], [250, 28], [300, 19], [330, 25], [570, 32]]

dp = [[0]*(capacity+1) for j in range(num+1)] #DPテーブルの作成
binary = np.zeros((num+1,capacity+1,num)) #binaryデーブルの作成

for i in range(num):
    for j in range(capacity+1):
        if j < gram_value[i][0]: #道具を追加しない場合
            dp[i+1][j] = dp[i][j]
            binary[i+1][j] = binary[i][j]
            
        else: #道具を追加する可能性がある場合
            #選んだ道具が現在の荷物より高い価値を生み出すかどうか判断
            dp[i+1][j] = max(dp[i][j],dp[i][j-gram_value[i][0]]+gram_value[i][1])
            
            if dp[i][j] >= dp[i][j-gram_value[i][0]]+gram_value[i][1]:
                binary[i+1][j] = binary[i][j]
                
            else:
                #追加する荷物と追加していた荷物を組み合わせる場合のbinary情報の更新
                if dp[i+1][j] > gram_value[i][1]:
                    binary[i+1][j] = binary[i][j-gram_value[i][0]]
                #現在の道具のbinary情報の更新
                binary[i+1][j][i] = 1
        


print(dp[num][capacity])
#リストを形式に変換して表示
print(''.join(map(str, [int(i) for i in binary[num][capacity].tolist()])))