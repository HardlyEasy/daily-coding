package dailyprogrammer.easy._391;

public class abacaba {
    public static void main(String[] args) {
        System.out.println(sequencer(5));
    }
    public static String sequencer(int n) {
        //given number of sequences, returns final sequence
        String seq = "";
        int i = 1;
        while(i <= n)
            seq = seq + (char)((int)'a' + i++ - 1) + seq;
        return seq;
    }
}
