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
