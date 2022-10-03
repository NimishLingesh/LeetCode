from asyncio.constants import ACCEPT_RETRY_DELAY


class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        if len(arr) == 0:
            return []
        if x in arr:
            idx = arr.index(x)
        else:
            idx = self.find_idx(arr, x)
        res = [arr[idx]]
        x -= 1
        i = idx - 1
        j = idx + 1
        if j>len(arr)-1:
            res = arr[idx-k+1:idx+1]
            return res
        elif i<0:
            res = arr[idx:idx+k+1]
            return res

        while i>=0 and j<len(arr) and x>=0:
            i_val = abs(arr[i]-x)
            j_val = abs(arr[j]-x)
            if i_val <= j_val:
                res.insert(0, arr[i])
                i -= 1
            elif i_val > j_val:
                res.append(arr[j])
                j += 1
            x -= 1
        
        if x>0:
            if i<0:
                res.extend(arr[j:j+x])
            elif j>=len(arr):
                new_arr = arr[i-x+1:i+1]
                new_arr.extend(res)
                res = new_arr
        return res
        # i = idx
        # while i >= 0 and k > 0:
        #     res.insert(0, arr[i])
        #     i -= 1
        #     k -= 1
        # # print(res)


        # j = idx + 1
        # while j < len(arr) and k > 0:
        #     # ifsontinue
        #     res.append(arr[j])
        #     k -= 1
        #     j += 1
        # return res

    def find_idx(self, arr, x):
        min_v = abs(arr[0] - x)
        idx = 0
        for id, num in enumerate(arr):
            if abs(arr[id] - x) < min_v:
                idx = id
        return idx
        

sol = Solution()
arr = [1,2,3,4,5]
k = 4
x = -1
print(sol.findClosestElements(arr, k, x))