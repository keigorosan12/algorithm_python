
def binary_search(item, array):
    array.sort()
    print(array)

    head = 0
    number = len(array) - 1
    while head <= number:
        center = (head + number) // 2
        if array[center] == item:
            return center
        elif array[center] < item:
            head = center + 1
        else:
            number = center - 1
    print('存在しませんでした。')
    return None