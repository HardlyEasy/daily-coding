public class Test {
    public static void Main(String[] args) {
        Solution s = new Solution();
        int[] ex1 = {2, 2, 1};
        int[] ex2 = {4, 1, 2, 1, 2};
        int[] ex3 = {1};
        System.Console.WriteLine(s.SingleNumber(ex1));
        System.Console.WriteLine(s.SingleNumber(ex2));
        System.Console.WriteLine(s.SingleNumber(ex3));
    }
}