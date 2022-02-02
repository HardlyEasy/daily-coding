package leetcode.medium.addtwonumbers2;

public class Test {
    public static void main(String[] args) {
        ListNode ex10 = createNode(new int[] {2, 4, 3});
        ListNode ex11 = createNode(new int[] {5, 6, 4});
        ListNode ex20 = createNode(new int[] {0});
        ListNode ex21 = createNode(new int[] {0});
        ListNode ex30 = createNode(new int[] {9, 9, 9, 9, 9, 9, 9});
        ListNode ex31 = createNode(new int[] {9, 9, 9, 9});
        Solution sol = new Solution();
        printNode(sol.addTwoNumbers(ex10, ex11));
        printNode(sol.addTwoNumbers(ex20, ex21));
        printNode(sol.addTwoNumbers(ex30, ex31));

    }
    public static ListNode createNode(int[] arr) {
        ListNode head = new ListNode(arr[0]);
        ListNode ln = head;
        for(int i = 1; i < arr.length; i++) {
            ln.next = new ListNode(arr[i]);
            ln = ln.next;
        }
        return head;
    }
    public static void printNode(ListNode ln) {
        while(ln != null) {
            System.out.print(ln.val);
            ln = ln.next;
        }
        System.out.println();
    }
}
