package dailyprogrammer.easy._239;

public class ThreesGame {
    static final int[] INPUT = {100};
    public static void main(String[] args) {
        for (int number : INPUT) {
            while (number > 1) {
                number = step(number);
            }
            System.out.println(number);
        }
    }
    public static int step(int number) {
        int remainder = number % 3;
        int adjust = 0;
        if (remainder == 1)
            adjust = -1;
        else if (remainder == 2)
            adjust = 1;
        System.out.printf("%d %d\n", number, adjust);
        return (number + adjust) / 3;
    }
}