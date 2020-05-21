variable = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_variable = [el for el in variable if variable.count(el) < 2]
print(new_variable)