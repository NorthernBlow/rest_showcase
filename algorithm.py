import sys


def sequence(n):
    num = 1  # текущее число
    count = 1  # текущее количество повторений числа
    i = 0  # счётчик выводимых элементов

    while i < n:
        for i in range(count):
            if i == n:
                break
            sys.stdout.write(str(num))
            i += 1
        count += 1
        num += 1



n = int(input())
sequence(n)

