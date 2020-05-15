my_dict =  {'1':'Зима','2':'Зима','3':'Весна','4':'Весна','5':'Весна','6':'Лето','7':'Лето','8':'Лето','9':'Осень','10':'Осень','11':'Осень','12':'Зима' }
my_list = ('Зима', 'Весна' ,'Лето' ,"Осень")
month = input('Введите месяц в виде целого числа от 1 до 12:' )
if int(month) > 12 or int(month) <= 0:
    while int(month) > 12 or int(month) <= 0:
        print("Такого месяца нет")
        month = input('Введите месяц в виде целого числа от 1 до 12:')
else:
    print(my_dict[month])
    if  int(month) >= 3 and int(month) <= 5:
            print(my_list[1])

    elif int(month) >= 6 and int(month) <=8:
        print(my_list[2])

    elif int(month) >= 9 and int(month) <=11:
        print(my_list [3])

    elif int(month) == 12 or int(month) <=2:
        print(my_list [0])

