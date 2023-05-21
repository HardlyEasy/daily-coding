INPUT = ['xxxyyyzzz', 'abccbaabccba', 'xxxyyyzzzz', 
        'abcdefghijklmnopqrstuvwxyz', 'pqq', 'fdedfdeffeddefeeeefddf',
        'www', 'x', '']

def count_letters() -> dict:
    letter_dict = dict()
    for ch in s:
        if ch not in letter_dict:
            letter_dict[ch] = 1
        else:
            letter_dict[ch] += 1
    return letter_dict

def balanced_bonus(s: str) -> bool:
    """steps
    1) count_letter() : count letters and store in dict
    2) handle 0 or 1 letter
    3) handle 2 letter and above
    """
    letter_dict = count_letters()
    if len(letter_dict) <= 1:  # 0 or 1 letter
        return True
    last_c = letter_dict.popitem()[1]
    for count in letter_dict.values():
        if last_c != count:
            return False
    return True

def main():
    for i in range(0, len(INPUT), +1):
        print('balanced_bonus("%s") => %s' % \
            (INPUT[i], balanced_bonus(INPUT[i])))

if __name__ == '__main__':
    main()