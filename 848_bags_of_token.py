class Solution:
    def bagOfTokensScore(self, tokens, power) -> int:
        i = 0
        j = len(tokens) - 1
        score = 0
        tokens = sorted(tokens)
        while i<=j:
            if power>=tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
            elif score > 0 and j-i > 1:
                power += tokens[j]
                j -= 1
                score -= 1
            else:
                break
        return score

sol = Solution()
tokens = [81, 91, 31]
power = 73
print(sol.bagOfTokensScore(tokens, power))