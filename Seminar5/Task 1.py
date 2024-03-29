"""
Задание 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


def math_operation():  # рекурсивная функция выбора оператора
    operators = {"+", "-", "*", "/"}
    # Вводим знак операции
    operation = input("\nВведите операцию (+, -, *, / или 0 для выхода): ")
    # Если это верная операция, вводим числа
    if operation in operators:
        try:  # Делаем валидацию ввода чисел
            number01 = int(input("Введите первое число: "))
            number02 = int(input("Введите второе число: "))
        # Если ошибка ввода, запускаем рекурсию
        except ValueError:
            print("вы ввели не число, попробуйте еще раз")
            math_operation()
        # Если все хорошо, запускаем подсчет операции
        else:
            match operation:  # выбор операции
                case "+":
                    summ(number01, number02)
                    math_operation()
                case "-":
                    diff(number01, number02)
                    math_operation()
                case "*":
                    multi(number01, number02)
                    math_operation()
                case "/":
                    div(number01, number02)
                    math_operation()
    # Если 0, то выходим
    elif operation == "0":
        print("выход")
        return
    # Если нет совпадений по оператору, то запускаем рекурсию
    else:
        print("введен неверный оператор, попробуйте еще раз")
        math_operation()


# Функция сложения
def summ(num01, num02):
    print("сумма равна {}".format(num01 + num02))


# Функция вычитания
def diff(num01, num02):
    print("разность равна {}".format(num01 - num02))


# Функция произведения
def multi(num01, num02):
    print("произведение равно {}".format(num01 * num02))


# Функция деления
def div(num01, num02):
    if num02:
        print("деление равно {}".format(num01 / num02))
    else:
        print("На 0 делить нельзя, попробуйте еще раз")


math_operation()