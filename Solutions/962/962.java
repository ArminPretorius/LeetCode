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
