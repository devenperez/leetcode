/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** fizzBuzz(int n, int* returnSize){
    char **array = malloc(n * sizeof(char *));
    *returnSize = n;
    
    for (int i = 1; i <= n; ++i) {
        if (i % 15 == 0) {
            array[i - 1] = "FizzBuzz";
        } else if (i % 3 == 0) {
            array[i - 1] = "Fizz";
        } else if (i % 5 == 0) {
            array[i - 1] = "Buzz";
        } else {
            array[i - 1] = malloc((int) (ceil(log10(i + 1)) + 1) * sizeof(char));
            sprintf(array[i - 1], "%d", i);
        }
    }
    
    return array;
    
}