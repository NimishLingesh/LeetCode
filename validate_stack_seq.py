class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # stack = []
        # # i = 0
        # for ele in pushed:
        #     if ele == popped[0]:
        #         stack.append(ele)
        #         stack.pop()
        #         # i += 1
        #         popped.pop(0)
        #     else:
        #         stack.append(ele)
        # print(popped)
        # print(stack)
        # if len(stack) != 0:
        #     if popped[0] == stack[0]:
        #         stack.pop()
        #         popped.pop()
        # for ele in popped:
        #     if ele == stack[-1]:
        #         stack.pop()

        # if len(stack) == 0:
        #     return True
        # else:
        #     return False

        # working solution
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)


sol = Solution()
pushed = [2, 1, 0]
popped = [1, 2, 0]
resp = sol.validateStackSequences(pushed, popped)
print(resp)
