import numpy as np

def random_predict(number: int = 1) -> int:
    """ Рандомно угадываем число
    Args:
        number (int, optional): Загаданое число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0
    min1 = 1
    max1 = 101
    predict_current = np.random.randint(1, 101)
    
    while True:
        count+=1

        if predict_current == number:
            break # выход из цикла, если угадали
        elif predict_current > number:
            max1 = predict_current
            predict_current -= int((max1 - min1) // 2)
        else:
            min1 = predict_current
            predict_current += int((max1 - min1) // 2)
    return(count)


def score_game(random_predict, size=20) -> int:
    """За какое колличество попыток в среднем из 1000 подходов угадывает наш алгоритм
    Args:
        random_predict (_type_): Функция угадывания
    Returns:
        int: среднее колличество попыток
    """
    count_ls = [] # список для сохранения колличества попыток
    np.random.seed(1) # фиксируем RANDOM SEED для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # находим среднее колличество попыток
    print(f'Ваш алгоритм угадывает число в среднем за:{score} попыток')
    return(score)



if __name__ == '__main__':
    #запускаем
    score_game(random_predict)
