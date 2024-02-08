counter = 0
"""Распечатываю файл с помощью цикла"""
file_byron = 'byron.txt'
with open(file_byron, mode='r',encoding='utf8') as file:
    for line in file:
        counter += 1
        if counter > 1:
            print(line, end='')
    counter = 0



"""Распечатываю файл с помощью цикла и метода readlines()"""
file_byron = 'byron.txt'
with open(file_byron, mode='r',encoding='utf8') as file:
    lines = file.readlines()
    for line in lines:
        counter += 1
        if counter > 1:
            print(line, end='')
    counter = 0

"""Распечатываю файл с помощью цикла и метода readline()"""
file_byron = 'byron.txt'
with open(file_byron, mode='r',encoding='utf8') as file:
    line = True
    while line:
        line = file.readline()
        counter += 1
        if counter > 1:
            print(line, end='')
    counter = 0


"""Оператор with автоматически закрывает файл по окончанию блока кода в котором он использовался"""
