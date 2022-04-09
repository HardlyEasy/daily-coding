package leetcode.medium.sortlist148;

public class Test {
    public static void main(String[] args) {
        Solution s = new Solution();
        ListNode head = new ListNode(4);
        head.next = new ListNode(2);
        head.next.next = new ListNode(1);
        head.next.next.next = new ListNode(3);
        printLinkedList(head);
    }
    public static void printLinkedList(ListNode head) {
        ListNode current = head;
        while (current != null) {
            System.out.print(current.val);
            current = current.next;
        }
        System.out.println();
    }
    /*
    public static void buildLinkedList(ListNode head, int[] a) {
        ListNode current = head;
        for (int i = 0; i < a.length; i++) {
            current.val = a[i];
            if (i != a.length - 1)
                current.next = new ListNode();
        }
    }
     */
}
