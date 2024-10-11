# 1942. The Number of the Smallest Unoccupied Chair
## Index
- [Python](/Solutions/1942/README.md#python)
- [C#](/Solutions/1942/README.md#c)
- [Java](/Solutions/1942/README.md#java)

## Python
#### Solution Code
```py
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
```
#### Breakdown
Declare events (all sitting down and getting up events), AvailChairs (available chairs) and OccChairs (occupied chairs). Assign max possible available chairs to AvailChairs.
```py
events = []
AvailChairs = list(range(len(times)))
OccChairs = []
```
Populate events list by appending all sitting and getting up time with a corresponding friend index, make the index the inverse if they are getting up.
```py
for i in range(len(times)):
    events.append([times[i][0],i])
    events.append([times[i][1],~i])
```
Sort events to be in order.
```py
events.sort()
```
Loop through events and assigns time to the time of the event and friend to the friend index of the event.

Use a while loop to check if the OccChairs are empty and if time is bigger than or equal to the time of the oldest OccChairs item, it then pops out all the OccChairs that are not occupied anymore and pushes them into AvailChairs again.

Use an if to check if the friend index is bigger than or equal to 0 (Friend is coming to sit down). Pop the next chair from AvailChairs as it is no longer available, and check if the friend is the target friend, if the friend is, return the chair. Otherwise push the time of the event and the chair into OccChairs
```py
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
```
Return -1 as a backup, but the code should not reach it.
```py
return -1
```
## C#
#### Solution Code
```cs
public class Solution {
    public int SmallestChair(int[][] times, int targetFriend) {
        List<(int, int, int)> events = new List<(int, int, int)>();
        PriorityQueue<int, int> AvailChairs = new PriorityQueue<int, int>();
        PriorityQueue<(int, int), int> OccChairs = new PriorityQueue<(int, int), int>();

        for (int i = 0; i < times.Length; i++)
            AvailChairs.Enqueue(i, i);

        for (int i = 0; i < times.Length; i++)
            events.Add((times[i][0], times[i][1], i));

        events = events.OrderBy(t => t.Item1).ThenBy(t => t.Item2).ToList();

        for (int i = 0; i < events.Count; i++)
        {
            while (OccChairs.Count > 0 && events[i].Item1 >= OccChairs.Peek().Item1)
            {
                AvailChairs.Enqueue(OccChairs.Peek().Item2, OccChairs.Peek().Item2);
                OccChairs.Dequeue();
            }
            if (events[i].Item3 == targetFriend) return AvailChairs.Dequeue();
            OccChairs.Enqueue((events[i].Item2, AvailChairs.Dequeue()), events[i].Item2);
        }
        return -1;
    }
}
```
#### Breakdown
Declare events (all sitting down and getting up events), AvailChairs (available chairs) and OccChairs (occupied chairs).
```cs
List<(int, int, int)> events = new List<(int, int, int)>();
PriorityQueue<int, int> AvailChairs = new PriorityQueue<int, int>();
PriorityQueue<(int, int), int> OccChairs = new PriorityQueue<(int, int), int>();
```
Assign max possible available chairs to AvailChairs.
```cs
for (int i = 0; i < times.Length; i++)
    AvailChairs.Enqueue(i, i);
```
Populate events list by appending all sitting and getting up time with a corresponding friend index.
```cs
for (int i = 0; i < times.Length; i++)
    events.Add((times[i][0], times[i][1], i));
```
Sort events to be in order.
```cs
events = events.OrderBy(t => t.Item1).ThenBy(t => t.Item2).ToList();
```
Loop through events.

Use a while loop to check if the OccChairs are empty and if time is bigger than or equal to the time of the oldest OccChairs item, it then enqueues into AvailChairs, with the values from OccChairs and then dequeues the item from OccChairs.

Check if the friend is the target friend, if the friend is, return the chair. Otherwise enqueue the dequeued chair of AvailChair on OccChair.
```cs
for (int i = 0; i < events.Count; i++)
{
    while (OccChairs.Count > 0 && events[i].Item1 >= OccChairs.Peek().Item1)
    {
        AvailChairs.Enqueue(OccChairs.Peek().Item2, OccChairs.Peek().Item2);
        OccChairs.Dequeue();
    }
    if (events[i].Item3 == targetFriend) return AvailChairs.Dequeue();
    OccChairs.Enqueue((events[i].Item2, AvailChairs.Dequeue()), events[i].Item2);
}
```
Return -1 as a backup, but the code should not reach it.
```cs
return -1;
```
## Java
#### Solution Code
```java
class Solution {
    public int smallestChair(int[][] times, int targetFriend) {
        List<int[]> events = new ArrayList<>();
        PriorityQueue<Integer> availChairs = new PriorityQueue<>();
        PriorityQueue<int[]> occChairs = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        for (int i = 0; i < times.length; i++) {
            events.add(new int[]{times[i][0], i});
            events.add(new int[]{times[i][1], ~i});
        }

        Collections.sort(events, (a, b) -> a[0] - b[0]);

        for (int i = 0; i < times.length; i++) {
            availChairs.add(i);
        }

        for (int[] event : events) {
            int time = event[0];
            int friend = event[1];

            while (!occChairs.isEmpty() && occChairs.peek()[0] <= time) {
                availChairs.add(occChairs.poll()[1]);
            }

            if (friend >= 0) {
                int chair = availChairs.poll();
                if (friend == targetFriend)
                    return chair;
                occChairs.add(new int[]{times[friend][1], chair});
            }
        }
        return -1;
    }
}
```
#### Breakdown
Declare events (all sitting down and getting up events), availChairs (available chairs) and occChairs (occupied chairs).
```java
List<int[]> events = new ArrayList<>();
PriorityQueue<Integer> availChairs = new PriorityQueue<>();
PriorityQueue<int[]> occChairs = new PriorityQueue<>((a, b) -> a[0] - b[0]);
```
Populate events list by appending all sitting and getting up time with a corresponding friend index, make the index the inverse if they are getting up.
```java
for (int i = 0; i < times.length; i++) {
    events.add(new int[]{times[i][0], i});
    events.add(new int[]{times[i][1], ~i});
}
```
Sort events to be in order.
```java
Collections.sort(events, (a, b) -> a[0] - b[0]);
```
Assign max possible available chairs to availChairs.
```java
for (int i = 0; i < times.length; i++) {
    availChairs.add(i);
}
```
Loop through events and assigns time to the time of the event and friend to the friend index of the event.

Use a while loop to check if the occChairs are empty and if time is bigger than or equal to the time of the oldest occChairs item, it then polls out all the occChairs items that are not occupied anymore and pushes them into availChairs again.

Use an if to check if the friend index is bigger than or equal to 0 (Friend is coming to sit down). Poll the next chair from availChairs as it is no longer available, and check if the friend is the target friend, if the friend is, return the chair. Otherwise push the time of the event and the chair into occChairs
```java
for (int[] event : events) {
            int time = event[0];
            int friend = event[1];

            while (!occChairs.isEmpty() && occChairs.peek()[0] <= time) {
                availChairs.add(occChairs.poll()[1]);
            }

            if (friend >= 0) {
                int chair = availChairs.poll();
                if (friend == targetFriend)
                    return chair;
                occChairs.add(new int[]{times[friend][1], chair});
            }
        }
```
Return -1 as a backup, but the code should not reach it.
```java
return -1;
```