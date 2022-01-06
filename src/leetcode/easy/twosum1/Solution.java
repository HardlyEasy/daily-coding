package leetcode.easy.twosum1;

public class Solution {
    public static int[] twoSum(int[] nums, int target)  {
        int[] summed = {-1, -1}; // constraints prevent this from returning
        for (int li = 0; li < nums.length - 1; li++) { // li means left index
            for (int ri = li + 1; ri < nums.length; ri++) {
                int left = nums[li], right = nums[ri];
                if (left + right == target) {
                    summed[0] = li;
                    summed[1] = ri;
                }
            } // end inner loop
        } // end outer loop
        return summed;
    } // end method twoSum()
} // end class