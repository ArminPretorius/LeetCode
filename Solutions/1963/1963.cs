public class Solution {
    public int MinSwaps(string s) {
        int x = 0;
        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] == '[')
                x++;
            else if (x > 0)
                x--;
        }
        return (int) (x+1)/2;
    }
}
