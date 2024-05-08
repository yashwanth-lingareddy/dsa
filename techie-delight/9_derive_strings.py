'''
Question:
Check if a given string can be derived from another string by circularly rotating it. The rotation can be in a clockwise or anti-clockwise rotation.

Input: X = 'ABCD', Y = 'DABC'
Output: True
Explanation: 'DABC' can be derived from 'ABCD' by right-rotating it by 1 unit

Solution: Concat X with itself and check if Y is sub-string of concatinated string
'''

def is_derived_string(X: str, Y: str) -> bool:
    if Y == '':
        return False
    if len(X) != len(Y):
        return False
    new_string = X + X
    if Y in new_string:
        return True
    return False
