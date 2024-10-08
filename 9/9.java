class Solution {
    public boolean isPalindrome(int x) {
        String strNum = String.valueOf(x);
        String strRevNum = "";
        for (int i = strNum.length()-1; i >= 0; i--) {
            strRevNum += strNum.charAt(i);
        }
        
        if (strNum.equals(strRevNum)) {
            return true;
        }
        else {
            return false;
        }
    }
}
