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