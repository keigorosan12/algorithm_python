def run_length_decode(text):
    char = ''
    composite = []
    
    #変数textの文字列を一つずつループする
    for i in text:
        #iが数字の場合、変数charに格納しておいた文字をiの値の数作成し、compositeに格納
        if i.isdecimal():
            char = char * int(i)
            composite.append(char)
        #iが数字以外の場合、変数charにiを格納
        else:
            char = i

    return ''.join(composite)