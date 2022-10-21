class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # print(set(sentence))
        return len(set(sentence)) == 26