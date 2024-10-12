# 2406. Divide Intervals Into Minimum Number of Groups
## Index
- [Python](/Solutions/2406/README.md#python)
- [C#](/Solutions/2406/README.md#c)
- [Java](/Solutions/2406/README.md#java)

## Python
#### Solution Code
```py
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
```
#### Breakdown
Declare dictionary to function as a timeline to see how many intervals are starting and ending at a given time.
```py
events = defaultdict(int)
```
Populate the dictionary by adding 1 when the interval is started and subtracting 1 after the ending time (because it is technically still there).
```py
for interval in intervals:
    events[interval[0]] += 1
    events[interval[1]+1] -= 1
```
Declare conCurInter (Concurrent Intervals) and maxConCurInter (Maximum Concurrent Intervals).
```py
conCurInter = MaxConCurInter = 0
```
Loop through the dictionary keys (ordered) and count all the concurrent intervals and assign new maximums if one is found.
```py
for event_key in sorted(events.keys()):
    conCurInter += events[event_key]
    MaxConCurInter = max(conCurInter,MaxConCurInter)
```
Return maxCunCurInter.
```py
return MaxConCurInter
``` 
## C#
#### Solution Code
```cs
public class Solution {
    public int MinGroups(int[][] intervals) {
        SortedDictionary<int, int> events = new SortedDictionary<int, int>();

        foreach (int[] interval in intervals)
        {
            if (events.ContainsKey(interval[0]))
                events[interval[0]] += 1;
            else
                events.Add(interval[0], 1);
            if (events.ContainsKey(interval[1]+1))
                events[interval[1]+1] -= 1;
            else
                events.Add(interval[1]+1, -1);
        }

        int conCurInter = 0;
        int maxConCurInter = 0;

        foreach (KeyValuePair<int,int> evnt in events)
        {
            conCurInter += evnt.Value;
            maxConCurInter = Math.Max(conCurInter, maxConCurInter);
        }

        return maxConCurInter;
    }
}
```
#### Breakdown
Declare sorted dictionary to function as a timeline to see how many intervals are starting and ending at a given time.
```cs
SortedDictionary<int, int> events = new SortedDictionary<int, int>();
```
Populate the dictionary by adding 1 when the interval is started and subtracting 1 after the ending time (because it is technically still there) and also check if the key was already declared to avoid errors.
```cs
foreach (int[] interval in intervals)
{
    if (events.ContainsKey(interval[0]))
        events[interval[0]] += 1;
    else
        events.Add(interval[0], 1);
    if (events.ContainsKey(interval[1]+1))
        events[interval[1]+1] -= 1;
    else
        events.Add(interval[1]+1, -1);
}
```
Declare conCurInter (Concurrent Intervals) and maxConCurInter (Maximum Concurrent Intervals).
```cs
int conCurInter = 0;
int maxConCurInter = 0;
```
Loop through the dictionary and count all the concurrent intervals and assign new maximums if one is found.
```cs
foreach (KeyValuePair<int,int> evnt in events)
{
    conCurInter += evnt.Value;
    maxConCurInter = Math.Max(conCurInter, maxConCurInter);
}
```
Return maxCunCurInter.
```cs
return maxConCurInter;
``` 
## Java
#### Solution Code
```java
class Solution {
    public int minGroups(int[][] intervals) {
        TreeMap<Integer,Integer> events = new TreeMap<>();

        for (int[] interval : intervals) {
            events.put(interval[0], events.getOrDefault(interval[0],0)+1);
            events.put(interval[1]+1, events.getOrDefault(interval[1]+1,0)-1);
        }

        int conCurInter = 0;
        int maxConCurInter = 0;

        for (Map.Entry<Integer,Integer> entry : events.entrySet()) {
            conCurInter += entry.getValue();
            maxConCurInter = Math.max(maxConCurInter, conCurInter);
        }

        return maxConCurInter;
    }
}
```
#### Breakdown
Declare sorted TreeMap to function as a timeline to see how many intervals are starting and ending at a given time.
```java
TreeMap<Integer,Integer> events = new TreeMap<>();
```
Populate the tree by adding 1 when the interval is started and subtracting 1 after the ending time (because it is technically still there) get a default if the key does not exist to avoid errors.
```java
for (int[] interval : intervals) {
    events.put(interval[0], events.getOrDefault(interval[0],0)+1);
    events.put(interval[1]+1, events.getOrDefault(interval[1]+1,0)-1);
}
```
Declare conCurInter (Concurrent Intervals) and maxConCurInter (Maximum Concurrent Intervals).
```java
int conCurInter = 0;
int maxConCurInter = 0;
```
Loop through the tree and count all the concurrent intervals and assign new maximums if one is found.
```java
for (Map.Entry<Integer,Integer> entry : events.entrySet()) {
    conCurInter += entry.getValue();
    maxConCurInter = Math.max(maxConCurInter, conCurInter);
}
```
Return maxCunCurInter.
```java
return maxConCurInter;
``` 