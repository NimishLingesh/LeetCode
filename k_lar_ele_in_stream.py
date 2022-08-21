from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums_list = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums_list.append(val)
        self.nums_list.sort()
        return self.nums_list[-self.k]


obj = KthLargest(3, [4, 5, 8, 2])
inp = [3, 5, 10, 9, 4]
for ele in inp:
    print(obj.add(ele))
