class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for x in s:
            if x == "(":
                stack.append("()")
            elif x == ")":
                if len(stack) == 0:
                    return False
                elif stack[len(stack)-1] == "()":
                    del stack[len(stack)-1]
                else:
                    return False
            elif x == "[":
                stack.append("[]")
            elif x == "]":
                if len(stack) == 0:
                    return False
                elif stack[len(stack)-1] == "[]":
                    del stack[len(stack)-1]
                else:
                    return False
            elif x == "{":
                stack.append("{}")
            elif x == "}":
                if len(stack) == 0:
                    return False
                elif stack[len(stack)-1] == "{}":
                    del stack[len(stack)-1]
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
