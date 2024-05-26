massive_input = []
massive_otput = []

#Написать программу, которая из имеющегося массива строк 
#формирует новый массив из строк, длина которых меньше, либо равна 3 символам. Первоначальный массив можно ввести 
#с клавиатуры, либо задать на старте выполнения алгоритма. При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.

print('Для окончания ввода напишите end')

while True:
    item = input('Введите элемент массива: ')
    if item == "end":
        break
    else:
        massive_input.append(item)


for i in range(len(massive_input)):
    if len(massive_input[i]) <= 3:
        massive_otput.append(massive_input[i])
        i += 1
    else:
        i += 1

print('Заданный массив: ', massive_input)
print('Новый массив: ', massive_otput)