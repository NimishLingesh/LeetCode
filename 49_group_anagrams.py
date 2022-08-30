from re import S


class Solution:
    def groupAnagrams(self, strs):
        # if len(strs) < 2:
        #     return [strs]

        # main_dict = {}
        # # for st in strs:
        # #     ch_cnt = {}
        # #     for ch in st:
        # #         ch_cnt[ch] = 1 + ch_cnt.get(ch, 0)
        # #     if ch_cnt in main_dict.values():

        # for st in strs:
        #     st_sorted = sorted(st)
        #     print(st_sorted)
        #     if st_sorted in main_dict.keys():
        #         main_dict[st_sorted].append(st)
        #     else:
        #         main_dict[st_sorted] = [st]
        # print(main_dict)
        # return main_dict.values() 

        import collections
        res = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            print(count)
            res[tuple(count)].append(s)
        print(res)
        return res.values()

sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
res = sol.groupAnagrams(strs)
# print(res)
