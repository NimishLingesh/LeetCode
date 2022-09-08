from tkinter import N


class Solution:
    def topKFrequent(self, words, k: int):
        words = sorted(words)
        f_dict = {}
        for word in words:
            if word not in f_dict.keys():
                f_dict[word] = 1
            else:
                f_dict[word] += 1
        cnt_dict = {}
        for word, cnt in f_dict.items():
            if cnt not in cnt_dict.keys():
                cnt_dict[cnt] = [word]
            else:
                cnt_dict[cnt].append(word)
        
        # print(f_dict)
        # sorted(cnt_dict.keys())
        res = []
        i = 0
        print(cnt_dict)

        while i != k:
            # num = list(cnt_dict.keys())[-1]
            num = max(cnt_dict.keys())
            if len(cnt_dict[num]) <= (k-i):
                # cnt_dict[num].sort()
                for ele in cnt_dict[num]:
                    i += 1
                    res.append(ele)
                cnt_dict.pop(num)
            else:
                for j in range(k-i):
                    i += 1
                    res.append(cnt_dict[num][j])

        return res


sol = Solution()
words = ["i","love","leetcode","i","love","coding"]
k = 1
print(sol.topKFrequent(words, k))