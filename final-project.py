flatten_list  = [[1, -20, 3], [2, -200, -3]]

def flattenFunc (x):
    new_list = []
    for list_1 in x:
        for list_2 in list_1:
            new_list.append(list_2)
    print(new_list)

flattenFunc(flatten_list)

reverse_list = [[1, 2], [3, 4], [5, 6, 7]]

def reverseFunc (y):
    y.reverse()
    for z in y:
        z.reverse()
    print(y)

reverseFunc(reverse_list)
