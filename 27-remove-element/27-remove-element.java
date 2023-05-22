class Solution {
    public int removeElement(int[] nums, int val) {
        if (nums.length == 0) {
            return 0;
        }

        int backIndex = nums.length - 1;
        for (int i = 0; i < backIndex; ++i) {
            if (nums[i] == val) {
                while (nums[backIndex] == val) {
                    backIndex--;
                    if (backIndex == i) {
                        return nums[backIndex] == val ? backIndex : backIndex + 1;
                    }
                }
                nums[i] = nums[backIndex];
                nums[backIndex] = val;
                backIndex--;
            }
        }
        return nums[backIndex] == val ? backIndex : backIndex + 1;
    }
}