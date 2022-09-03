class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a_cnt = 0
        bulls = {}
        for idx, ch in enumerate(secret):
            if ch == guess[idx]:
                a_cnt += 1
                bull_ch = ch
            if ch not in bulls.keys():
                bulls[ch] = 1
            else:
                bulls[ch] += 1
        
        cows = {}
        cows_cnt = 0
        for ch in guess:
            if ch not in cows.keys():
                cows[ch] = 1
            else:
                cows[ch] += 1

        total_bulls = 0

        for bull in bulls:
            if bull in cows.keys():
                total_bulls += min(bulls[bull], cows[bull])

        print(bulls)
        print(cows)

        cows_cnt = total_bulls - a_cnt
        return str(a_cnt) + "A" + str(cows_cnt) + "B"

            

sol = Solution()
secret = "1807"
guess = "7810"
print(sol.getHint(secret, guess))