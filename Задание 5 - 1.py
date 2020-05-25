# Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
my_f = open("text-one.txt","w")
my_text = input("введите текст\n")
while my_text:
    my_f.writelines(my_text + "\n")
    my_text = input("введите текст\n")
    if not my_text:
        break
my_f.close()
my_f = open("text-one.txt","r")
content = my_f.read()
print(content)
my_f.close()


