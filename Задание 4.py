

my_str = input("Введите строку из нескольких слов")
variable = my_str.split(' ')
for number , my_str_finish in enumerate (variable,1):
    if len(my_str_finish) > 10:
        my_str_finish = my_str_finish [0:10]
    print(f"{number}. - {my_str_finish}")