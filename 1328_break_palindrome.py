class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            return ""
        temp = 0
        st_len = len(palindrome)//2
        for idx in range(st_len):
            if palindrome[idx] != "a":
                palindrome = palindrome[:idx] + "a" + palindrome[idx+1:]
                return palindrome
        return palindrome[:-1] + "b"