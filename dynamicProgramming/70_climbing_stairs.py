class Solution(object):
    # def __init__(self):
    #     # self.n_sum = 0
    #     self.total_cnt = 0

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # self.n_sum = n
        return self.recurse_1(n)
        # return self.total_cnt

    # def recurse(self, local_n):
    #     if local_n == 0:
    #         self.total_cnt += 1
    #         return
    #     self.recurse(local_n-1)
    #     self.recurse(local_n-1)

    def recurse_1(self, n):
        if n == 2 or n == 1:
            return n
        return self.recurse_1(n-1) + self.recurse_1(n-2)


# SAME AS FIBONACCI SERIES
# ALTERNATE SOLUTION
 # just a fibonacci series
        # one, two = 1,1      
        # for i in range(n-1):
        #     temp = two
        #     two = one + two
        #     one = temp
        # return two

        

sol = Solution()
n = 5
print(sol.climbStairs(n))