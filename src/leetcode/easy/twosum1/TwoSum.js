/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let li = 0; li < nums.length - 1; li++) { // li means left index
        for (let ri = li + 1; ri < nums.length; ri++) {
            let left = nums[li];
            let right = nums[ri];
            if (right + left === target) {
                return [li, ri];
            }
        }
    }
};

ex1 = [2, 7, 11, 15], ex2 = [3, 2, 4], ex3 = [3, 3];
console.log(twoSum(ex1, 9));
console.log(twoSum(ex2, 6));
console.log(twoSum(ex3, 6));