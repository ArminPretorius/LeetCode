# 921. Minimum Add to Make Parentheses Valid
## Index
- [Python](/Solutions/921/README.md#python)
- [C#](/Solutions/921/README.md#c)
- [Java](/Solutions/921/README.md#java)

## Python
#### Solution Code
```py
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        missed = 0
        for x in s:
            if x == "(":
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    missed += 1
        return count+missed
```
#### Breakdown
Initialize variables (count: counts the number of parentheses that were opened but not closed; missed: counts the number of parentheses that were closed but never opened).
```py
count = 0
missed = 0
```
Loop through s with x being a character of s. If x is "(" then increase count by one, else if count is bigger than 0 then decrease it by one, however if count is not, then increase missed by one.
```py
for x in s:
    if x == "(":
        count += 1
    else:
        if count > 0:
            count -= 1
        else:
            missed += 1
```
Return count + missed, as these will be the minimum amount of parentheses needed.
```py
return count+missed
```
## C#
#### Solution Code
```cs
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
```
#### Breakdown
Initialize variables (count: counts the number of parentheses that were opened but not closed; missed: counts the number of parentheses that were closed but never opened).
```cs
int count = 0;
int missed = 0;
```
Loop through s with x being a character of s. If x is "(" then increase count by one, else if count is bigger than 0 then decrease it by one, however if count is not, then increase missed by one.
```cs
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
```
Return count + missed, as these will be the minimum amount of parentheses needed.
```cs
return count+missed;
```
## Java
#### Solution Code
```java
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
```
#### Breakdown
Initialize variables (count: counts the number of parentheses that were opened but not closed; missed: counts the number of parentheses that were closed but never opened).
```java
int count = 0;
int missed = 0;
```
Loop through s with x being a character of s. If x is "(" then increase count by one, else if count is bigger than 0 then decrease it by one, however if count is not, then increase missed by one.
```java
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
```
Return count + missed, as these will be the minimum amount of parentheses needed.
```java
return count+missed;
```
