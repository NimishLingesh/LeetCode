class Solution:
    def countBits(self, n):
        # self.num_to_binary(n)
        # print(self.binary)
        # return self.num_of_ones()
        l = []
        for num in range(0, n + 1):
            self.binary = ""
            self.count = 0
            self.num_to_binary(num)
            # cnt = self.num_of_ones()
            l.append(self.count)
        return l

    def num_to_binary(self, num):
        self.binary = ""
        if num >= 1:
            self.num_to_binary(num / 2)
        rem = num % 2
        self.binary += str(rem)
        if rem == 1:
            self.count += 1

    # def num_of_ones(self):
    #     count = 0
    #     for i in self.binary:
    #         if i == "1":
    #             count += 1
    #     return count


sol = Solution()
num = 16
lis = sol.countBits(num)
print(lis)
