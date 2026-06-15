class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums), -1,-1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    LIS[i] = max(LIS[i], 1 +LIS[j])
        return max(LIS)

        # O(n^2) - since each visited value is visited multiple times when goin in reverse order