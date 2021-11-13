package dailyprogrammer.easy.lettervaluesum399;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class LetterValueSum {
    // text file needed for bonus challenge only
    static final String textFilePath = "./src/dailyprogrammer/easy/" +
            "lettervaluesum399/wordList.txt";
    static final String[] challengeArr = {"", "a", "z", "cab",
            "excellent", "microspectrophotometries"};

    public static void main(String[] args) {
        challenge();
        bonus();
    }

    // sums all letters in word
    // a=1 z=26
    public static int letterSum(String word) {
        int sum = 0;
        for(int i=0; i < word.length(); i++) {
            char letter = word.charAt(i);
            sum += (int)letter -96;
        }
        return sum;
    }

    // prints sum of letters in each challenge word
    public static void challenge() {
        System.out.println("===== Challenge =====");
        for(int i=0; i < challengeArr.length; i++) {
            String word = challengeArr[i];
            System.out.println("letterSum(\"" + word + "\") => " + letterSum(word));
        }
    }

    // finds answers to bonus challenges and prints them
    public static void bonus() {
        int evenCount = 0;
        int oddCount = 0;
        System.out.println("===== Bonus =====");
        try {
            File wordFile = new File(textFilePath);
            Scanner myScanner = new Scanner(wordFile);
            while(myScanner.hasNextLine()) {
                String word = myScanner.nextLine();
                int sum = letterSum(word);
                if(sum == 319)
                    System.out.println(word + " has sum of 319");
                if(sum % 2 == 0)
                    evenCount++;
                else if(sum % 2 == 1)
                    oddCount++;
            }
            myScanner.close();
        } catch(FileNotFoundException e) {
            System.out.println("Caught an error");
            e.printStackTrace();
        }

        System.out.println(oddCount + " odd sums");
    }
}