import math


def calculator():
    print("Калькулятор")
    print("Выберите операцию: ")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень числа")
    print("7. Факториал числа")
    print("8. Синус числа")
    print("9. Косинус числа")
    print("10. Тангенс числа")
    print("11. Выход")

    choice = input("Введите операцию: ")




    if choice not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
        if choice == "11":
            print("Калькулятор закрыт")
            return

        print("Ошибка: неправильный номер операции")
        print("Введите правильный номер: ")
        print("\n")
        calculator()



    if choice in ('1', '2', '3', '4', '5'):
        while True:
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                break
            except ValueError:
                print("Ошибка: введено некорректное значение")

        if choice == '1':
            result = num1 + num2
            print("Результат: ", result)
        elif choice == '2':
            result = num1 - num2
            print("Результат: ", result)
        elif choice == '3':
            result = num1 * num2
            print("Результат: ", result)
        elif choice == '4':
            if num2 == 0:
                print("Ошибка: Делить на ноль недопустимо")
            else:
                result = num1 / num2
                print("Результат: ", result)
        elif choice == '5':
            result = num1 ** num2
            print("Результат: ", result)

    else:

        while True:
            try:
                number = float(input("Введите число: "))
                break
            except ValueError:
                print("Ошибка: введено некорректное значение")

        if choice == '6':
            if number < 0:
                print("Ошибка: квадратный корень из отрицательного числа недопустим")
            else:
                result = math.sqrt(number)
                print("Результат: ", result)
        elif choice == '7':
            if number < 0:
                print("Ошибка: факториал не может быть отрицательным")
            else:
                result = math.factorial(number)
                print("Результат: ", result)
        elif choice == '8':
            result = math.sin(math.radians(number))
            print("Результат: ", result)
        elif choice == '9':
            result = math.cos(math.radians(number))
            print("Результат: ", result)
        elif choice == '10':
            result = math.tan(math.radians(number))
            print("Результат: ", result)

    print("\n")
    calculator()


calculator()