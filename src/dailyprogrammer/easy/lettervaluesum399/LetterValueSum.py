TEXT_FILE_PATH = "./src/dailyprogrammer/easy/lettervaluesum399/wordList.txt"
CHALLENGE_ARR = ["", "a", "z", "cab", "excellent", "microspectrophotometries"]


def challenge():
    print('===== Challenge =====')
    for i in range(0, len(CHALLENGE_ARR)):
        challenge_word = CHALLENGE_ARR[i]
        print('letter_sum(\"' + challenge_word + '\") => ', end=" ")
        print(letter_sum(challenge_word))


def bonus():
    f = open('wordList.txt', 'r')
    lines = f.readlines()
    for word in lines:
        word = word.strip()  # remove new line
        word_sum = letter_sum(word)
        if sum == 319:
            print(word)


def letter_sum(word):
    """ Sums all letters in word, a = 1 z = 26

    :param word:
    :type word: str
    :return: Sum of all letters in word
    :rtype: int
    """
    word_sum = 0
    for i in range(0, len(word)):
        word_sum += ord(word[i]) - ord("`")  # ord() gives ascii int value
    return word_sum


def main():
    challenge()
    bonus()


if __name__ == '__main__':
    main()