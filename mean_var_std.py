import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    list_array = np.reshape(list, (3,3))
    
    calculations = {
        "mean": [list_array.mean(axis=axis).tolist() for axis in (0,1,None)],
        "variance": [list_array.var(axis=axis).tolist() for axis in (0,1,None)],
        "standard deviation": [list_array.std(axis=axis).tolist() for axis in (0,1,None)],
        "max": [list_array.max(axis=axis).tolist() for axis in (0,1,None)],
        "min": [list_array.min(axis=axis).tolist() for axis in (0,1,None)],
        "sum": [list_array.sum(axis=axis).tolist() for axis in (0,1,None)],
    }

    return calculations