class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        events = []
        AvailChairs = list(range(len(times)))
        OccChairs = []
    
        for i in range(len(times)):
            events.append([times[i][0],i])
            events.append([times[i][1],~i])
    
        events.sort()
    
        for event in events:
            time,friend = event
    
            while (OccChairs and time >= OccChairs[0][0]):
                _,chair = heapq.heappop(OccChairs)
                heapq.heappush(AvailChairs,chair)
            
            if friend >= 0:
                chair = heapq.heappop(AvailChairs)
                if friend == targetFriend:
                    return chair
                heapq.heappush(OccChairs,[times[friend][1], chair])
        return -1