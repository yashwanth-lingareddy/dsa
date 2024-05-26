'''
This script will print
- completed quesion numbers
- remainig question number

Run this script from inside techie-delight folder
'''
import os

def check_completion():
    total_questions = 580
    all_questions_dict = {i+1: {'status': 'not_completed'} for i in range(total_questions)}
    directory = "."
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for f in files:
        splits = f.split('_')
        if not splits or len(splits) == 0:
            continue
        question_no = splits[0]
        if not question_no.isdigit():
            continue
        question_no = int(question_no)
        if question_no not in all_questions_dict:
            continue
        all_questions_dict[question_no]['status'] = 'completed'
    
    completed_question_numbers = []
    not_completed_question_numbers = []
    for k, v in all_questions_dict.items():
        if v['status'] == 'completed':
            completed_question_numbers.append(k)
        else:
            not_completed_question_numbers.append(k)

    return completed_question_numbers, not_completed_question_numbers

if __name__=="__main__":
    completed_question_numbers, not_completed_question_numbers = check_completion()
    print(f"Completed questions numbers: {', '.join(str(num) for num in completed_question_numbers)}")
    print(f"Not Completed questions numbers: {', '.join(str(num) for num in not_completed_question_numbers)}")






    