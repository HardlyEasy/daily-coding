TEXT_FILE_PATH = "./src/dailyprogrammer/easy/lettervaluesum399/wordList.txt"
CHALLENGE_ARR = ["", "a", "z", "cab", "excellent", "microspectrophotometries"]


def letter_sum(word):
    """ Sums all letters in word, a = 1 z = 26

    :param str word: Can be garbled nonsense characters
    :return: Sum of all letters in word
    :rtype: int
    """
    summed = 0
    for i in range(0, len(word)):
        summed += ord(word[i]) - ord("`")  # ord() gives ascii int value
    return summed


def challenge():
    """ Finds sum of values of letters in CHALLENGE_ARR
    """
    print('===== Challenge =====')
    for i in range(0, len(CHALLENGE_ARR)):
        challenge_word = CHALLENGE_ARR[i]
        print('letter_sum(\"' + challenge_word + '\") => ', end=" ")
        print(letter_sum(challenge_word))


def all_bonus():
    """ Calls upon helper bonus functions
    """
    print('===== Bonus =====')
    f = open('wordList.txt', 'r')
    temp_lines = f.readlines()
    lines = list()
    for line in temp_lines:
        lines.append(line.strip())
    print(bonus1(lines), 'has letter sum of 319')
    print(bonus2(lines), 'words of odd letter sum')
    max_word_sum, max_letter_sum = bonus3(lines)
    print(max_word_sum, 'words with letter sum of', max_letter_sum)
    # TODO: not done yet
    # print(bonus4(lines))


def bonus1(lines):
    """ microspectrophotometries is the only word with a letter sum of 317.
    Find the only word with a letter sum of 319.

    :param list lines: contains words
    :return: the word with letter sum of 319
    :rtype: str
    """
    for word in lines:
        summed = letter_sum(word)
        if summed == 319:
            return word


def bonus2(lines):
    """ How many words have an odd letter sum?

    :param list lines: contains words
    :return: number of odd letter sums
    :rtype: int
    """
    odd_count = 0
    even_count = 0
    for word in lines:
        summed = letter_sum(word)
        if summed % 2 == 0:
            even_count += 1
        elif summed % 2 == 1:
            odd_count += 1
    return odd_count


def bonus3(lines):
    """ There are 1921 words with a letter sum of 100, making it the second
    most common letter sum. What letter sum is most common, and how many words
    have it?

    :param list lines: contains words
    :return: (number of words, most common letter sum)
    :rtype: (int, int)
    """
    sum_count_dict = dict()  # key of letter sum, value of count
    for word in lines:
        summed = letter_sum(word)
        if summed in sum_count_dict:
            sum_count_dict[summed] += 1
        else:
            sum_count_dict[summed] = 1

    max_num_words = 0
    max_letter_sum = 0
    for summed, num_words in sum_count_dict.items():
        if num_words > max_num_words:
            max_letter_sum = summed
            max_num_words = num_words
    return max_num_words, max_letter_sum


# TODO: partially done
def bonus4(lines):
    """ zyzzyva and biodegradabilities have the same letter sum as each other
    (151), and their lengths differ by 11 letters. Find the other pair of
    words with the same letter sum whose lengths differ by 11 letters.

    :param list lines: contains words
    :return: (word1, word2)
    :rtype: (str, str)
    """
    lookup_dict = dict()
    '''
    A nested dictionary with key of word length and value of another dictionary
    Inner dictionary key of letter sum, value of list of words
    { 
      1: { 1: ['a'], 2: ['b'], 3: ['c']},
      2: { 3: ['ab', 'ba'], 5: ['cb', 'bc']}, 
    }
    '''
    for word in lines:
        summed = letter_sum(word)
        # create outer dictionary key entry of word length
        if len(word) not in lookup_dict:
            lookup_dict[len(word)] = dict()
        # create inner dictionary key entry of letter sum
        if summed not in lookup_dict[len(word)]:
            lookup_dict[len(word)][summed] = list()
        # add word to inner dictionary
        lookup_dict[len(word)][summed].append(word)
    for word_len in sorted(lookup_dict.keys()):
        if (word_len + 11) not in lookup_dict:
            break
        first_sums = lookup_dict[word_len].keys()
        second_sums = lookup_dict[word_len + 11].keys()
        intersected = set(first_sums).intersection(set(second_sums))
        # Assumed that only 2 words can have same word length and same word sum
        if len(intersected) > 2:
            raise Exception("ERROR: More than 2 words found with same word "
                            "length same word sum")
        if len(intersected) == 1:  # same word length, same word sum pair found
            intersected_word_sum = intersected.pop()
            first_word = lookup_dict[word_len][intersected_word_sum][0]
            second_word = lookup_dict[word_len + 11][intersected_word_sum][0]
            return first_word, second_word


def main():
    challenge()
    all_bonus()


if __name__ == '__main__':
    main()
