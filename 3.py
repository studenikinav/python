a =  input( 'введите число от 1 до 9 : ' )
a_first = int(a)
b = a + a
с = b + a
while a_first >= 10 or a_first == 0:
    if a_first >= 10 or a_first == 0:
        print('введено неверное число')
    a_first = int(input('введите число от 0 до 9 : '))
else:
   if a_first < 10:
       r = int(a) + int(b) + int(с)
       print('Сумма введеных чисел n + nn +nnn: ',r)

