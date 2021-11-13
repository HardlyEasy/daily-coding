TEXT_FILE_PATH = "./src/dailyprogrammer/easy/lettervaluesum399/wordList.txt"
CHALLENGE_ARR = ["", "a", "z", "cab", "excellent", "microspectrophotometries"]


def main():
    challenge()


def challenge():
    print("===== Challenge =====")
    for i in range(0, len(CHALLENGE_ARR)):
        challenge_word = CHALLENGE_ARR[i]
        print("letter_sum(\"" + challenge_word + "\") => ", end=" ")
        print(letter_sum(challenge_word))


# Sums all letters in word, a = 1 z = 26
def letter_sum(word):
    word_sum = 0
    for i in range(0, len(word)):
        word_sum += ord(word[i]) - ord("`")  # ord() gives ascii int value
    return word_sum


if __name__ == "__main__":
    main()