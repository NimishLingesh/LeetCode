class Solution:
    def numberOfWeakCharacters(self, properties) -> int:
        # properties = sorted(properties)
        # print(properties)
        # res = 0
        # for idx, game in enumerate(properties):
        #     # import pdb 
        #     # pdb.set_trace()
        #     for j_num in range(idx+1,len(properties)):
        #         other_game = properties[j_num]
        #         if other_game[0] > game[0] and other_game[1] > game[1]:
        #             res += 1
        #             break
        properties = sorted(properties)
        print(properties)
        res = 0
        len_p = len(properties)
        for idx, game in enumerate(properties):
            # import pdb 
            # pdb.set_trace()
            for j_num in range(len_p-1, idx, -1):
                other_game = properties[j_num]
                if other_game[0] > game[0] and other_game[1] > game[1]:
                    res += 1
                    break
        return res


sol = Solution()
properties = [[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]]
print(sol.numberOfWeakCharacters(properties))