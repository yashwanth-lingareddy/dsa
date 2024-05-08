'''
Question
Given a string, check if it is a rotated palindrome or not.

Input: 'CBAABCD'
Output: True
Explanation: 'CBAABCD' is a rotation of the palindrome 'ABCDCBA'

Input: 'BAABCC'
Output: True
Explanation: 'BAABCC' is a rotation of the palindrome 'ABCCBA'

Input: 'DCABC'
Output: False

Solution: Concat the string with itself
from the concatinated string find longest possible palindromic substring
if the length of longest possible palindromic substring is greater than or equal to length of input string, the True
'''

def expand_palindrome(s: str, left: int, right: int):
    start_index_of_expanded_palindrome = -1
    end_index_of_expanded_palindrome = -1
    length_of_expanded_palindrome = 0

    if left > right:
        return start_index_of_expanded_palindrome, end_index_of_expanded_palindrome, length_of_expanded_palindrome
    
    while(left > 0 and right < len(s) and s[left] == s[right]):
        left -= 1
        right += 1
    
    start_index_of_expanded_palindrome = left + 1
    end_index_of_expanded_palindrome = right - 1
    length_of_expanded_palindrome = right - left - 1
    
    return start_index_of_expanded_palindrome, end_index_of_expanded_palindrome, length_of_expanded_palindrome

def longest_palindromic_substring(s: str):
    start_index_of_largest_palindromic_substring = -1
    end_index_of_largest_palindromic_substring = -1
    length_of_largest_palindromic_substring = 0
    for i in range(len(s)):
        start_index, end_index, length = expand_palindrome(s, i, i)
        s_2, e_2, l_2 = expand_palindrome(s, i, i+1)

        if l_2 > length:
            length = l_2
            start_index = s_2
            end_index = e_2
        if length > length_of_largest_palindromic_substring:
            length_of_largest_palindromic_substring = length
            start_index_of_largest_palindromic_substring = start_index
            end_index_of_largest_palindromic_substring = end_index
        
    return s[start_index_of_largest_palindromic_substring:end_index_of_largest_palindromic_substring+1]

def is_rotated_palindrome(s: str) -> bool:
    # Edge case
    if len(s) == 2:
        if s[0] == s[1]:
            return True
        else:
            return False
    new_string = s+s
    l_p_s = longest_palindromic_substring(new_string)
    if len(l_p_s) >= len(s):
        return True
    return False

if __name__=="__main__":
    s = 'DCABC'
    s = 'AB' # edge case
    s = 'AA' # edge case
    ans = is_rotated_palindrome(s)
    print(ans)