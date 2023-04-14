/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    
    for (int i = 0; i < numsSize; ++i) {
       for (int j = i + 1; j < numsSize; ++j) {
            if (nums[i] + nums[j] == target) {
                int *returnPair = malloc(2 * sizeof(int));
                returnPair[0] = i;
                returnPair[1] = j;
                *returnSize = 2;
                
                return returnPair;
            }
        } 
    }
    return NULL;
}