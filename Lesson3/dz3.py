def my_func(var_1, var_2, var_3):
    perem = [var_1, var_2, var_3]
    perem.remove(min(var_1, var_2, var_3))
    return sum(perem)
print(my_func(10, 20, 30))