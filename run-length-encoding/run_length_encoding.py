def run_length_encode(text):
    A_count = 0
    B_count = 0
    compression = [] 
    
    #変数textの文字列を一つずつループする
    for i in text:
        if i == 'A':
            #iがAのときにB_countが0以上であればcompressionにBとBのカウント数を格納
            if B_count > 0:
                compression.append('B' + str(B_count))
                B_count = 0
            A_count += 1
        else:
            #iがBのときにA_countが0以上であればcompressionにAとAのカウント数を格納
            if A_count > 0:
                compression.append('A' + str(A_count))
                A_count = 0
            B_count += 1
    
    return ''.join(compression)  #compressionを連結したものを戻り値とする