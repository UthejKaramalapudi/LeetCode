class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_count = {}
        res = 0
        l = 0
        n = len(s)

        for r in range(n):
            if s[r] in char_count:
                char_count[s[r]] += 1
            else:
                char_count[s[r]] = 1

            while len(char_count) == 3:
                res += (n - r)
                char_count[s[l]] -= 1

                if char_count[s[l]] == 0:
                    del char_count[s[l]]

                l += 1

        return res
