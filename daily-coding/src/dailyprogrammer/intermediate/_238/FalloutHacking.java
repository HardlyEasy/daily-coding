package dailyprogrammer.intermediate._238;

import java.io.File;
import java.io.FileNotFoundException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Random;

public class FalloutHacking {
    static final String WORD_FNAME = "popular_words.txt";
    static final int[] WORD_LEN = {4, 6, 8, 10, 12};
    static final int[] WORD_AMT = {6, 8, 10, 12, 14};
    static final int GUESSES = 4;

    public static int inputDifficulty() {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter difficulty level(0-4): ");
        return scan.nextInt();
    }

    public static ArrayList<String> getWords(int difficulty)
            throws FileNotFoundException {
        /* Scans through entire word text file and puts valid words in list
        Time complexity: O(n)
            n words in word text file
         */
        URL url = FalloutHacking.class.getResource(WORD_FNAME);
        File wordFile = new File(url.getPath());
        Scanner scan = new Scanner(wordFile);
        ArrayList<String> wordList = new ArrayList<String>();

        while (scan.hasNext()) {
            String word = scan.next();
            if (word.length() == WORD_LEN[difficulty])
                wordList.add(word);
        }

        return wordList;
    }

    public static ArrayList<String> pickWords(
            ArrayList<String> wordList, int numWords) {
        /* Randomly picks words from valid words list
         */
        Random rand = new Random();
        ArrayList<String> gameWords = new ArrayList<String>();

        for (int i = 0; i < numWords; i++) {
            int randInt = rand.nextInt(wordList.size());
            gameWords.add(wordList.get(randInt));
        }
        return gameWords;
    }

    public static int findMatchAmt(String guess, String answer) {
        /* Returns number of matching characters between guess and answer
        Assumes guess and answer are same length
         */
        int matchAmt = 0;
        for (int i = 0; i < guess.length(); i++) {
            if (guess.charAt(i) == answer.charAt(i))
                matchAmt++;
        }
        return matchAmt;
    }

    public static void startGame(ArrayList<String> gameWords) {
        /* The "game master"
         */
        Scanner scan = new Scanner(System.in);
        Random rand = new Random();
        // Print out all game words
        for (String gameWord : gameWords)
            System.out.println(gameWord.toUpperCase());
        // Randomly pick an answer word
        String answer = gameWords.get(rand.nextInt(gameWords.size()));
        // Ask for a guess, then print number letters correct
        for (int i = GUESSES; i >= 0; i--) {
            System.out.printf("\nGuess (%d left)? ", i);
            String guess = scan.next();
            int matchAmt = findMatchAmt(guess, answer);
            System.out.printf("%d/%d correct", matchAmt, guess.length());
            if (matchAmt == guess.length()) {
                System.out.println("\nYou win!");
                break;
            }
        }
    }

    public static void main(String[] args) throws FileNotFoundException {
        int diff = inputDifficulty();
        ArrayList<String> wordList = getWords(diff);
        ArrayList<String> gameWords=  pickWords(wordList, WORD_AMT[diff]);
        startGame(gameWords);
    }
}
