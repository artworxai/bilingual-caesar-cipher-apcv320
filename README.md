# Bilingual Caesar Cipher (English + Korean)

A Python implementation of a Caesar cipher capable of concurrently processing and encrypting mixed English and Korean (Hangul) text within the same input string.

## Features

* **Dual-Language Support**: Handles English Latin characters (`A-Z`, `a-z`) and Korean Hangul syllables (`가`-`힣`) in a single pass.
* **Preserves Unicodes**: Non-alphabetic characters, spaces, punctuation, and digits remain untouched.
* **Modular Shift Logic**: Uses standard modulo arithmetic ($26$ for English, $11{,}172$ for Korean Hangul blocks).

## How It Works

1. **English Subsets**: Standard 26-letter modulo shift applied independently to uppercase and lowercase ASCII ranges.
2. **Korean Hangul Block**: Uses the standard Unicode range `0xAC00` (`가`) through `0xD7A3` (`힣`). The script calculates the relative offset within the 11,172 Syllables block, shifts by the user input, and maps back to valid Unicode characters.

## Usage

Run the script directly using Python 3:

```bash
python bilingual_caesar.py
