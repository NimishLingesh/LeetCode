class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        hash_ch = {}
        for idx, ch in enumerate(s):
            hash_ch[ch] = idx
        size = 0
        window = 0
        for idx, ch in enumerate(s):
            size += 1
            if hash_ch[ch]>window:
                window = hash_ch[ch]
            if idx == window:
                res.append(size)
                size = 0
        if size>0:
            res.append(size)
        return res
            