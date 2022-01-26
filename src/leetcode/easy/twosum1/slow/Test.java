package leetcode.easy.twosum1.slow;

import java.util.Arrays;
import java.util.Random;

public class Test {
    public static void main(String[] args)  {
        int[] ex1 = {2, 7, 11, 15}, ex2 = {3, 2, 4}, ex3 = {3, 3}; // examples
        //System.out.println(Arrays.toString(Solution.twoSum(ex1, 9)));
        //System.out.println(Arrays.toString(Solution.twoSum(ex2, 6)));
        //System.out.println(Arrays.toString(Solution.twoSum(ex3, 6)));
        int[] hugeArray = createBigTest();
        long start = System.currentTimeMillis();
        System.out.println(Arrays.toString(Solution.twoSum(hugeArray, 500)));
        long end = System.currentTimeMillis();
        long elapsedTime = end - start;
        System.out.println(elapsedTime);
    }
    public static int[] createBigTest() {
        int[] a = new int[2000000];
        Random rd = new Random();
        for (int i = 0; i < a.length - 2; i++) {
            a[i] = rd.nextInt(100);
        }
        a[1999999] = 499;
        a[1999998] = 1;
        return a;
    }
}
