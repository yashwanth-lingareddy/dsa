'''

Given a string, find the maximum length contiguous substring of it that is also a palindrome.

Input: 'bananas'
Output: 'anana'

Input: 'abdcbcdbdcbbc'
Output: 'bdcbcdb'

The longest palindromic substring is not guaranteed to be unique. If multiple longest palindromic substring exists, the solution should return the one which appear first in the string.

Input: 'abracadabra'
Output: 'aca'
Explanation: There is no palindromic substring in a string 'abracadabra' with a length greater than 3. There are two palindromic substrings with length 3, namely, 'aca' and 'ada'. The solution returns 'aca' as it appears before 'ada' in the string.

Input: 'dcabc'
Output: 'd'

'''

def expand(s: str, left: int, right: int):
    start_index_of_expanded_palindrome = -1
    end_index_of_expanded_palindrome = -1
    expanded_palindrome = ''
    if left > right:
        return start_index_of_expanded_palindrome, end_index_of_expanded_palindrome, expanded_palindrome
    
    while (left >= 0 and right < len(s) and s[left] == s[right]):
        left -= 1
        right += 1
    
    start_index_of_expanded_palindrome = left + 1
    end_index_of_expanded_palindrome = right - 1
    expanded_palindrome = s[start_index_of_expanded_palindrome: end_index_of_expanded_palindrome + 1]
    return start_index_of_expanded_palindrome, end_index_of_expanded_palindrome, expanded_palindrome

def longest_palindromic_substring(s: str) -> str:
    # Write your code here...
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s[0]
    max_length = 0
    max_continous_string = s[0]
    for i in range(len(s)):
        start, end, panlindome = expand(s, i, i)
        s2, e2, p2 = expand(s, i, i+1)
        if len(p2) > len(panlindome):
            panlindome = p2
            start = s2
            end = e2
        
        if len(panlindome) > max_length:
            max_length = len(panlindome)
            max_continous_string = panlindome
    return max_continous_string

if __name__=="__main__":
    s = 'abdcbcdbdcbbc'
    ans = longest_palindromic_substring(s)
    print(ans)