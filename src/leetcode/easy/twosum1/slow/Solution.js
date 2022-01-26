// Comment me for solution submission
// Uncomment me to run Test.js
// export { twoSum }

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
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