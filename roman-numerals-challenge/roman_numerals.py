
#記号パターン
roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
roman_decrease = {4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}

def convert_to_roman(n):
    try:
        target = str(n)

        # 桁数を取得
        target_digit = len(target)
        result = ''
        
        for i in target:
            i = int(i)
            target_digit -= 1

            # 減算即を用いる場合
            if i == 4 or i == 9:
                result += roman_decrease[i * 10 ** target_digit]
                continue

            if i >= 5:
                result += roman[5 * 10 ** target_digit]
                i = i - 5

            result += roman[10 ** target_digit] * i

        print(result)
    
    except:
        print('1以上3999以下の範囲の値にしてください。')