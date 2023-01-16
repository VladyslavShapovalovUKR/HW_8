1. NameError: - ошибка получения имени переменной, для получения нужно обратиться к переменной которая не задана
age=int(input())
print(vozrast)

    print(vozrast)
          ^^^^^^^
NameError: name 'vozrast' is not defined

2. ZeroDivisionError: - ошибка при попытке деления на ноль
dig=int(input())
print(dig/0)

    print(dig/0)
          ~~~^~
ZeroDivisionError: division by zero

3. TypeError: возникает при действиях между разными типами данных (например конкантенации числа и строки)
a=int(input())
b=input()
print(a+b)

    print(a+b)
          ~^~
TypeError: unsupported operand type(s) for +: 'int' and 'str'

4. ValueError: возникает когда переменная получает данные некорректного значения (в число записать строку)
a=int(input())
print(a)

    a=int(input())
      ^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'остывс'

5. IndentationError: возникает во время неправильной расстановки пробела (лишний либо недостаточно)

a=int(input())
 print(a)

    print(a)
IndentationError: unexpected indent