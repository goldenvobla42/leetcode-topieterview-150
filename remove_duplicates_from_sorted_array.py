def removeDuplicates(self, nums: List[int]) -> int:
    new_array = set(nums)
    nums.clear()
    for i in new_array:
        if i not in nums:
            nums.append(i)
        nums.sort()
    return len(nums)
