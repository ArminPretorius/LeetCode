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