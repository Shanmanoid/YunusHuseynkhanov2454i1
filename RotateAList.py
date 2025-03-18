def rotate_list(test_list):
    rotate_number = int(input("Please write an index: "))
    exaculated_numbers = test_list[rotate_number:]
    previous_numbers = test_list[:rotate_number]
    print(exaculated_numbers + previous_numbers)

list1 = [2, 1, 6, 8, 3 ,5]
result = rotate_list(list1)R