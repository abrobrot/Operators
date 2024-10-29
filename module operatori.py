first=input('Введите первое число: ')
second=input('Введите второе число: ')
third=input('Введите третье число: ')
if first == second == third:
    print('Ответ: ',3)
if first == second != third or first != second == third or first == third != second :
    print('Ответ: ',2)
if  first != second != third and first != third != second:
    print('Ответ: ',0)
