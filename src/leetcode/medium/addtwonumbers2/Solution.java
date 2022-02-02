/*Elementary Math?
Notes:
    Tricky part is the special case of carried digit at end
    Besides that straightforward
    Just annoying problem not a good one
O(n):
    n, traverse and add
Runtime:
    6 ms, faster than 11.58%
Memory Usage:
    48.5 MB, less than 5.20%
 */

package leetcode.medium.addtwonumbers2;

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int sumDigit = 0;
        ListNode newHead = new ListNode();
        ListNode l3 = newHead;
        boolean carryDigit = false;
        while (true) {
            int sum = 0;
            /* Find Sum
            1) Carry a digit over if needed
            2) Sum digits from l1 and l2
                a) only l1
                b) only l2
                c) both l1 and l2
             */
            if (carryDigit)
                sum++;
            if (l1 == null) {
                sum += l2.val;
                l2 = l2.next;
            }
            else if (l2 == null) {
                sum += l1.val;
                l1 = l1.next;
            }
            else {
                sum += l1.val + l2.val;
                l1 = l1.next;
                l2 = l2.next;
            }
            /* Handle sum
            1) Carry digit if sum greater than equal 10
                a) special exit case, l1 and l2 null
                b) still more summing to do on next pass
            2) No carry digit if sum less than 10
             */
            if (sum >= 10) {
                String tempStr = Integer.toString(sum);
                sumDigit = Integer.parseInt(tempStr.substring(1));
                if (l1 == null && l2 == null) {
                    l3.val = sumDigit;
                    l3.next = new ListNode(1);
                    return newHead;
                }
                else {
                    carryDigit = true;
                }
            }
            else {
                sumDigit = sum;
                carryDigit = false;
            }
            // set columns digit
            l3.val = sumDigit;
            // prepare the next column, if necessary
            if (l1 == null && l2 == null) {
                return newHead;
            }
            else {
                l3.next = new ListNode();
                l3 = l3.next;
            }
        }
    } // end addTwoNumbers()
} // end class