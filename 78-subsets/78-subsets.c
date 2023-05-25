/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** subsets(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    int twoN = pow(2, numsSize);
    int **subsets = malloc(twoN * sizeof(int *));
    *returnColumnSizes = malloc(twoN * sizeof(int));
    for (int i = 0; i < twoN; ++i) {
        int iCount = i;
        int *array = NULL;
        int arraySize = 0;
        int j = 0;
        while (iCount > 0) {
            if (iCount & 1) {
                ++arraySize;
                array = realloc(array, arraySize * sizeof(int));
                array[arraySize - 1] = nums[j];
            }
            
            iCount >>= 1;
            ++j;
        }
        subsets[i] = array;
        (*returnColumnSizes)[i] = arraySize;
    }
    *returnSize = twoN;
    return subsets;
}