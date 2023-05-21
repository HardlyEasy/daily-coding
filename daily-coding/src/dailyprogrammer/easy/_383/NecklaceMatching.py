import re

EXAMPLES = '''same_necklace("nicole", "lenico") => true
same_necklace("nicole", "icolen") => true
same_necklace("nicole", "coneli") => false
same_necklace("aabaaaaabaab", "aabaabaabaaa") => true
same_necklace("abc", "cba") => false
same_necklace("xxyyy", "xxxyy") => false
same_necklace("xyxxz", "xxyxz") => false
same_necklace("x", "x") => true
same_necklace("x", "xx") => false
same_necklace("x", "") => false
same_necklace("", "") => true'''.split('\n')

def get_pairs() -> list:
    pairs = []
    for s in EXAMPLES:
        # regex matches text within double quotes
        l = re.findall('"(.*?)"', s)
        pairs.append(tuple(l))
    return pairs

def same_necklace(s1: str, s2: str):
    if len(s1) != len(s2):  # special case
        return False
    elif len(s1) == 0 and len(s2) == 0:  # special case
        return True
    for i in range(0, len(s2)):
        if s1 == s2:
            return True
        s1 = s1[1:] + s1[0]
    return False

def main():
    for (s1, s2) in get_pairs():
        print('same_necklace(%s, %s) => %s' % (s1, s2, same_necklace(s1, s2)))

if __name__ == "__main__":
    main()