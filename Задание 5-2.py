# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


with open("text-5-2.txt","r",encoding="utf-8") as my_f:
    variable = my_f.read()
    print("Количество строк в файле:",len(variable.splitlines()))

with open("text-5-2.txt","r",encoding="utf-8") as my_f:
    variable = my_f.read()
    variable = variable.split()
    print("Общее количество слов в файле: ",len(variable))



