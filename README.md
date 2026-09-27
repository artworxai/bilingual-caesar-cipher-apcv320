# Bilingual Caesar Cipher (English + Korean)

A Python implementation of a Caesar cipher that encrypts and decrypts mixed English and Korean (Hangul) text in the same input string.

이중언어 카이사르 암호 — 영어와 한국어를 한 번에 암호화하고 복호화합니다.

## Features

* **Dual-Language Support**: Handles English letters (`A-Z`, `a-z`) and Korean Hangul syllables (`가`-`힣`) in a single pass.
* **Encrypt and Decrypt in One Session**: An interactive menu lets you encrypt, decrypt, and repeat without restarting the script.
* **Same Shift to Decrypt**: Decrypt with the same shift number you encrypted with. The script reverses it for you.
* **Leaves Other Characters Alone**: Spaces, punctuation, digits, and other symbols pass through unchanged.
* **Handles Pasted Korean**: Input is normalized to Unicode NFC, so Korean pasted as separate jamo (`ㅇ`+`ㅏ`+`ㄴ`) is joined into full syllables (`안`) before encrypting.
* **Input Validation**: A non-numeric shift shows a friendly message instead of crashing.

## How It Works

1. **English**: A standard 26-letter modulo shift, applied separately to uppercase and lowercase so case is preserved.
2. **Korean Hangul**: Uses the Unicode Hangul Syllables block, `0xAC00` (`가`) through `0xD7A3` (`힣`). The script finds each syllable's position within the 11,172-syllable block, shifts it, and wraps around with modulo 11,172 so the result is always a valid syllable.
3. **Decryption**: Decrypting is encrypting with the negative shift. Python's `%` operator handles negative numbers, so one function does both jobs.

## Usage

Run the script with Python 3:

```bash
python bilingual_caesar.py
```

Then choose an option from the menu:

```
Choose: [E] Encrypt   [D] Decrypt   [Q] Quit
```

## Example

```
Choose: [E] Encrypt   [D] Decrypt   [Q] Quit
> E
Enter message (English/Korean/Both): Hello. 안녕하세요.
Enter shift amount: 25

You entered: Hello. 안녕하세요.
Encrypted:   Gdkkn. 액녮핱셑욭.

Choose: [E] Encrypt   [D] Decrypt   [Q] Quit
> D
Enter message (English/Korean/Both): Gdkkn. 액녮핱셑욭.
Enter shift amount: 25

You entered: Gdkkn. 액녮핱셑욭.
Decrypted:   Hello. 안녕하세요.
```

## Note for Mobile Users

Some phone Python apps (such as Pyto on iPhone) display the typed line incorrectly when you enter Korean, because Korean characters are double-width and the keyboard composes syllables as you type. The input itself is received correctly. Check the **You entered:** line to see exactly what the script got.

## Requirements

* Python 3.6 or newer (no external libraries)
