class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for s in s1:
            count1[s] = 1 + count1.get(s,0)
        need = len(count1)
        for i in range(len(s2)):
            count2,win = {},0
            for j in range(i,len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j],0)
                if count1.get(s2[j],0) < count2[s2[j]]:
                    break
                if count1.get(s2[j],0) == count2[s2[j]]:
                    win+=1
                if win == need:
                    return True
        return False
