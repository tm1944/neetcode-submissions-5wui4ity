class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nset = set(nums)
        for n in nset:
            if (n-1) not in nset:
                length = 1
                while (n+length) in nset:
                    length+=1
                longest = max(length,longest)
        return longest