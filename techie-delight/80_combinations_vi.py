'''

Given a sequence of numbers between 2 and 9, print all possible combinations of words formed from the mobile keypad which has english alphabets associated with each key.

keypad = {
	2: ['A', 'B', 'C'],
	3: ['D', 'E', 'F'],
	4: ['G', 'H', 'I'],
	5: ['J', 'K', 'L'],
	6: ['M', 'N', 'O'],
	7: ['P', 'Q', 'R', 'S'],
	8: ['T', 'U', 'V'],
	9: ['W', 'X', 'Y', 'Z']
}

Input : [2, 3, 4]

Output: {'CEG', 'AEH', 'CDH', 'CFI', 'CEH', 'BEI', 'AFH', 'BFG', 'BDI', 'ADH', 'AEG', 'AEI', 'BEH', 'BFH', 'BDH', 'CEI', 'AFG', 'BFI', 'ADG', 'CDG', 'BDG', 'CDI', 'BEG', 'AFI', 'CFG', 'CFH', 'ADI'}

'''
from typing import List, Set, Dict

def back_track(keypad: Dict[int, List[str]], combination: str, next_digits: List[int], result: Set[str]):
    if not next_digits:
        result.add(combination)
    else:
        for letter in keypad[next_digits[0]]:
            back_track(keypad, combination + letter, next_digits[1:], result)

def letter_combinations(nums: List[int], keypad: Dict[int, List[str]]):
    result = set()
    if not nums:
        return result

    back_track(keypad, '', nums, result)
    return result

if __name__=="__main__":
    keypad = {
        2: ['A', 'B', 'C'],
        3: ['D', 'E', 'F'],
        4: ['G', 'H', 'I'],
        5: ['J', 'K', 'L'],
        6: ['M', 'N', 'O'],
        7: ['P', 'Q', 'R', 'S'],
        8: ['T', 'U', 'V'],
        9: ['W', 'X', 'Y', 'Z']
    }
    digits = [2,3,4]
    combinations = letter_combinations(digits, keypad)
    print(combinations)