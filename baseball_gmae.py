class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        lst = []
        for op in ops:
            if op == "+":
                lst.append(lst[-1] + lst[-2])
            elif op == "D":
                lst.append(2 * lst[-1])
            elif op == "C":
                lst.pop()
            else:
                lst.append(int(op))
        return sum(lst)


sol = Solution()
ops = ["5", "2", "C", "D", "+"]
print(sol.calPoints(ops))
