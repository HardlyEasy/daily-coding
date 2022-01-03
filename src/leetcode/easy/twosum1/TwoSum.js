/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let lc = 0; lc < nums.length - 1; lc++) {
        for (let rc = lc + 1; rc < nums.length; rc++) {
            let left = nums[lc];
            let right = nums[rc];
            if (right + left === target) {
                return [lc, rc];
            }
        }
    }
};

ex1 = [2, 7, 11, 15], ex2 = [3, 2, 4], ex3 = [3, 3];
console.log(twoSum(ex1, 9));
console.log(twoSum(ex2, 6));
console.log(twoSum(ex3, 6));