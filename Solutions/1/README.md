# 1. Two Sum
## Index
- [Python](/Solutions/1/README.md#python)
- [C#](/Solutions/1/README.md#c)
- [Java](/Solutions/1/README.md#java)

## Python
#### Solution Code
```py
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x]+nums[y] == target and x != y:
                    return x,y
```
#### Breakdown
Loop through nums using a double pointer technique using x and y as the pointers (index), and then checking if nums[x]+nums[y] = target and that x is not the same as y. Then it returns x and y.
```py
for x in range(len(nums)):
    for y in range(x+1, len(nums)):
        if nums[x]+nums[y] == target and x != y:
            return x,y
```
## C#
#### Solution Code
```cs
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        for (int x = 0; x < nums.Length; x++)
        {
            for (int y = x+1; y < nums.Length; y++)
            {
                if (nums[x] + nums[y] == target && x != y)
                {
                    int[] output = {x,y};
                    return output;
                }
            }
        }
        return null;
    }
}
```
#### Breakdown
Loop through nums using a double pointer technique using x and y as the pointers (index), and then checking if nums[x]+nums[y] = target and that x is not the same as y. Then it returns x and y.
```cs
for (int x = 0; x < nums.Length; x++)
{
    for (int y = x+1; y < nums.Length; y++)
    {
        if (nums[x] + nums[y] == target && x != y)
        {
            int[] output = {x,y};
            return output;
        }
    }
}
```
## Java
#### Solution Code
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int x = 0; x < nums.length; x++) {
            for (int y = 0; y < nums.length; y++) {
                if (nums[x] + nums[y] == target && x!=y) {
                    return new int[]{x,y};
                }
            }
        }
        return null;
    }
}
```
#### Breakdown
Loop through nums using a double pointer technique using x and y as the pointers (index), and then checking if nums[x]+nums[y] = target and that x is not the same as y. Then it returns x and y.
```java
for (int x = 0; x < nums.length; x++) {
    for (int y = 0; y < nums.length; y++) {
        if (nums[x] + nums[y] == target && x!=y) {
            return new int[]{x,y};
        }
    }
}
```
