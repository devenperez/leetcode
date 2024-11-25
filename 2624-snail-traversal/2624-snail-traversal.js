/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    n = this.length

    if (n !== rowsCount * colsCount) return []

    arr = Array(rowsCount)
    for (let i = 0; i < rowsCount; ++i) arr[i] = Array(colsCount)

    for (let i = 0; i < n; ++i) {
        let col = parseInt(i / rowsCount)
        let row = col % 2 === 0 ? i % rowsCount : rowsCount - (i % rowsCount) - 1
        arr[row][col] = this[i]
    }
    return arr
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */