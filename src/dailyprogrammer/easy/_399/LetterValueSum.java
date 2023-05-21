package dailyprogrammer.easy._399;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

class LetterValueSum {
    static final String textFilePath = "./src/dailyprogrammer/easy/" +
            "_399/wordList.txt";
    static final String[] challengeArr = {"", "a", "z", "cab",
            "excellent", "microspectrophotometries"};

    public static void main(String[] args) {
        challenge();
        all_bonus();
    }

    // sums all letters in word, a=1 z=26
    public static int letterSum(String word) {
        int sum = 0;
        for(int i=0; i < word.length(); i++) {
            char letter = word.charAt(i);
            sum += (int)letter -96;
        }
        return sum;
    }

    public static void challenge() {
        System.out.println("===== Challenge =====");
        for(int i=0; i < challengeArr.length; i++) {
            String word = challengeArr[i];
            System.out.println("letterSum(\"" + word + "\") => " + letterSum(word));
        }
    }

    public static ArrayList<String> read_file() {
        ArrayList<String> words = new ArrayList<String>();
        try {
            File wordFile = new File(textFilePath);
            Scanner wordScanner = new Scanner(wordFile);
            while(wordScanner.hasNextLine())
                words.add(wordScanner.nextLine());
            wordScanner.close();
        } catch(FileNotFoundException e) {
            System.out.println("File reading error");
            e.printStackTrace();
        }
        return words;
    }

    public static void all_bonus() {
        System.out.println("===== Bonus =====");
        ArrayList<String> words = read_file();
        System.out.println(bonus1(words) + " has letter sum of 319");
        System.out.println(bonus2(words) + " odd letters");
        HashMap<Integer, String> sum_map = create_sum_map(words);
        //bonus3_answer = bonus3(sum_map);
        //System.out.println(bonus3_answer[0] + bonus3_answer[1]);
    }

    public static String bonus1(ArrayList<String> words) {
        for(int i = 0; i < words.size(); i++) {
            String word = words.get(i);
            int sum = letterSum(word);
            if (sum == 319) // bonus 1
                return word;
        }
        return "";
    }

    public static int bonus2(ArrayList<String> words) {
        int oddCount = 0;
        for(int i = 0; i < words.size(); i++) {
            String word = words.get(i);
            int sum = letterSum(word);
            if ((sum % 2) == 1) // bonus 1
                oddCount++;
        }
        return oddCount;
    }

    public static HashMap<Integer, String> create_sum_map(
            ArrayList<String> words) {
        HashMap<Integer, String> sum_map = new HashMap<Integer, String>();
        for(int i =0; i< words.size(); i++) {
            String word = words.get(i);
            int sum = letterSum(word);
            sum_map.put(sum, word);
        }
        return sum_map;
    }

    /*
    public static int[] bonus3(HashMap<Integer, String> sum_map) {
        for (HashMap.Entry<Integer, String> entry : sum_map.entrySet()) {
            Integer sum = entry.getKey();
            String word = entry.getValue();
        }
    }
     */
}