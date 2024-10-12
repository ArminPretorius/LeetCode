class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        events = defaultdict(int)

        for interval in intervals:
            events[interval[0]] += 1
            events[interval[1]+1] -= 1

        conCurInter = MaxConCurInter = 0

        for event_key in sorted(events.keys()):
            conCurInter += events[event_key]
            MaxConCurInter = max(conCurInter,MaxConCurInter)
            
        return MaxConCurInter
        