from math import sqrt

message = ('Добро пожаловать в самую лучшую программу '
           'для вычисления квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Вывод сообщения вычислений и проверка на меньше нуля."""
    if your_number <= 0:
        return
    result = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {result}')


if __name__ == '__main__':
    print(message)
    calc(25.5)
