package leetcode.easy.twosum1;

import java.util.Arrays;

public class TwoSum {
    public static int[] twoSum(int[] nums, int target)  {
        int[] solution = {-1, -1}; // constraints prevent this from returning
        for (int lc = 0; lc < nums.length - 1; lc++) {
            for (int rc = lc + 1; rc < nums.length; rc++) {
                int left = nums[lc], right = nums[rc];
                if (left + right == target) {
                    solution[0] = lc;
                    solution[1] = rc;
                }
            } // end inner loop
        } // end outer loop
        return solution;
    } // end method twoSum()
    public static void main(String[] args)  {
        int[] ex1 = {2, 7, 11, 15}, ex2 = {3, 2, 4}, ex3 = {3, 3}; // examples
        System.out.println(Arrays.toString(twoSum(ex1, 9)));
        System.out.println(Arrays.toString(twoSum(ex2, 6)));
        System.out.println(Arrays.toString(twoSum(ex3, 6)));
    }
} // end class TwoSum