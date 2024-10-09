class Solution {
    public int minAddToMakeValid(String s) {
        int count = 0;
        int missed = 0;
        for (char x : s.toCharArray()) {
            if (x == '(') {
                count++;
            } else {
                if (count > 0) {
                    count--;
                } else {
                    missed++;
                }
            }
        }
        return count+missed;
    }
}
