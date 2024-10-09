public class Solution {
    public int MinLength(string s) {
        bool bRem = false;
        while (!bRem)
        {
            int pos1 = s.IndexOf("AB");
            if (pos1 != -1)
            {
                s = s.Remove(pos1,2);
            }
            int pos2 = s.IndexOf("CD");
            if (pos2 != -1)
            {
                s = s.Remove(pos2,2);
            }
            if (pos1 == -1 && pos2 == -1)
            {
                bRem = true;
            }
        }
        return s.Length;
    }
}
