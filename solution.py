import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1015647760 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Вычисляем среднее значение измерений
    x_mean = np.mean(x)
    
    # Вычисляем стандартное отклонение измерений
    x_std = np.std(x, ddof=1)
    
    # Вычисляем критическое значение z_alpha/2
    z_alpha_2 = norm.ppf(1 - (1 - p) / 2)
    
    # Вычисляем доверительный интервал
    interval_half_width = z_alpha_2 * x_std / np.sqrt(len(x))
    interval_left = x_mean - interval_half_width
    interval_right = x_mean + interval_half_width
    
    return (interval_left, interval_right)
