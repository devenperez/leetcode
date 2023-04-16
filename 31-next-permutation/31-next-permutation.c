int cmpInt(const void *a, const void *b) {
    const int *ia = a;
    const int *ib = b;
    return *ia - *ib;
}

void nextPermutation(int* nums, int numsSize){
    int firstDecrI = -1; 
    for (int i = numsSize - 2; i >= 0; --i) {
        if (nums[i] < nums[i + 1]) {
            firstDecrI = i;
            break;
        }
    }
    
    // Last permutation edge case
    if (firstDecrI == - 1) {
        qsort(nums, numsSize, sizeof(int), cmpInt);
        return;
    }
    
    // place next largest num into nums[firstDecrI]
    int nextHighest = INT_MAX;
    int nextHighestI = -1;
    for (int i = firstDecrI + 1; i < numsSize; ++i) {
        if (nums[firstDecrI] < nums[i] && nums[i] < nextHighest) {
            nextHighest = nums[i];
            nextHighestI = i;
        }
    }
    int tmp = nums[firstDecrI];
    nums[firstDecrI] = nums[nextHighestI];
    nums[nextHighestI] = tmp;
    
    // sort nums[firstDecrI + 1...numsSize - 1]
    qsort(nums + firstDecrI + 1, numsSize - firstDecrI - 1, sizeof(int), cmpInt);
    
}