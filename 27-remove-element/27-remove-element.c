int removeElement(int* nums, int numsSize, int val){
    if (numsSize == 0) {
        return 0;
    }
    
    int backIndex = numsSize - 1;
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