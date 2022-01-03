package leetcode.easy.twosum1;

import java.util.Arrays;

public class TwoSum {
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
    public static void main(String[] args)  {
        int[] ex1 = {2, 7, 11, 15}, ex2 = {3, 2, 4}, ex3 = {3, 3}; // examples
        System.out.println(Arrays.toString(twoSum(ex1, 9)));
        System.out.println(Arrays.toString(twoSum(ex2, 6)));
        System.out.println(Arrays.toString(twoSum(ex3, 6)));
    }
} // end class TwoSum