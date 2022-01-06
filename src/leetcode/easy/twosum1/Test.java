package leetcode.easy.twosum1;

import java.util.Arrays;

public class Test {
    public static void main(String[] args)  {
        int[] ex1 = {2, 7, 11, 15}, ex2 = {3, 2, 4}, ex3 = {3, 3}; // examples
        System.out.println(Arrays.toString(Solution.twoSum(ex1, 9)));
        System.out.println(Arrays.toString(Solution.twoSum(ex2, 6)));
        System.out.println(Arrays.toString(Solution.twoSum(ex3, 6)));
    }
}
