bool isValidSudoku(char** board, int boardSize, int* boardColSize){
    bool rowFilter[9][9] = {};
    bool colFilter[9][9] = {};
    bool boxFilter[9][9] = {};
    
    for (int row = 0; row < boardSize; ++row) {
        for (int col = 0; col < boardColSize[row]; ++col) {
            int box = ((int) (row / 3)) * 3 + ((int) (col / 3));
            int val = board[row][col] - '0' - 1;
            
            if (val == ('.' - '0' - 1)) {
                continue;
            }
            
            if (rowFilter[row][val] || colFilter[col][val] || boxFilter[box][val]) {
                return false;
            }
            
            rowFilter[row][val] = true;
            colFilter[col][val] = true;
            boxFilter[box][val] = true;
            
        }
    }
    
    return true;
}