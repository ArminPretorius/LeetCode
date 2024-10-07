class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        px = ""
        for x in s:
            if x == "I":
                num+=1
            elif x == "V":
                if px == "I":
                    num+=4-1
                else:
                    num+=5
            elif x == "X":
                if px == "I":
                    num+=9-1
                else:
                    num+=10
            elif x == "L":
                if px == "X":
                    num+=40-10
                else:
                    num+=50
            elif x == "C":
                if px == "X":
                    num+=90-10
                else:
                    num+=100
            elif x == "D":
                if px == "C":
                    num+=400-100
                else:
                    num+=500
            elif x == "M":
                if px == "C":
                    num+=900-100
                else:
                    num+=1000
            px = x
        return num
