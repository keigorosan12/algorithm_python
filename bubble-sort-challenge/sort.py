
def bubble_sort(sort_list):
    list_length = len(sort_list) - 1 #listをrangeでループできるように調整
    for i in range(list_length):
        for j in range(i+1,list_length):
            if sort_list[i] > sort_list[j]: #listの中の右側にある数字すべてと大小比較
                sort_list[i], sort_list[j] = sort_list[j], sort_list[i] #条件に合えば数字を入れ替え
            else:
                continue
    return sort_list


#改善版
def bubble_sort(numbers):
    for idx, elem in enumerate(numbers):
        for right_idx in range(idx+1,len(numbers)):
            if numbers[idx] > numbers[right_idx]: #listの中の右側にある数字すべてと大小比較
                numbers[idx], numbers[right_idx] = numbers[right_idx], numbers[idx] #条件に合えば数字を入れ替え
    return numbers