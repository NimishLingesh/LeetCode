from re import L


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        t_dict = {}
        for task in tasks:
            if t_dict.get(task):
                t_dict[task] += 1
            else:
                t_dict[task] = 1
        task_list = t_dict.keys()
        

sol = Solution()
tasks = ["A","A","A","B","B","B"]
n = 2
print(sol.leastInterval(tasks, n))