class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        # max = 1
        max_of_all = 1
        for i in range(0,len(s)-max_of_all):
            sub_str = ""
            sub_str = s[i]
            max = 1
            for j in range(i+1,len(s)):
                if s[j] not in sub_str:
                    sub_str += s[j]
                    max += 1
                else:
                    if max > max_of_all:
                        max_of_all = max
                    break
            if max > max_of_all:
                max_of_all = max
        # print(sub_str)
        return max_of_all
        

if __name__ == "__main__":
    obj = Solution()
    resp = obj.lengthOfLongestSubstring("aabc")
    print(resp)
        