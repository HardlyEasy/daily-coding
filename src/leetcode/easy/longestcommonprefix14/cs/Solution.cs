public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        string longest = "";
        for (int i = 0; i < strs[0].Length; i++) {
            // Select substring of first word
            string firstSub = strs[0].Substring(0, i + 1);
            for (int j = 1; j < strs.Length; j++) {
                // Guard against out of bounds
                if (strs[j].Length == 0 || firstSub.Length > strs[j].Length)
                    return longest;
                // Select substring of next word
                string nextSub = strs[j].Substring(0, i + 1);
                if (!firstSub.Equals(nextSub))
                    return longest;
            }
            // We checked all strings for matching substring at this point
            longest = firstSub;
        }
        return longest;
    }
} // end class