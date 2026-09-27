from functools import lru_cache

class Solution:

    @lru_cache
    def climbStairs(self, n: int) -> int:
        match n:
            case 1:
                return 1
            case 2:
                return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)