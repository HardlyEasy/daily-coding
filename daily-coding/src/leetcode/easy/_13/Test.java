package leetcode.easy._13;

public class Test {
    static final String[] INPUT = {"III", "LVIII", "MCMXCIV"};
    public static void main(String[] args) {
        Solution s = new Solution();
        for (String ex : INPUT) {
            System.out.println(s.romanToInt(ex));
        }
    }
}
