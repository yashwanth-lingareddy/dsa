'''

Given a string and a dictionary of words, determine if the string can be segmented into a space-separated sequence of one or more dictionary words.

Input:

dict = ['this', 'th', 'is', 'famous', 'Word', 'break', 'b', 'r', 'e', 'a', 'k', 'br', 'bre', 'brea', 'ak', 'problem']
word = 'Wordbreakproblem'

Output: True

Explanation: The string can be segmented. The segmented strings are:

Word break problem
Word brea k problem
Word bre ak problem
Word bre a k problem
Word br e ak problem
Word br e a k problem
Word b r e ak problem
Word b r e a k problem

'''
from typing import List

def word_break(dict: List[str], word: str):
    n = len(word)
    word_set = set(dict)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and word[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[n]

if __name__=="__main__":
    dict = ['this', 'th', 'is', 'famous', 'Word', 'break', 'b', 'r', 'e', 'a', 'k', 'br', 'bre', 'brea', 'ak', 'problem']
    word = 'Wordbreakproblem'
    ans = word_break(dict, word)
    print(ans)