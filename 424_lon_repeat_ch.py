class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # max_cnt = k
        # for idx, ch in enumerate(s):
        #     l, r = idx, idx
        #     k_inner = k
        #     while l >=0 and r < len(s) and k_inner > 0:
        #         if s[l] != ch and s[r] != ch:
        #             k_inner += 2
        #             if k_inner < 1:
        #                 max_cnt = max(max_cnt, r-l+1)
        #                 break
        #         elif s[l] != ch:
        #             k_inner += 1
        #         elif s[r] != ch:
        #             k_inner += 1
        #         l -= 1
        #         r += 1
        #     max(max_cnt, r-l+1)
        # print(max_cnt)

        ##############
        # visited = []
        # max_cnt = k
        # for idx, ch in enumerate(s):
        #     # if ch not in visited:
        #     visited.append(ch)
        #     k_inner = k
        #     itr = idx
        #     cnt = 0
        #     while itr < len(s) and k_inner > 0:
        #         if s[itr] != ch:
        #             k_inner -= 1
        #         cnt += 1
        #         itr += 1
        #     max_cnt = max(max_cnt, cnt)
        # return max_cnt

        ################ DIDNT RUN ALL THE TEST CASES #############

        # # sliding window approach
        # l, r = 0, 0
        # ch_cnt = {}
        # max_repeat = 0
        # # for l in range(len(s)):
        # #     for r in range(l, len(s)):

        # while r<len(s):
        #     if s[r] not in ch_cnt.keys():
        #         ch_cnt[s[r]] = 1
        #     else:
        #         ch_cnt[s[r]] += 1
        #     sub_len = r-l+1
        #     max_cnt = max(ch_cnt.values())
        #     k_len = sub_len-max_cnt
        #     # import pdb
        #     # pdb.set_trace()
        #     if k_len > k:
        #         l = r
        #         r = 0
        #         ch_cnt = {}
        #     max_repeat = max(max_repeat, max_cnt + k_len)
        #     r += 1
        # # decrement the cnt in the sliding the ch_cnt dictionary
        # print(ch_cnt)
        # while l < len(s):
        #     ch_cnt[s[l]] -= 1
        #     l += 1
        #     sub_len = r-l+1
        #     max_cnt = max(ch_cnt.values())
        #     k_len = sub_len-max_cnt
        #     if k_len > k:
        #         break
        #     max_repeat = max(max_repeat, max_cnt + k_len)
            
        # # print(ch_cnt)
        

        # return max_repeat

        ###################### CORRECT SOLUTION #################
        



sol = Solution()
s = "AABABBA"
k = 1
print(sol.characterReplacement(s, k))