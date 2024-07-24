"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3]
"""

"""
Cho 1 list va n so mat hang, tao mot list ma moi mat hang chi duoc xuat hien nhieu nhat n lan, ma khong duoc thay doi thu tu cac mat hang trong list
vi du neu N = 2 []
"""

from collections import defaultdict

def delete_nth(array, n):
    arr = []
    for num in array:
        if arr.count(num) < n:
            arr.append(num)
    return arr

# nhu l tru khi array count 
def delete_nth_dict(array, n):
    result = []
    counts = defaultdict(int)
    for i in array:
        if counts[i] < n:
            result.append(i)    
            counts[i] += 1
    return result 

def max_n_item(array, n):
    arr = []
    for num in array:
        if arr.count(num) < n:
            arr.append(num)
    return arr
            

arr = [1,2,3,1,2,1,2,3]
n = 2
print(arr, n)

print(delete_nth(arr,n))
print(delete_nth_dict(arr,n))

            
        
    