def my_func (x, y):
    try:
        division = x / y
        return division
    except ZeroDivisionError:
        return "на ноль делить нельзя"
print(my_func((int(input("Введите первое число: "))),(int(input("Введите второе число: ")))))





