#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число
    Args:
        number (int, optional): Загаданое число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0
    start = 1
    end = 100

    while True:
        count += 1
        predict_number =  (start + end)//2 # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        elif (number > predict_number):
            start = predict_number
        else:
            end = predict_number
    return count


def score_game(random_predict) -> int:
    """За какое колличество попыток в среднем из 1000 подходов угадывает наш алгоритм
    Args:
        random_predict (_type_): Функция угадывания
    Returns:
        int: среднее колличество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print("Your algorithm guesses the number in average for:{score} attemts")
    return score

# RUN
if __name__ == "_main_":
    score_game(random_predict)