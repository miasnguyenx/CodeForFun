"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""

"""Turn nested array into one array
"""
from _collections_abc import Iterable
import numpy

arr = [0, 1, 2, ['b','c','d', [2,3,4]]]
def flatten_array(input_array, output_array=None):
    if output_array is None:
        output_array = []
    for ele in input_array:
        if not isinstance(ele, str) and isinstance(ele, Iterable):
            flatten_array(ele, output_array)
        else:
            output_array.append(ele)
    return output_array
            
print(flatten_array(arr))