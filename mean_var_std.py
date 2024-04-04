import numpy as np

def calculate(lst):
    # 
    if len(lst) != 9: raise ValueError("List must contain nine numbers.")
    # Parsint
    arr = np.array(lst).reshape((3,3))
    d = {'mean':[],
         'variance':[],
         'standard deviation':[],
         'max':[],
         'min':[],
         'sum':[] }

    # Mean
    d["mean"] = [arr.mean(axis=n).tolist() for n in [0,1,None]]
    # variance
    d["variance"] = [arr.var(axis=n).tolist() for n in [0,1,None]]
    # standard deviation
    d["standard deviation"] = [arr.std(axis=n).tolist() for n in [0,1,None]]
    # max
    d["max"] = [arr.max(axis=n).tolist() for n in [0,1,None]]
    # min
    d["min"] = [arr.min(axis=n).tolist() for n in [0,1,None]]
    # sum
    d["sum"] = [arr.sum(axis=n).tolist() for n in [0,1,None]]



    return d