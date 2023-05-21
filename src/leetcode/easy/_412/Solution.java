package leetcode.easy._412;

import java.util.List;
import java.util.ArrayList;
import java.lang.Integer;


/*
runtime
    1 ms 99.83%
memory
    43.5 MB 50.6%
*/

class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> l = new ArrayList<String>();

        for (int i = 1; i < n + 1; i++) {
            if (i % 3 == 0 && i % 5 == 0)
                l.add("FizzBuzz");
            else if (i % 3 == 0)
                l.add("Fizz");
            else if (i % 5 == 0)
                l.add("Buzz");
            else
                l.add(Integer.toString(i));
        }

        return l;
    }
}