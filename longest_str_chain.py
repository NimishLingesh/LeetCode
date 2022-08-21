class Solution:
    def longestStrChain(self, words):
        max_count = 0
        count = 1
        while len(words)>1:
            tmp1 = min(words, key=len)
            words.remove(tmp1)    
            tmp2 = min(words, key=len)
            # import pdb
            # pdb.set_trace()
            if self.check_sub_str(tmp1, tmp2) and len(tmp2) == len(tmp1) + 1:
                count += 1
                # if len(words) == 1:
                #     count += 1
                #     break
            else:
                # words.remove(min(words))
                if count>max_count:
                    max_count = count
                count = 1
        print(words)
        if count>max_count:
            return count
        else:
            return max_count+1

    def check_sub_str(self,s1, s2):
        val = True
        for ch in s1:
            if ch in s2:
                continue
            else:
                val = False
        return val
        
sol = Solution()
words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
print(sol.longestStrChain(words))
