class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longest= 0 
        for n in nset:
            if (n-1) not in nset:
                length = 1
                while (n+length) in nset:
                    length += 1
                longest = max(longest,length)
        return longest