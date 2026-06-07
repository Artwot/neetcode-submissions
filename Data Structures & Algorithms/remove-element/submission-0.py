class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val == nums[len(nums) - 1]:
            nums[len(nums) - 1] = -1
        for i in range(len(nums)):
            if nums[i] == val:
                j = i
                for j in range(len(nums) - 1):
                    nums[j] = nums[j + 1]
        print(nums)
        k: int = len(nums)
        return k