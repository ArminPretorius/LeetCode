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