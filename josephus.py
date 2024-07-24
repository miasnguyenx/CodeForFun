"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.
For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""
from numpy import array


array = [1,2,3,4,5,6,7,8,9]
final = []
def josepush(array, skip):
    skip -= 1
    initial = array
    final = []
    idx = 0
    len_list = len(initial)
    while(len_list > 0):
        idx = (skip + idx) % len_list   # hash index to every 3rd
        yield initial.pop(idx)
        len_list -= 1
for i in josepush(array, 3):
    final.append(i)
print(final)
        