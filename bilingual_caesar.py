## Bilingual Caesar Cipher - English + Korean
## This combines both encryption methods!

import unicodedata

# Korean Hangul constants
HANGUL_START = 0xAC00  # '가'
HANGUL_END = 0xD7A3    # '힣'
HANGUL_COUNT = HANGUL_END - HANGUL_START + 1  # 11,172 syllables

def encode_bilingual(msg, shift):
    """
    Encrypts BOTH English and Korean characters in the same message!

    How it works:
        - English uppercase letters (A-Z) are shifted within A-Z
        - English lowercase letters (a-z) are shifted within a-z
        - Korean Hangul syllables (가-힣) are shifted within the Hangul range
        - Everything else (numbers, punctuation, spaces) stays the same

    To decrypt, call it again with the negative shift (e.g. 25 -> -25).
    """

    newmsg = ""

    for ch in msg:
        char_code = ord(ch)

        # Check: Is it an English uppercase letter?
        if 'A' <= ch <= 'Z':
            newch = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            newmsg = newmsg + newch

        # Check: Is it an English lowercase letter?
        elif 'a' <= ch <= 'z':
            newch = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            newmsg = newmsg + newch

        # Check: Is it a Korean Hangul character?
        elif HANGUL_START <= char_code <= HANGUL_END:
            position = char_code - HANGUL_START
            new_position = (position + shift) % HANGUL_COUNT
            newch = chr(new_position + HANGUL_START)
            newmsg = newmsg + newch

        # Everything else: keep as-is
        else:
            newmsg = newmsg + ch

    return newmsg


# Main program
print("=" * 70)
print("BILINGUAL CAESAR CIPHER - 이중언어 카이사르 암호")
print("Encrypts both English AND Korean in the same message!")
print("=" * 70)
print()

# Keep running until the user quits, so you can encrypt AND decrypt
# in the same session
while True:
    print("Choose: [E] Encrypt   [D] Decrypt   [Q] Quit")
    choice = input("> ").strip().upper()

    if choice == "Q":
        print("Goodbye! 안녕히 가세요!")
        break

    if choice not in ("E", "D"):
        print("Please type E, D, or Q.")
        print()
        continue

    # Get input from user
    msg = input("Enter message (English/Korean/Both): ")

    # Some apps paste Korean as separate pieces (ㅇ+ㅏ+ㄴ) instead of whole
    # syllables (안). NFC joins them back into syllables so they get encrypted.
    msg = unicodedata.normalize("NFC", msg)

    shiftstr = input("Enter shift amount: ")
    try:
        shift = int(shiftstr)
    except ValueError:
        print("The shift must be a whole number, like 3 or 25.")
        print()
        continue

    # Decrypting is just encrypting with the opposite shift
    if choice == "D":
        shift = -shift

    result = encode_bilingual(msg, shift)

    # Show the real input, since some phone consoles garble the typed line
    print()
    print("You entered: " + msg)
    if choice == "E":
        print("Encrypted:   " + result)
    else:
        print("Decrypted:   " + result)
    print("=" * 70)
    print()
