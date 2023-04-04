import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1015647760 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    t_alpha = t.ppf(1 - (1-p)/2, n-2)
    x_mean = np.mean(x)
    s = np.sqrt(np.sum((x-x_mean)**2) / (n-1))
    se = s / np.sqrt(n)
    t_val = se * t_alpha
    a = x_mean - t_val / 2
    b = x_mean + t_val / 2
    return (a, b)
