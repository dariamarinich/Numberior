import time

def get_minimum(arr):
    minimum = arr[0]
    for number in arr:
        if number < minimum:
            minimum = number
    return minimum

def get_maximum(arr):
    maximum = arr[0]
    for number in arr:
        if number > maximum:
            maximum = number
    return maximum

def get_sum(arr):
    sum = 0
    for number in arr:
        sum = sum + number
    return sum

def get_mult(arr):
    mult = 1
    for number in arr:
        mult = mult * number
    return mult

def get_run_time(run_time_start) -> float:
    run_time = time.time() - run_time_start
    return run_time

# доп. тест: получение среднего значения
def get_average_number(array) -> float:
    # сумма
    sum = get_sum(array)
    # ср. значение
    average = sum / len(array)
    return average

file = open("file.txt", "r")
file = file.read().split(' ')

run_time_start = time.time()

if (len(file) > 1):
    numbers = list(map(int, file))
else:
    print("Файл пуст")
    exit(0)

print("Минимум: %d" % get_minimum(numbers))
print("Максимум: %d" % get_maximum(numbers))

try:
    print("Сумма: %d" % get_sum(numbers))
    print("Произведение: %d" % get_mult(numbers))
except OverflowError:
    print("Возникла ошибка переполнения")

print("Среднее значение в последовательности: %f" % get_average_number(numbers))
print("Время выполнения программы: %f секунд" % get_run_time(run_time_start))

quit()