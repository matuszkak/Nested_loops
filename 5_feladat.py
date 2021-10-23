my_list = [[4, 5], [7, 4], [2, 5], [9, 4]]

for sub_list in my_list:
    sum = 0
    element = 0
    while (element < len(sub_list)):
        sum = sum + sub_list[element]
        element += 1
    sub_list.append(sum)

print(my_list)
