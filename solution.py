import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1015647760 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Calculate sample mean and standard deviation
    n = len(x)
    sample_mean = np.mean(x)
    sample_std = np.std(x, ddof=1)
    
    # Calculate t-value for two-tailed test with (1-p) confidence level and n-1 degrees of freedom
    t_value = abs(norm.ppf((1-p)/2))
    
    # Calculate margin of error
    margin_of_error = t_value * sample_std / np.sqrt(n)
    
    # Calculate confidence interval
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    
    return (lower_bound, upper_bound)
