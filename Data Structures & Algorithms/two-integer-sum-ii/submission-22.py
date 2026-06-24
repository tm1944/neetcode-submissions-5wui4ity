class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        while l < r:
            nsum = numbers[l]+numbers[r]
            if nsum > target:
                r-=1
            elif nsum < target:
                l+=1
            else:
                return [l+1,r+1]
        