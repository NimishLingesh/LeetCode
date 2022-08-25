import collectionsß

class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ####### solution as per discussionß

        total_count = 0
        
        for index, count in enumerate(sorted(collections.Counter(arr).values(), reverse=True)):
            total_count += count
            
            if total_count >= len(arr) // 2:
                return index + 1
        
        return 0

        ###################### my code - doesnt work completely (time limit exceeds )

        dict_cnt = {}
        a_size = len(arr)
        for i in arr:
            if i in dict_cnt.keys():
                dict_cnt[i] += 1
            else:
                dict_cnt[i] = 1 
        # arr_cnt = list(dict_cnt.values()).sort()
        dict_val = list(dict_cnt.values())
        dict_val.sort(reverse=True)
        print(dict_val)
        num_len = 0
        sum = 0
        
        
        if len(dict_cnt.items()) == a_size:
            return a_size//2
        for i in dict_val:
            if sum >= a_size/2:
                return num_len
            sum += i
            num_len += 1
        return 1

sol = Solution()
arr = [3,3,3,3,5,5,5,2,2,7]
arr2 = [1,2,3,4,5,6,7,8,9,10]
print(sol.minSetSize(arr2))
