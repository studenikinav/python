x =  float(input("выработка в часах: "))
y = int(input("ставка в часах: "))
z = int(input("премия: "))
def wage():
    return print (f' заработная плата сотрудника {(x * y) + z} рублей')


wage()