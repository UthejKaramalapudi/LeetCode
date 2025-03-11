class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = 0

        for i, char in enumerate(word):
            if char in vowels:
                res += (i+1)*(n-i)

        return res
