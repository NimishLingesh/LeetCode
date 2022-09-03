class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = self.stack_op(s)
        t_stack = self.stack_op(t)
        if s_stack == t_stack:
            return True
        return False
    
    def stack_op(self, s):
        s_stack = []
        for ch in s:
            if ch == "#" and len(s_stack) == 0:
                continue
            elif ch == "#":
                s_stack.pop()
            else:
                s_stack.append(ch)
        return s_stack

sol = Solution()
s = "ab#"
t = "ad#c"
print(sol.backspaceCompare(s, t))