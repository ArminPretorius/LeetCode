class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """

        remainder_count = [0] * k

        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1

        for i in range(1, (k // 2) + 1):
            if i == k - i:
                if remainder_count[i] % 2 != 0:
                    return False
            else:
                if remainder_count[i] != remainder_count[k - i]:
                    return False

        return remainder_count[0] % 2 == 0
