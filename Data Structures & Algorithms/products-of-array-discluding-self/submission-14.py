class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pfix = 1
        for i in range(len(nums)):
            res[i] = pfix
            pfix *= nums[i]
        pofix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= pofix
            pofix *= nums[i]
        return res