class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps1 = 1
        steps2 = 1
        for i in range(n - 1):
            temp = steps1
            steps1 = steps1 + steps2
            steps2 = temp
        return steps1