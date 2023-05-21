package dailyprogrammer.easy._364;

import java.util.Arrays;
import java.util.Random;
import java.util.ArrayList;

public class DiceRoller {
    public static void main(String[] args) {
        Random randInst = new Random();
        ArrayList<String> ex1 = new ArrayList<>(Arrays.asList(
                "5d12", "6d4", "1d2", "1d8", "3d6", "4d20", "100d100"));
        for (int i = 0; i < ex1.size(); i++) {
            String[] input = ex1.get(i).split("d");
            System.out.println(rollAll(input, randInst));
        }
        // (inc, exc)
    }

    public static int rollAll(String[] input, Random randInst) {
        // Rolls all dice and returns sum of values
        int sum = 0;
        int diceAmt = Integer.parseInt(input[0]);
        int sides = Integer.parseInt(input[1]);
        for (int i = 0; i < diceAmt; i++) {
            sum += rollOnce(sides, randInst);
        }
        return sum;
    }

    public static int rollOnce(int sides, Random randInst) {
        // Rolls dice once and returns value
        return randInst.nextInt(sides - 1) + 1;
    }
}
