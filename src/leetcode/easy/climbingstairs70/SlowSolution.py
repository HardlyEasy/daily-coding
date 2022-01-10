class SlowSolution:
    def climbStairs(self, n: int) -> int:
        return self.descend(n)

    def descend(self, current_n: int) -> int:
        """Work backwards to find total number of ways to climb
        """
        if current_n == 1:
            return 1
        elif current_n == 2:
            return 2
        else:
            return self.descend(current_n - 1) + self.descend(current_n - 2)
