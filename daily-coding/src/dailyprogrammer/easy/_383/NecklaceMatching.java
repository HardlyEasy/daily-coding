package dailyprogrammer.easy._383;

import java.util.ArrayList;

public class NecklaceMatching {
    static final String[][] PAIRS = { 
        {"nicole", "icolen"}, {"nicole", "coneli"}, {"abc", "cba"},
        {"xyxxz", "xxyxz"}, {"x", "xx"}, {"", ""}
    };

    public static boolean isMatch(String s1, String s2) {
        if (s1.length() != s2.length())
            return false;
        else if (s1.equals(s2))
            return true;
        for (int i = 0; i < s2.length(); i++) {
            s1 = s1.substring(1) + s1.substring(0, 1);
            if (s1.equals(s2))
                return true;
        }
        return false;
    }

    public static void main(String[] args) {
        for (int i = 0; i < PAIRS.length; i++) {
            System.out.println(isMatch(PAIRS[i][0], PAIRS[i][1]));
        }
    }
}

// EXPECTED:
/*
 * same_necklace("nicole", "icolen") => true
 * same_necklace("nicole", "coneli") => false
 * same_necklace("abc", "cba") => false
 * same_necklace("xyxxz", "xxyxz") => false
 * same_necklace("x", "xx") => false
 * same_necklace("", "") => true
 */