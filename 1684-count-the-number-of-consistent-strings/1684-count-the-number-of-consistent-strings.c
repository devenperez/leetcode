

int countConsistentStrings(char * allowed, char ** words, int wordsSize){
    
    bool allowedFilter[26] = {false};
    for (char *c = allowed; *c != '\0'; ++c) {
        allowedFilter[*c - 'a'] = true;
    }
    
    int numAllowedWords = 0;
    for (int i = 0; i < wordsSize; ++i) {
        bool allowedWord = true;
        for (char* a = words[i]; *a != '\0'; ++a) {
            if (!allowedFilter[*a - 'a']) {
                allowedWord = false;
                break;
            }
        }  
        if (allowedWord) {
            ++numAllowedWords;
        }
    }
    return numAllowedWords;
}