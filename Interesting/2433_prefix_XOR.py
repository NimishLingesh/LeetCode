class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        XOR = 0
        for idx, i in enumerate(pref):
            pref[idx] = XOR^i
            XOR = 0^i
        return pref
        
