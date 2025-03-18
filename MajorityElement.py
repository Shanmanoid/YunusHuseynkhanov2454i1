def major_number(test_list):
    max_num = 0
    me = -1

    for num in test_list:
        a = test_list.count(num)
        if a > max_num:
            max_num = a
            me = num
    return me

list1 = [5, 4, 1, 2, 1, 3, 3, 3, 3]
result = major_number(list1)
print(result)