from itertools import count,cycle
#итератор, генерирующий целые числа, начиная с указанного,
for el in count(int(input('введите стартовое занчение от 1 до 10: '))):
    if el > 27 :
        break
    else:print(el)


#итератор, повторяющий элементы некоторого списка, определенного заранее.
c = 0
for el in cycle(["Hello",30,"World"]):
    if c > 27:
        break
    else:print(el)
    c += 1