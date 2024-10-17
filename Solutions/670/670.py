class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        n = len(num_str)

        last_seen = [-1] * 10

        for x in range(n):
            last_seen[int(num_str[x])] = x

        #print(last_seen)

        for x in range(n):
            for y in range(9, int(num_str[x]),-1):
                if last_seen[y] > x:
                    num_str = list(num_str)
                    num_str[x], num_str[last_seen[y]] = num_str[last_seen[y]], num_str[x]
                    num_str = "".join(num_str)
                    return int(num_str)
        return num