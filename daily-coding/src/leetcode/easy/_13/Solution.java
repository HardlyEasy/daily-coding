package leetcode.easy._13;
import java.util.HashMap;

class Solution {
    private static final HashMap<String, Integer> HM = 
            new HashMap<String, Integer>();
    static {
        HM.put("IV", 4);
        HM.put("IX", 9);
        HM.put("XL", 40);
        HM.put("XC", 90);
        HM.put("CD", 400);
        HM.put("CM", 900);

        HM.put("I", 1);
        HM.put("V", 5);
        HM.put("X", 10);
        HM.put("L", 50);
        HM.put("C", 100);
        HM.put("D", 500);
        HM.put("M", 1000);
    }
    public Solution() {
        
    }

    public int romanToInt(String s) {
        int sum = 0;
        while (true) {  // think of as numeral reader machine
            if (s.length() == 0) {
                break;
            }
            else if (s.length() == 1) {
                sum += HM.get("" + s.charAt(0));
                break;
            }
            else {
                String check = s.substring(0, 2);
                if (HM.containsKey(check)) {  // double numeral
                    sum += HM.get(check);
                    s = s.substring(2);
                }
                else {  // single numeral
                    sum += HM.get("" + check.charAt(0));
                    s = s.substring(1);
                }
            }
        }
        return sum;
    }
}