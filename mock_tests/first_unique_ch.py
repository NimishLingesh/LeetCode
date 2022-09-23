class Solution:
    def unique_ch(self, s):
        s_dict = {}
        for ch in s:
            if ch not in s_dict:
                s_dict[ch] = 1
            else:
                s_dict[ch] += 1
        
        for key in s_dict:
            if s_dict[key] == 1:
                return key
        return -1

sol = Solution()
s = "staircasest"
print(sol.unique_ch(s))