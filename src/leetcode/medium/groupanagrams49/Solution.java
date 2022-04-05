/*
Notes:
    Anagram words are equal when turned into sorted words
    Take all words, sort them, and catalog them in a hashmap
Time Complexity:
    Arrays.sort() done on 1000 strings of 100 length
Space Complexity: O(n)
    at most 1000 hashmap entries
    or 1000 entries split between hm and arraylist in hm
Runtime:
    12 ms, faster than 62.40% of Java
Memory Usage:
    55.7 MB, less than 63.51% of Java
 */

package leetcode.medium.groupanagrams49;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> hm = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            String sorted = sort(strs[i]);
            if (!hm.containsKey(sorted)) {  // create hm entry
                ArrayList<String> temp = new ArrayList<String>();
                temp.add(strs[i]);
                hm.put(sorted, temp);
            }
            else {  // add to existing hm entry
                hm.get(sorted).add(strs[i]);
            }
        }
        return new ArrayList<>(hm.values());
    }

    public String sort(String s) {
        char[] charArray = s.toCharArray();
        Arrays.sort(charArray);
        return new String(charArray);
    }
}