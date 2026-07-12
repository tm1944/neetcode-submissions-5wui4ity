class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        maxf = 0
        hmap = {}
        for r in range(len(s)):
            hmap[s[r]] = 1 + hmap.get(s[r],0)
            maxf = max(hmap[s[r]],maxf)
            while ((r-l+1)) - maxf > k:
                hmap[s[l]] -=1
                l+=1
            res = max(res,r-l+1)
        return res