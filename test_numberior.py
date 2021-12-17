import numberior

def test_numberior():
    assert numberior.get_minimum([4, 5, 7, 0, 4, 1]) == 0, "Тест не прошёл для get_minimum"
    assert numberior.get_maximum([-6, -5, 3, 4, -5]) == 4, "Тест не прошёл для get_maximum"
    assert numberior.get_sum([1, 2, 3, 10, 1]) == 17, "Тест не прошёл для get_sum"
    assert numberior.get_mult([2, 2, 2, 2, 5, -1]) == -80, "Тест не прошёл для get_mult"
    assert numberior.get_average_number([5, 5, 5]) == 5, "Тест не прошёл для get_average_number"
    assert numberior.get_run_time(numberior.run_time_start) < 15, "Время выполнения программы вышло за пределы"
