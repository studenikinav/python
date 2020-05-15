list_one = list(input("Введите множество значений: "))
if len(list_one) % 2 == 0:
    len_list_one = 0
    while len_list_one < len(list_one):
        variable = list_one[len_list_one]
        list_one[len_list_one] = list_one [len_list_one+1]
        list_one [len_list_one+1] = variable
        len_list_one = len_list_one + 2

else: len_list_one = 0
while len_list_one <  len(list_one) -1:
    variable = list_one [len_list_one]
    list_one [len_list_one] = list_one [len_list_one+1]
    list_one [len_list_one+1] = variable
    len_list_one += 2

print(list_one)