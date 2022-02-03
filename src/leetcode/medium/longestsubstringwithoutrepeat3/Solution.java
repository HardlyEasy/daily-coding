/*Sliding window
Notes:
    1) Expand window by 1, add expanded char to set
    2) Until no more repeating in set
        a) Tighten window by 1
    At this point we are guaranteed a valid window length
    3) If window length longest, remember it
    Back to 1) until out of bounds
    Out of bounds defined by right only, left shouldn't pass right ever
Time: O(n)
    n, ri visits a character
    n, li visits a character
Space: ???
    128? from char array
Runtime:
    5 ms, faster than 86.54% of Java
Memory Usage:
    43.6 MB, less than 19.61% of Java
 */

package leetcode.medium.longestsubstringwithoutrepeat3;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Store int values of ASCII characters
        int[] chars = new int[128];
        int longestSize = 0;
        // li to ri is window (inclusive, inclusive)
        int li = 0;
        int ri = 0;
        while (ri < s.length()) {
            // Expand window
            char rightChar = s.charAt(ri);
            chars[rightChar]++;
            // Tighten window if there is a repeat, until no repeat
            while (chars[rightChar] > 1) {
                char leftChar = s.charAt(li);
                chars[leftChar]--;
                li++;
            }
            // If new valid window longest, set it in memory
            longestSize = Math.max(longestSize, ri - li + 1);
            ri++;
        }
        return longestSize;
    }
}