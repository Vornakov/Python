"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод
running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета используйте функцию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time


class TrafficLight:
    # colors = [('красный', 7), ('желтый', 3), ('зеленый', 5)]
    # хотел сделать через список кортежей, но пока не хватает способностей

    # создаем список вариантов цветов
    colors = ['красный', 'желтый', 'зеленый']
    # создаем список задержки светофора
    timeouts = [7, 3, 5]

    # определяем приватный атрибут
    def __init__(self, color):
        self.__color = color
        print("\nСоздан {} светофор".format(color))

    # определяем метод переключения светофора
    def running(self):
        # находим индекс цвета в списке
        try:
            ind = self.colors.index(self.__color)
        # если введен неверный цвет, по умолчанию запускаем красный светофор
        except ValueError:
            ind = 0
            print("По умолчанию сработает красный светофор")
        # Запускаем работу светофора с найденного индекса, перебираем
        # оставшиеся элементы
        for index in range(ind, len(self.colors)):
            print("Горит {} свет {} секунд".format(self.colors[index],
                                                   self.timeouts[index]))
            time.sleep(self.timeouts[index])

        # вариант для списка кортежей
        # for color, timeout in self.colors:
        #   print("Горит {} свет {} секунд".format(color, timeout))
        #   time.sleep(timeout)


# Проверка возможными вариантами
tl1 = TrafficLight('красный')
tl1.running()

tl2 = TrafficLight('желтый')
tl2.running()

tl3 = TrafficLight('зеленый')
tl3.running()

tl4 = TrafficLight('синий')
tl4.running()