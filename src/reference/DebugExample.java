package reference;

public class DebugExample {
    public static void main(String[] args) {
        /*
        Step Over:
            Steps over current line of code and any method calls in it
        Step Into:
            Steps into method
        Step Out:
            Steps out of current method back to caller method
         */
        count(10);
        System.out.println("Count done");
    }
    public static void count(int c) {
        for (int i = 0; i < c; i++) {
            System.out.println(i);
        }
    }
}
