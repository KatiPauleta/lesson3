def div(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return 'Неверный делитель! Делить на 0 нельзя!'

print(div(int(input('Введите делимое: ')), int(input('Введите делитель: '))))