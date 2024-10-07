class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        bRem = False
        while bRem == False:
            oldLen = len(s)
            s = s.replace("AB","")
            s = s.replace("CD","")
            if oldLen == len(s):
                bRem = True

        return len(s)
