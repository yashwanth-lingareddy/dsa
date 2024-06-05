'''

Given a list of tasks with deadlines and total profit earned on completing a task, find the maximum profit earned by executing the tasks within the specified deadlines. Assume that each task takes one unit of time to complete, and a task can't execute beyond its deadline.

Input: (Task Id, Deadline, Profit)

[(1, 9, 15), (2, 2, 2), (3, 5, 18), (4, 7, 1), (5, 4, 25), (6, 2, 20), (7, 5, 8), (8, 7, 10), (9, 4, 12), (10, 3, 5)]

Output: {1, 3, 4, 5, 6, 7, 8, 9}
Explanation: The maximum profit that can be achieved is 109 by leaving tasks 2 and 10 out.

Constraints:

• Only a single task can be executed at a time.
• The maximum number of tasks are 100.
• The maximum deadline that can be associated with a job is 1000.

'''
from typing import List, Set

class Job:
    def __init__(self, taskId, deadline, profit):
        self.taskId = taskId
        self.deadline = deadline
        self.profit = profit

    def __repr__(self):
        return f'({self.taskId}, {self.deadline}, {self.profit})'

    def __eq__(self, o: object) -> bool:
        return self.taskId == o.taskId and self.deadline == o.deadline and self.profit != o.profit

def schedule_jobs(jobs: List[Job]) -> Set[int]:
    # Write your code here...
    n = len(jobs)
    jobIds = set()
    if n == 0:
        return jobIds
    jobs.sort(key=lambda x: x.profit, reverse=True)  # Sort tasks by descending profit

    max_deadline = max(task.deadline for task in jobs)
    schedule = [-1] * (max_deadline + 1)  # Initialize schedule with -1 (no task scheduled)

    profit = 0
    
    for j in jobs:
        id = j.taskId
        deadline = j.deadline
        profit_value = j.profit
        for slot in range(deadline, 0, -1):
            if schedule[slot] == -1:
                schedule[slot] = profit_value
                profit += profit_value
                jobIds.add(id)
                break

    return jobIds

if __name__=="__main__":
    jobs = [
        Job(
            taskId=1,
            deadline=9,
            profit=15
        ),
        Job(
            taskId=2,
            deadline=2,
            profit=2
        ),
        Job(
            taskId=3,
            deadline=5,
            profit=18
        ),
        Job(
            taskId=4,
            deadline=7,
            profit=1
        ),
        Job(
            taskId=5,
            deadline=4,
            profit=25
        ),
        Job(
            taskId=6,
            deadline=2,
            profit=20
        ),
        Job(
            taskId=7,
            deadline=5,
            profit=8
        ),
        Job(
            taskId=8,
            deadline=7,
            profit=10
        ),
        Job(
            taskId=9,
            deadline=4,
            profit=12
        ),
        Job(
            taskId=10,
            deadline=3,
            profit=5
        )
    ]

    ans = schedule_jobs(jobs=jobs)
    print(ans)