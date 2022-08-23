class Solution:
    def min_glass(self, n, k):
        glass_heap = list(range(1, n+1))
        glass_heap.reverse()
        sum = 0

        heap_lst = []
        # min_cnt = n
        cnt = 0
        # print(glass_heap)
        for i in glass_heap:
            # import pdb
            # pdb.set_trace()
            if sum == k:
                if cnt < min_cnt:
                    min_cnt = cnt
            elif sum > k:
                # backtrack
                import pdb
                pdb.set_trace()
                ele = heap_lst.pop(len(heap_lst)-1)
                sum -= ele
                cnt -= 1
            elif sum < k:
                cnt += 1
                sum += i
                heap_lst.append(i)
        
        return min_cnt

    # def helper(self, heap_lst):


sol = Solution()
n = 5
k = 8
print(sol.min_glass(n, k))

# 5
# 3 2 1
#   1 2
