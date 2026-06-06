class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0
        best_streak = 0
        for num in nums:
            if num == 1:
                current_streak += 1
                if best_streak < current_streak:
                    best_streak = current_streak
            else:
                current_streak = 0

        return best_streak
