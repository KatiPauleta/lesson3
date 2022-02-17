def my_func_sum(*nums):
    result = 0
    tip = False
    for num in nums:
        try:
            if num:
                result += float(num)
        except ValueError:
            tip = True
    return result, tip

general_result = 0

while True:
    numbers_string = input('Введите числа через пробел: ').split(' ')
    result, stop_tip = my_func_sum(*numbers_string)
    general_result += result
    print(f'сумма {general_result}')

    if stop_tip:
        break