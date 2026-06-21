class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0
        l,r = 1,max(piles)

        while l <= r:
            k = l +((r-l)//2)
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/k)
            
            if h >= totalTime:
                r = k -1 
                res = k
            else:
                l = k + 1
        return res