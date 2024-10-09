class Solution {
    public int minLength(String s) {
        boolean bRem = false;
        int oldLen = s.length();
        while (!bRem) {
            oldLen = s.length();
            s = s.replace("AB","");
            s = s.replace("CD","");
            if (oldLen == s.length())
                bRem = true;
        }
        return s.length();
    }
}
