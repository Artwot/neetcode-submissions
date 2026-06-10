class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k: int = 0
        for num in nums:
            if num != val:
                k += 1
                nums[k - 1] = num

        return k
