from math import pi
def area(r):
    areaC = pi*(r**2)
    return areaC
valores = [1, 3, 0, -1, -3, 2+3j, True, 'hola']

for v in valores:
    areacalculada = area(v)
    print('Para el valor', v, 'el área es', areacalculada)
    
#Module imports
from types import *
import pandas as pd
import numpy as np
from collections.abc import Iterable

list_one = [1, 3, 5, 6]

assert 5 in list_one #Success Example
assert 5 not in list_one #Fail Example
