class Solution:
    def palindromePairs(self, words):
        wordict = {}
        res = [] 
        for i in range(len(words)):
            wordict[words[i]] = i
        for i in range(len(words)):
            # Iterate through rach of the ch in the word 
            for j in range(len(words[i])+1):
                tmp1 = words[i][:j]
                tmp2 = words[i][j:]

                # dividing the word into two parts, check if the reverse of the first 
                # part exists in the dict and the the presence of the palindrome of the next part of the word
                if tmp1[::-1] in wordict and wordict[tmp1[::-1]]!=i and tmp2 == tmp2[::-1]:
                    res.append([i,wordict[tmp1[::-1]]])
                if j!=0 and tmp2[::-1] in wordict and wordict[tmp2[::-1]]!=i and tmp1 == tmp1[::-1]:
                    res.append([wordict[tmp2[::-1]],i])
                    
        return res
    """
    My solution, time exceeds in some test cases
        res = []
        for idx, i in enumerate(words):
            for idx_2 in range(idx+1, len(words)):
                is_pali = self.check_pali(words[idx] + words[idx_2])
                if is_pali and [idx, idx_2] not in res:
                    res.append([idx, idx_2])
                is_pali = self.check_pali(words[idx_2] + words[idx])
                if is_pali and [idx_2, idx] not in res:
                    res.append([idx_2, idx])
        return list(res)
        
    def check_pali(self, st):
        if st[0] != st[-1]:
            return False
        if len(st)%2 == 1:
            if st[0:len(st)//2] == st[len(st)-1:len(st)//2:-1]:
                return True
            else:
                return False
        else:
            if st[0:len(st)//2] == st[len(st)-1:len(st)//2-1:-1]:
                return True
            else:
                return False
    """

sol = Solution()
words = ["abcd","dcba","lls","s","sssll"]
print(sol.palindromePairs(words))