import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1015647760 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = x.size
    sum_x_2 = sum([e ** 2 for e in x])
    q_l = chi2(2 * n).ppf(q=alpha / 2)
    q_r = chi2(2 * n).ppf(q=1 - alpha / 2)
    # print(q_l, q_r)
    return np.sqrt(sum_x_2 / q_r / 56), np.sqrt(sum_x_2 / q_l / 56)
