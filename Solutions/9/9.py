class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        sint = str(x)
        if sint[::-1] == sint:
            return True
        else:
            return False
