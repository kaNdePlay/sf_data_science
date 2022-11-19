"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Этот приём каждый раз в 2 раза сокращает область поиска,
            и в конце нам становится легко угадать даже простым перебором.  
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0
    min_num = 1
    max_num = 101

    while True:
        count += 1
        # сумма может быть нечетная - округляем
        predict_number = int((max_num + min_num) / 2)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла, если угадали
        if number > predict_number:
            min_num = predict_number
        else:
            max_num = predict_number

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict2 ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    score_game(random_predict)