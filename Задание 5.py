def my_sum():
    total_sum = 0
    variable = False
    while variable == False:
        number = input("Введите числа , для выхода нажмите q")
        """необходимо разбить строку"""
        number= number.split()
        result = 0
        """разбиваю значения строки на индексы"""
        for el in range(len(number)):
            """если под индексом значение q цикл заканчивает"""
            if number[el] == "Q" or number[el] =="q":
                variable = True
                break
                """если нет то значение под индексом переводим в int и суммируем во вр.временную переменную
            далее значение суммируем значения итоговой сыммы с суммой во временной переменной
            """
            else: result = result + int(number[el])
        total_sum = total_sum + result
        print("Сумма введеных чисел равна: ",total_sum)


my_sum()

