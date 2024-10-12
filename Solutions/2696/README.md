# 2696. Minimum String Length After Removing Substrings
## Index
- [Python](/Solutions/2696/README.md#python)
- [C#](/Solutions/2696/README.md#c)
- [Java](/Solutions/2696/README.md#java)

## Python
#### Solution Code
```py
class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        bRem = False
        while bRem == False:
            oldLen = len(s)
            s = s.replace("AB","")
            s = s.replace("CD","")
            if oldLen == len(s):
                bRem = True

        return len(s)
```
#### Breakdown
Set bRem false (flag for while loop).
```py
bRem = False
```
While bRem is false, assign the pre-changes length of s, replace "AB" and "CD" with "" and then test if the pre-change string is the same length as the post-change one, if it is, set the flag to true, stopping the loop.
```py
while bRem == False:
    oldLen = len(s)
    s = s.replace("AB","")
    s = s.replace("CD","")
    if oldLen == len(s):
        bRem = True
```
Return the length of s.
```py
return len(s)
```
## C#
#### Solution Code
```cs
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
```
#### Breakdown
Set bRem false (flag for while loop).
```cs
bool bRem = false;
```
While bRem is false, get the index of "AB" and "CD", then remove them at the indexes if found. If both indexes retreived for "AB" and "CD" are -1, then none were found, so make bRem true and stop the loop.
```cs
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
```
Return the length of s.
```cs
return s.Length;
```
## Java
#### Solution Code
```java
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
```
#### Breakdown
Set bRem false (flag for while loop) and declare oldLen (stores the pre-changes length value for s).
```java
boolean bRem = false;
int oldLen = s.length();
```
While bRem is false, assign the pre-changes length of s, replace "AB" and "CD" with "" and then test if the pre-change string is the same length as the post-change one, if it is, set the flag to true, stopping the loop.
```java
while (!bRem) {
    oldLen = s.length();
    s = s.replace("AB","");
    s = s.replace("CD","");
    if (oldLen == s.length())
        bRem = true;
}
```
Return the length of s.
```java
return s.length();
```
