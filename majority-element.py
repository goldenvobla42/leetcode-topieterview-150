class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        majorityElement = nums[n // 2]
        return majorityElement

