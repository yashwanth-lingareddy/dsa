'''

Given a set of activities, along with the starting and finishing time of each activity, find the maximum number of activities performed by a single person assuming that a person can only work on a single activity at a time.

Input : [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: {(1, 4), (5, 7), (8, 11), (12, 14)}

Input : [(3, 7), (1, 3), (2, 9), (2, 7), (1, 2), (7, 8)]
Output: {(1, 3), (3, 7), (7, 8)} or {(1, 2), (3, 7), (7, 8)} or {(1, 2), (2, 7), (7, 8)}

'''

from typing import List, Set, Tuple

def select_activity(activities: List[Tuple[int]]):
    selected_activities = set()
    if len(activities) == 0:
        return selected_activities
    if len(activities) == 1:
        selected_activities.add(activities[0])
        return selected_activities
    sorted_tuples = sorted(activities, key=lambda x: x[1])
    selected_activities.add(sorted_tuples[0])
    previous_end_time = sorted_tuples[0][1]
    for i in range(1, len(sorted_tuples)):
        this_activity = sorted_tuples[i]
        this_start_time = this_activity[0]
        if this_start_time >= previous_end_time:
            selected_activities.add(this_activity)
            previous_end_time = this_activity[1]
    return selected_activities

if __name__=="__main__":
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    ans = select_activity(activities=activities)
    print(ans)