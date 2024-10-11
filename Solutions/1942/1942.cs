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