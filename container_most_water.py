class Solution:
    def maxArea(self, height) -> int:
        # max = 0
        # n = len(height)
        # i_pos = 0
        # for i in height[:-1]:
        #     count = 0
        #     for j in height[i_pos + 1 :]:
        #         count += 1
        #         base = count
        #         ht = min(i, j)
        #         area = base * ht
        #         if area > max:
        #             max = area
        #     i_pos += 1
        # return max

        # max_val = 0
        # i = 0
        # j = 0
        # while i < len(height):
        #     if j >= i:
        #         i += 1
        #         j = 0
        #         if i >= len(height):
        #             break
        #     base = i - j
        #     max_val = max(max_val, (i - j) * min(height[i], height[j]))
        #     j += 1
        # return max_val

        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res


sol = Solution()
height = [1, 1]
val = sol.maxArea(height)
print(val)
