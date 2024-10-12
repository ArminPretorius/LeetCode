# 1963. Minimum Number of Swaps to Make the String Balanced
## Index
- [Python](/Solutions/1963/README.md#python)
- [C#](/Solutions/1963/README.md#c)
- [Java](/Solutions/1963/README.md#java)

## Python
#### Solution Code
```py
class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = 0
        for i in s:
            if i == '[':
                x += 1
            elif x > 0:
                x -= 1
        return (x + 1) // 2
```
#### Breakdown
Declare x as 0 (x: count of opened brackets that have not been closed).
```py
x = 0
```
Loop through s, with i as the chars. If i = '[' then increase x by one, else if x is bigger than zero, then decrease x by one.
```py
for i in s:
    if i == '[':
        x += 1
    elif x > 0:
        x -= 1
```
Return (x+1) // 2, which gives you the minimum number of swaps you need to make.
```py
return (x + 1) // 2
```
## C#
#### Solution Code
```cs
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
```
#### Breakdown
Declare x as 0 (x: count of opened brackets that have not been closed).
```cs
int x = 0;
```
Loop through s, with i as the chars. If i = '[' then increase x by one, else if x is bigger than zero, then decrease x by one.
```cs
for (int i = 0; i < s.Length; i++)
{
    if (s[i] == '[')
        x++;
    else if (x > 0)
        x--;
}
```
Return (x+1) / 2, which gives you the minimum number of swaps you need to make with (int) conversion working as a method to truncate the value and convert it to an int.
```cs
return (int) (x+1)/2;
```
## Java
#### Solution Code
```java
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
```
#### Breakdown
Declare x as 0 (x: count of opened brackets that have not been closed).
```java
int x = 0;
```
Loop through s, with i as the chars. If i = '[' then increase x by one, else if x is bigger than zero, then decrease x by one.
```java
for (int i = 0; i < s.length(); i++) {
    if (s.charAt(i) == '[')
        x++;
    else if (x > 0)
        x--;
}
```
Return (x+1) / 2, which gives you the minimum number of swaps you need to make with (int) conversion working as a method to truncate the value and convert it to an int.
```java
return (int) (x+1)/2;
```
