/*
 * runtime: 1ms 73%
 * memory: 40.6 MB 33%
 */

import java.util.*;

class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<Integer>();
        row.add(1);
        if (rowIndex == 0)
            return row;
        row.add(1);
        if (rowIndex == 1)
            return row;
        for (int i = 2; i <= rowIndex; i++) {
            row = pascal(row);
        }
        return row;
    }

    public static List<Integer> pascal(List<Integer> prevRow) {
        ArrayList<Integer> nextRow = new ArrayList<Integer>();
        nextRow.add(1);
        nextRow.add(1);
        
        for (int i = 0; i < prevRow.size() - 1; i++) {
            nextRow.add(nextRow.size() - 1, prevRow.get(i) + prevRow.get(i+1));
        }
        return nextRow;
    }
}