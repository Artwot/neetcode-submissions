class Solution {
  int findMaxConsecutiveOnes({required List<int> nums}) {
    int currentStreak = 0;
    int bestStrak = 0;
    for (int num in nums) {
      if (num == 1) {
        currentStreak += 1;
        if (bestStrak < currentStreak) {
          bestStrak = currentStreak;
        }
      } else {
        currentStreak = 0;
      }
    }
    return bestStrak;
  }
}
