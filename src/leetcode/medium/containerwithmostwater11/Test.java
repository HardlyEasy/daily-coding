package leetcode.medium.containerwithmostwater11;

public class Test {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] ex1 = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        int[] ex2 = {1, 1};
        System.out.println(s.maxArea(ex1));
        System.out.println(s.maxArea(ex2));
    }
}
