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
