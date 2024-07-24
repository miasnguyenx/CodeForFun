"""
Given a non-negative number represented as an array of digits,
adding one to each numeral.
The digits are stored big-endian, such that the most significant
digit is at the head of the list.

"""

# def plus_one(digits):
    
    
def plus_one_v1(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits[-1] = digits[-1] + 1
    res = []
    ten = 0
    i = len(digits)-1
    while i >= 0 or ten == 1:
        summ = 0
        if i >= 0:
            summ += digits[i]
        if ten:
            summ += 1
        res.append(summ % 10)
        ten = summ // 10
        i -= 1
    return res[::-1]

print(plus_one_v1([99,9,9,9]))