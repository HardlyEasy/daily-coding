# (key, input message)
key1 = 'H GgG d gGg e ggG l GGg o gGG r Ggg w ggg'
input_msg1 = 'GgGggGGGgGGggGG, ggggGGGggGGggGg!'
key2 = 'a GgG d GggGg e GggGG g GGGgg h GGGgG i GGGGg l GGGGG m ggg o GGg ' \
       'p Gggg r gG y ggG'
input_msg2 = 'GGGgGGGgGGggGGgGggG ' \
             '/gG/GggGgGgGGGGGgGGGGGggGGggggGGGgGGGgggGGgGggggggGggGGgG!'
input_msg3 = 'Hello, world!'


def make_encoder_decoder(key: str) -> (dict, dict):
    """Returns a decoder dictionary
    Key of string of g letters
    Value of english letter
    """
    encoder, decoder = dict(), dict()
    split_key = key.split(' ')
    for i in range(0, len(split_key), +2):
        letter, g_letters = split_key[i], split_key[i+1]
        encoder[letter] = g_letters
        decoder[g_letters] = letter
    return encoder, decoder


def decode(decoder: dict, input_msg: str) -> str:
    """Returns decoded input message
    Does this with a sliced input message (left cursor, right cursor) being
    matched with decoder dictionary key
    """
    decoded_msg = ''
    lc, rc = 0, 1
    while lc < len(input_msg):
        sliced_msg = input_msg[lc:rc]
        if 'g' not in sliced_msg and 'G' not in sliced_msg:  # no decoding
            decoded_msg += sliced_msg
            lc, rc = rc, rc + 1
            continue
        while rc <= len(input_msg):  # expand sliced_msg size
            if sliced_msg in decoder:  # found matching key
                decoded_msg += decoder[sliced_msg]
                lc, rc = rc, rc + 1
                break
            rc += 1
            sliced_msg = input_msg[lc:rc]
    return decoded_msg


def encode(encoder: dict, input_msg: str) -> str:
    """Returns an encoded input message
    Goes char by char through input message and references encoder dict
    map to encode properly
    """
    encoded_msg = ''
    for ch in input_msg:
        if not ch.isalpha():  # no decoding
            encoded_msg += ch
        else:
            if ch in encoder:  # found matching key
                encoded_msg += encoder[ch]
            else:
                raise Exception('encode(): No match found for letter')
    return encoded_msg


def main():
    # Decoding
    encoder, decoder = make_encoder_decoder(key1)
    print(decode(decoder, input_msg1))
    encoder, decoder = make_encoder_decoder(key2)
    print(decode(decoder, input_msg2))

    # Encoding
    encoder, decoder = make_encoder_decoder(key1)
    print(encode(encoder, input_msg3))


if __name__ == "__main__":
    main()
