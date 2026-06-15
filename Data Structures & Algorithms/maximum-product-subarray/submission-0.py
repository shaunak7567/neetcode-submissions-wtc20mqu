class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # 0 -> [-1]
        curMin, curMax = 1,1 
        for n in nums:
            if n == 0:
                curMin, curMax = 1,1
                continue
            tmp = curMax *n
            curMax = max(tmp, n * curMin,n)
            curMin = min(tmp, n * curMin,n)
            res = max(res,curMax, curMin)
        return res

        # Time complexity O(n)
        # Mem Comlexity O(1)



