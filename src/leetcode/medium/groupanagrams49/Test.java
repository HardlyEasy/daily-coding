package leetcode.medium.groupanagrams49;

import java.util.List;

public class Test {
    public static void main(String[] args) {
        Solution s = new Solution();
        String[] ex1 = {"eat", "tea", "tan", "ate", "nat", "bat"};
        String[] ex2 = {""};
        String[] ex3 = {"a"};
        System.out.println(s.groupAnagrams(ex1));
        System.out.println(s.groupAnagrams(ex2));
        System.out.println(s.groupAnagrams(ex3));
    }
}
