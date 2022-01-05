public class Test {
    public static void Main(String[] args) {
        Solution s = new Solution();
        string[] ex1 = {"flower","flow","flight"};
        string[] ex2 = {"dog","racecar","car"};
        System.Console.WriteLine(s.LongestCommonPrefix(ex1));
        System.Console.WriteLine(s.LongestCommonPrefix(ex2));

        string[] test1 = {"ab","a"};
        System.Console.WriteLine(s.LongestCommonPrefix(test1));
    }
} // end class