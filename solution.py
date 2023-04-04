import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1015647760 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    t_alpha = t.ppf((1+p)/2, n-1)
    S = np.std(x, ddof=1)
    mean_path_length = np.mean(x)
    a = 2 * mean_path_length / (92 ** 2)
    b = S * np.sqrt(n/2) / (mean_path_length ** 2)
    delta = t_alpha * b
    left_bound = a - delta
    right_bound = a + delta
    return left_bound, right_bound
