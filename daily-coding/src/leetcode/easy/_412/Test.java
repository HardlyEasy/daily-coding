package leetcode.easy._412;

public class Test {
    static final int[] INPUT = {3, 5, 15};
    public static void main(String[] args) {
        Solution sol = new Solution();
        for (int ex : INPUT) {
            System.out.println(sol.fizzBuzz(ex));
        }
    }
}
