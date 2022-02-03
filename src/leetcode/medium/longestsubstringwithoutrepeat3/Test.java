package leetcode.medium.longestsubstringwithoutrepeat3;

public class Test {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.lengthOfLongestSubstring("abcabcbb"));
        System.out.println(sol.lengthOfLongestSubstring("bbbbb"));
        System.out.println(sol.lengthOfLongestSubstring("pwwkew"));
        System.out.println(sol.lengthOfLongestSubstring(" "));

        //System.out.println("abc".substring(0));
    }
}
