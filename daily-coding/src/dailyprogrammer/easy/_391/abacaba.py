def sequencer(n: int):
    """given number of sequences, returns last sequence
    """
    seq = 'a'
    for i in range(1, n):  # ex: n = 5, builds up seq 2-5, returns seq 5
        seq = seq + next_letter(i) + seq
    return seq

def next_letter(i: int):
    """given iteration number, returns middle letter
    """
    return chr(ord('a') + i)

print(next_letter(1))
print(sequencer(5))