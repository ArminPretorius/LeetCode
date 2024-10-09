class Solution {
    public int minSwaps(String s) {
        int x = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '[')
                x++;
            else if (x > 0)
                x--;
        }
        return (int) (x+1)/2;
    }
}
