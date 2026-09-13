## Bilingual Caesar Cipher - English + Korean
## This combines both encryption methods!

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

# Get input from user
msg = input("Enter message (English/Korean/Both): ")
shiftstr = input("Enter shift amount: ")
shift = int(shiftstr)

# Encrypt
encrypted = encode_bilingual(msg, shift)

print()
print("Encrypted: " + encrypted)
print()
print("Tips:")
print(f"   - To decrypt English: use shift {26 - shift}")
print(f"   - To decrypt Korean: use shift {HANGUL_COUNT - shift}")
print("=" * 70)
