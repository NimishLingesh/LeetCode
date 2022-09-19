class Solution:
    def findOriginalArray(self, changed):
        # visited = []
        # changed = sorted(changed)
        # res = []
        # for ele in changed:
        #     if ele*2 in visited:
        #         res.append(int(ele))
        #         visited.pop(visited.index(ele*2))
        #     elif int(ele/2) in visited:
        #         res.append(int(ele/2))
        #         visited.pop(visited.index(int(ele/2)))
        #     else:
        #         visited.append(ele)
        #     print(visited)
        # print("res", res)
        # if len(res) == len(changed)/2:
        #     return res
        # else:
        #     return []

        """
        if len(changed)%2 == 1:
            return []
        changed = sorted(changed)
        first_half = changed[:len(changed)//2]
        second_half = changed[len(changed)//2:]
        print(first_half)
        print(second_half)
        """
        if len(changed)%2 == 1:
            return []
        res = []
        changed1 = changed.copy()
        changed = sorted(changed)
        i = 0
        while i < len(changed1):
            i += 1
            num = changed[0]
            idx = changed[1:].index(num*2)
            if idx:
                changed.pop(idx)
                res.append(changed.pop(0))
            else:
                continue
        if len(res) == len(changed1)//2:
            return res
        else:
            return []

sol = Solution()
changed = [4,4,16,20,8,8,2,10]
print(sol.findOriginalArray(changed))