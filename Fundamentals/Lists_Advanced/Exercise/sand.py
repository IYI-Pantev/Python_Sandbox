# num = 32
# num_as_str = str(num)
#
# num_list = list(num_as_str)
# print(num_list)
#
# num_list[0], num_list[1] = num_list[1], num_list[0]
# print('-'.join(num_list))
#
my_list = ["dog", "cat", "fish"]
while len(my_list) > 0:
    print(my_list.pop(0), end=" ")
