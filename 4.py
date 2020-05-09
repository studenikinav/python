first_number = int(input('введите число '))
maximum = first_number%10
first_number = first_number//10
while first_number > 0:
    if first_number%10 > maximum:
        maximum = first_number % 10
    first_number = first_number//10
print('Наибольшая цифра из введенного числа: ',maximum)