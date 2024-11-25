/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    let s = JSON.stringify(obj)
    return s === "[]" || s === "{}" || s === ""
};