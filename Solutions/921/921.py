class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        missed = 0
        for x in s:
            if x == "(":
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    missed += 1
        return count+missed
