class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_map = {}
        for idx, i in enumerate(s):
            if i not in dic_map.keys() and t[idx] not in dic_map.values():
                dic_map[i] = t[idx]
            else:
                if dic_map.get(i) != t[idx]:
                    return False
        print(dic_map)
        # for idx, i in enumerate(s):
        #     if dic_map[i] != t[idx]:
        #             return False
        return True
        

sol = Solution()
s = "badc"
t = "baba"
print(sol.isIsomorphic(s, t))