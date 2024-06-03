class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s[::-1].split()[0]
        return len(word)