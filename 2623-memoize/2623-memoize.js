/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    memo = {}
    return function(...args) {
        let key = JSON.stringify(args)
        let val = memo[key]
        if (val !== undefined) return val

        val = fn(...args)
        memo[key] = val
        return val
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */