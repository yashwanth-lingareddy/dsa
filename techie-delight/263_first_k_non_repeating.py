'''

Given a string, find first `k` non-repeating characters in it by doing only a single traversal of it.

Input: s = 'ABCDBAGHCHFAC', k = 3
Output: ['D', 'G', 'F']

Input: s = 'ABBCDAB', k = 3
Output: ['C', 'D']

If `k` is more than the non-repeating characters count, return all possible non-repeating characters.

Input: s = 'YYXBYX', k = 2
Output: ['B']

Input: s = 'YYXBYXB', k = 3
Output: []

Note: The solution should return non-repeating characters in the same order as they appear in the string.

'''
from typing import List

def first_k_non_repeating(s: str, k: int):
    repeat_chars = {}
    for c in s:
        if c not in repeat_chars:
            repeat_chars[c] = 0
        repeat_chars[c] = repeat_chars[c] + 1
    ans = []
    for key, v in repeat_chars.items():
        if v == 1:
            ans.append(key)
    if len(ans) <= k:
        return ans
    
    return ans[:k]

if __name__=="__main__":
    s = 'ABCDBAGHCHFAC'
    k = 3
    ans = first_k_non_repeating(s, k)
    print(ans)