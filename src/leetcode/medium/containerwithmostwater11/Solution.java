/*
Notes:
    There's a O(n) solution using two pointers
    My solution seems along the right track to the O(n)
Time Complexity: O(n^2)

Runtime:
    205 ms, faster than 5.28% of Java
Memory Usage:
    81.2 MB, less than 38.41% of Java
 */

package leetcode.medium.containerwithmostwater11;

class Solution {
    public int maxArea(int[] height) {
        int max = 0;
        for (int x0 = 0; x0 < height.length - 1; x0++) {
            int y0 = height[x0];
            for (int x1 = height.length - 1; x1 > x0; x1--) {
                int y1 = height[x1];
                int area = calcArea(x0, x1, y0, y1);
                if (area > max)
                    max = area;
                // Greatest possible area encountered already
                if (y0 <= y1)
                    break;
            }
        }
        return max;
    }

    public int calcArea(int x0, int x1, int y0, int y1) {
        int width = x1 - x0;
        return (x1 - x0) * Math.min(y0, y1);
    }
}