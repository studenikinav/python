
def my_lis (x, y, z):
   my_liso = [x,y,z]
   my_liso.sort(reverse=True)
   if x == y == z:
       return print(sum(my_liso))
   else:my_liso.pop()
   print (sum(my_liso))
my_lis((int(input("введите первое число: "))),int(input("введите второе число: ")),int(input("введите третье число: ")))






