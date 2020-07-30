from string import ascii_lowercase as alphabet


def encrypt(message, key):
    encrypted = ""

    # this means we can do keys greater than 26 without it breaking
    # and decryption with -key
    key = key % 26

    # first we need to make all the letters lowercase
    message = message.lower()

    for letter in message:
        # if we have a letter and not a space etc...
        if letter in alphabet:
            # get the position of letter in the alphabet
            pos = alphabet.index(letter)

            # shift the letter
            new_pos = pos + key

            # because we can go past 26 we need to wrap new_pos
            new_pos = new_pos % 26

            # translate back into letters
            letter = alphabet[new_pos]

        # add the new character onto our encrypted message
        encrypted = encrypted + letter

    return encrypted


def decrypt(message, key):
    # decryption is just shifting backwards :)
    return encrypt(message, -key)


def main():
    # my favourite pangram :)
    message = "Sphinx of black quartz, judge my vow."
    key = 3

    print(message)

    enc = encrypt(message, key)
    print(enc)

    dec = decrypt(enc, key)
    print(dec)

    assert dec == message.lower()


if __name__ == "__main__":
    main()