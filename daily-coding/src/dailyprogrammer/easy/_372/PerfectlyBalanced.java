package dailyprogrammer.easy._372;

import java.util.HashMap;

public class PerfectlyBalanced {
    static final String[] INPUT = {
        "xxxyyyzzz", "abccbaabccba", "xxxyyyzzzz", 
        "abcdefghijklmnopqrstuvwxyz", "pqq", "fdedfdeffeddefeeeefddf",
        "www", "x", ""
    };
    public static void main(String[] args) {
        for (int i = 0; i < INPUT.length; i++) {
            System.out.printf("balanced_bonus(\"%s\") => %s\n", INPUT[i], 
                balanced_bonus(INPUT[i]));
        }
    }

    public static HashMap<String, Integer> count_letters(String s) {
        /*
         * destructive to String s, cuts it down
         */
        HashMap<String, Integer> hm = new HashMap<String, Integer>();
        while (s.length() > 0) {
            // cut off front
            String ch = s.substring(0, 1);
            s = s.substring(1);
            if (!hm.containsKey(ch))
                hm.put(ch, 1);
            else
                hm.put(ch, hm.get(ch) + 1);
        }
        return hm;
    }

    public static boolean balanced_bonus(String s) {
        HashMap<String, Integer> hm = count_letters(s);
        // handle 0-1 letter cases
        if (hm.size() <= 1)
            return true;
        // handle 2+ letter cases
        int i = 0;
        Integer first_count = 0;
        for (Integer count : hm.values()) {
            if (i == 0)  // annoying to get first hm value out of hm
                first_count = count;
            if (first_count != count)
                return false;
            i++;
        }
        return true;
    }
}