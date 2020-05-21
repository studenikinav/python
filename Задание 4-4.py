from functools import reduce
def multiplication (num_1,num_2):
    return num_1 * num_2
print(f'Список четных чисел от 100-1000(включительно):'
      f'  {[el for el in range(99,1001) if el % 2 ==0]}')
print(f'Результат перемножения всех четных чисел от 100-1000'
      f' включительно:   {reduce(multiplication,[el for el in range(99,1001) if el % 2 == 0])}')


