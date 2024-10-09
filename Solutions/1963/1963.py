class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = 0
        for i in s:
            if i == '[':
                x += 1
            elif x > 0:
                x -= 1
        return (x + 1) // 2
