import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    array_3x3 = np.array(input_list).reshape((3, 3))

    calculations = {}

    calculations['mean'] = [
        array_3x3.mean(axis=0).tolist(), 
        array_3x3.mean(axis=1).tolist(), 
        np.mean(array_3x3).tolist()
    ]
    calculations['variance'] = [  # Renamed 'var' to 'variance' to match the expected keys
        array_3x3.var(axis=0).tolist(), 
        array_3x3.var(axis=1).tolist(), 
        np.var(array_3x3).tolist()
    ]
    calculations['standard deviation'] = [  # Renamed 'std' to 'standard deviation'
        array_3x3.std(axis=0).tolist(), 
        array_3x3.std(axis=1).tolist(), 
        np.std(array_3x3).tolist()
    ]
    calculations['max'] = [
        array_3x3.max(axis=0).tolist(), 
        array_3x3.max(axis=1).tolist(), 
        np.max(array_3x3).tolist()
    ]
    calculations['min'] = [
        array_3x3.min(axis=0).tolist(), 
        array_3x3.min(axis=1).tolist(), 
        np.min(array_3x3).tolist()
    ]
    calculations['sum'] = [
        array_3x3.sum(axis=0).tolist(), 
        array_3x3.sum(axis=1).tolist(), 
        np.sum(array_3x3).tolist()
    ]

    return calculations