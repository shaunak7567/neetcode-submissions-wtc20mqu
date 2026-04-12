class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countmap={}
        counter=0
        for num in nums:
            if num in countmap:
                return True
            countmap[num]=1
        return False
                 
                

