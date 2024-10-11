# 9. Palindrome Number
## Index
- [Python](/Solutions/9/README.md#python)
- [C#](/Solutions/9/README.md#c)
- [Java](/Solutions/9/README.md#java)

## Python
#### Solution Code
```py
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        sint = str(x)
        if sint[::-1] == sint:
            return True
        else:
            return False
```
#### Breakdown
Convert the integer to a string.
```py
sint = str(x)
```
Reverse the string and test if it equals the normal string.
```py
if sint[::-1] == sint:
        return True
    else:
        return False
```
## C#
#### Solution Code
```cs
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
```
#### Breakdown
Convert the integer to a string.
```cs
string strNum = Convert.ToString(x);
```
Reverse the string using a for loop.
```cs
string newNum = "";

for (int i = strNum.Length-1; i >= 0; i--)
{
    newNum += strNum[i];
}
```
Check if the reversed string is the same as the normal string.
```cs
if (newNum == strNum)
{
    return true;
}
else
{
    return false;
}
```
## Java
#### Solution Code
```java
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
```
#### Breakdown
Convert the integer to a string.
```java
String strNum = String.valueOf(x);
```
Reverse the string using a for loop.
```java
String strRevNum = "";
for (int i = strNum.length()-1; i >= 0; i--) {
    strRevNum += strNum.charAt(i);
}
```
Check if the reversed string is the same as the normal string.
```java
if (strNum.equals(strRevNum)) {
    return true;
}
else {
    return false;
}
```
