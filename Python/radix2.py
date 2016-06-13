def radix_sort(my_list):
    len_my_list = len(my_list)
    modulus = 10
    div = 1
    while True:
        # empty array, [[] for i in range(10)]
        new_list = [[], [], [], [], [], [], [], [], [], []]
        for value in my_list:
            least_digit = value % modulus
            least_digit /= div
            new_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10

        if len(new_list[0]) == len_my_list:
            return new_list[0]

        my_list = []
        rd_list_append = my_list.append
        for x in new_list:
            for y in x:
                rd_list_append(y)

random_data = [10, 6, 102, 31, 3, 500, 1000, 870, 1, 22, 44, 51, 16, 234]
print radix_sort(random_data)
