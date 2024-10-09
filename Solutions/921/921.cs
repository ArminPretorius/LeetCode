public class Solution {
    public int MinAddToMakeValid(string s) {
        int count = 0;
        int missed = 0;
        foreach (char x in s)
        {
            if (x == '(')
                count++;
            else
            {
                if (count > 0)
                    count--;
                else
                    missed++;
            }
        }
        return count+missed;
    }
}
