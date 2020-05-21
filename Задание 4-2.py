my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(my_new_list)


print(f'Для чисел в пределах от 20 до 240 числа, кратные 20 или 21: {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

