import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1015647760 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    s = np.sqrt(np.mean(x**2) - np.mean(x)**2)
    z = norm.ppf(1 - (1 - p) / 2)
    delta = z * s / np.sqrt(n)
    mean = np.mean(x)
    left = mean - delta
    right = mean + delta
    return (left, right)
