EX_WARMUP = [('a', 0), ('a', 1), ('a', 5), ('a', 26), ('d', 15),
                ('z', 1), ('q', 22)]

EX_CHALLENGE = [('a', 1), ('abcz', 1), ('irk', 13), ('fusion', 6),
                ('dailyprogrammer', 6), ('jgorevxumxgsskx', 20)]

EX_BONUS1 = [('Daily Progammer!', 6)]

EX_BONUS2 = ['Zol abyulk tl puav h ulda.', 
            'Tfdv ef wlikyvi, wfi uvrky rnrzkj pfl rcc nzky erjkp, szx, gfzekp kvvky.',
            'Qv wzlmz bw uiqvbiqv iqz-axmml dmtwkqbg, i aeittwe vmmla bw jmib qba eqvoa nwzbg-bpzmm bquma mdmzg amkwvl, zqopb?']

FREQ_TABLE = [3,-1,1,1,4,0,0,2,2,-5,-2,1,0,2,3,0,-6,2,2,3,1,-1,0,-5,0,-7]

def shift_letter(letter: str, number: int) -> str:
    """caesar shifts a lower or upper letter
    """
    shift_amt = number % 26
    raw_advance = ord(letter) + shift_amt
    if (letter.islower() and raw_advance > ord('z')
        or letter.isupper() and raw_advance > ord('Z')):
        # wrap required
        return chr(raw_advance - 26)
    # no wrap
    return chr(raw_advance)

def shift_full(s: str, number: int) -> str:
    """caesar shifts entire string
    """
    full = ''
    for letter in s:
        if letter.isalpha():
            full += shift_letter(letter, number)
        else:
            full += letter
    return full

def guess_cipher(s: str) -> str:
    """caesar shifts a string between 0 and 26
    calculates score of each shift
    picks best score and returns it as best guess
    """
    guess_list = []
    for i in range(0, 27):
        score = 0
        # shift
        shifted_str = shift_full(s, i)
        for letter in shifted_str:
            if letter.isalpha():
                # best score calc using given freq table
                score += FREQ_TABLE[ord(letter.lower()) - ord('a')]
        guess_list.append((shifted_str, score))
    # best guess
    return max(guess_list, key=lambda guess : guess[1])

def main():
    for ex in EX_WARMUP:
        print('warmup(\'%s\', %i) => %s' % \
            (ex[0], ex[1], shift_letter(ex[0], ex[1])))
    for ex in EX_CHALLENGE:
        print('challenge(\'%s\', %i) => %s' % \
            (ex[0], ex[1], shift_full(ex[0], ex[1])))
    for ex in EX_BONUS1:
        print('bonus1(\'%s\', %i) => %s' % \
            (ex[0], ex[1], shift_full(ex[0], ex[1])))
    for ex in EX_BONUS2:
        print('bonus2(\'%s\') => %s' % (ex, guess_cipher(ex)))

if __name__ == "__main__":
    main()