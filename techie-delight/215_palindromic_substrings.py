'''

Given a string, find all possible distinct palindromic substrings in it.

Input : 'google'
'racecar'
Output: {'e', 'l', 'g', 'o', 'oo', 'goog'}

'''
from typing import Set

def expand(left: int, right: int, s: str, result: Set[str]):
    this_string = ''
    while left >= 0 and right < len(s) and s[left] == s[right]:
        if left == right:
            this_string += s[left]
        else:
            this_string = s[left] + this_string + s[right]
        result.add(this_string)
        left -= 1
        right += 1

def palidromic_substring(s: str):
    result = set()
    if s == '':
        return result
    for i in range(len(s)):
        expand(i, i, s, result)
        expand(i, i + 1, s, result)
    
    return result

if __name__=="__main__":
    s = "google"
    ans = palidromic_substring(s)
    print(ans)