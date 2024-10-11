# 962. Maximum Width Ramp
## Index
- [Python](/Solutions/962/README.md#python)
- [C#](/Solutions/962/README.md#c)
- [Java](/Solutions/962/README.md#java)

## Python
#### Solution Code
```py
class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        indices_stack = []

        for i in range(n):
            if not indices_stack or nums[indices_stack[-1]] > nums[i]:
                indices_stack.append(i)

        max_width = 0

        for j in range(n - 1, -1, -1):
            while indices_stack and nums[indices_stack[-1]] <= nums[j]:
                max_width = max(max_width, j - indices_stack[-1])
                indices_stack.pop()

        return max_width
```
#### Breakdown
Declaring n (Length of nums) & indices_stack (Monotonic stack of indices).
```py
n = len(nums)
indices_stack = []
```
Populating indices_stack based on the value of the indices in nums by adding to the stack if the stack is empty or the number at the last added index is bigger than the number at index i.
```py
for i in range(n):
    if not indices_stack or nums[indices_stack[-1]] > nums[i]:
        indices_stack.append(i)
```
Declaring max_width and assigning it the value of 0.
```py
max_width = 0
```
Calculating the maximum width by iterating through nums while the indices stack is not empty and the num at index j is bigger than or equal to the number at the last added index. In the while it sets the max_width to the maximum index between max_width and j - the last added index, and then pops the last added index from the stack.
```py
for j in range(n - 1, -1, -1):
    while indices_stack and nums[indices_stack[-1]] <= nums[j]:
        max_width = max(max_width, j - indices_stack[-1])
        indices_stack.pop()
```
Returning max_width.
```py
return max_width
```
## C#
#### Solution Code
```cs
public class Solution {
    public int MaxWidthRamp(int[] nums) {
        int n = nums.Length;
        Stack indicesStack = new Stack();

        for (int i = 0; i < n; i++)
        {
            if (indicesStack.Count == 0 || nums[Convert.ToInt32(indicesStack.Peek())] > nums[i])
                indicesStack.Push(i);
        }

        int maxWidth = 0;

        for (int i = n-1; i > -1; i--)
        {
            while (!(indicesStack.Count == 0) && nums[Convert.ToInt32(indicesStack.Peek())] <= nums[i])
            {
                maxWidth = Math.Max(i - Convert.ToInt32(indicesStack.Peek()),maxWidth);
                indicesStack.Pop();
            }
        }

        return maxWidth;
    }
}
```
#### Breakdown
Declaring n (Length of nums) & indicesStack (Monotonic stack of indices).
```cs
int n = nums.Length;
Stack indicesStack = new Stack();
```
Populating indicesStack based on the value of the indices in nums by adding to the stack if the stack is empty or the number at the last added index is bigger than the number at index i.
```cs
for (int i = 0; i < n; i++)
{
    if (indicesStack.Count == 0 || nums[Convert.ToInt32(indicesStack.Peek())] > nums[i])
        indicesStack.Push(i);
}
```
Declaring maxWidth and assigning it the value of 0.
```cs
int maxWidth = 0;
```
Calculating the maximum width by iterating through nums while the indices stack is not empty and the num at index j is bigger than or equal to the number at the last added index. In the while it sets the maxWidth to the maximum index between maxWidth and j - the last added index, and then pops the last added index from the stack.
```cs
for (int i = n-1; i > -1; i--)
{
    while (!(indicesStack.Count == 0) && nums[Convert.ToInt32(indicesStack.Peek())] <= nums[i])
    {
        maxWidth = Math.Max(i - Convert.ToInt32(indicesStack.Peek()),maxWidth);
        indicesStack.Pop();
    }
}
```
Returning maxWidth.
```cs
return maxWidth;
```
## Java
#### Solution Code
```java
class Solution {
    public int maxWidthRamp(int[] nums) {
        int n = nums.length;
        Stack<Integer> indices_mstack = new Stack<>();
        
        for (int i = 0; i < n; i++) {
            if (indices_mstack.isEmpty() || nums[indices_mstack.peek()] > nums[i]) {
                indices_mstack.push(i);
            }
        }

        int maxWidth = 0;
        
        for (int i = n-1; i > -1; i--) {
            while (!indices_mstack.isEmpty() && nums[indices_mstack.peek()] <= nums[i]) {
                maxWidth = Math.max(maxWidth, i-indices_mstack.pop());
            }
        }
        
        return maxWidth;
    }
}
```
#### Breakdown
Declaring n (Length of nums) & indicesStack (Monotonic stack of indices).
```java
int n = nums.length;
Stack<Integer> indices_mstack = new Stack<>();
```
Populating indices_mstack based on the value of the indices in nums by adding to the stack if the stack is empty or the number at the last added index is bigger than the number at index i.
```java
for (int i = 0; i < n; i++) {
    if (indices_mstack.isEmpty() || nums[indices_mstack.peek()] > nums[i]) {
        indices_mstack.push(i);
    }
}
```
Declaring maxWidth and assigning it the value of 0.
```java
int maxWidth = 0;
```
Calculating the maximum width by iterating through nums while the indices stack is not empty and the num at index j is bigger than or equal to the number at the last added index. In the while it sets the maxWidth to the maximum index between maxWidth and j - the last added index, and then pops the last added index from the stack.
```java
for (int i = n-1; i > -1; i--) {
    while (!indices_mstack.isEmpty() && nums[indices_mstack.peek()] <= nums[i]) {
        maxWidth = Math.max(maxWidth, i-indices_mstack.pop());
    }
}
```
Returning maxWidth.
```java
return maxWidth;
```
