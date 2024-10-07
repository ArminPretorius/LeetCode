public class Solution {
    public bool IsPalindrome(int x) {
        string strNum = Convert.ToString(x);
        string newNum = "";

        for (int i = strNum.Length-1; i >= 0; i--)
        {
            newNum += strNum[i];
        }

        if (newNum == strNum)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
