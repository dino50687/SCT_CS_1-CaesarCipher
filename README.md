# SCT_CS_1-CaesarCipher

A Python implementation of the Caesar Cipher algorithm that can encrypt and decrypt text. This program allows users to input a message and a shift value to perform encryption and decryption operations.

## Features

- **Encryption**: Convert plain text to encrypted text using a shift value
- **Decryption**: Convert encrypted text back to plain text using the same shift value
- **Interactive CLI**: User-friendly command-line interface
- **Character Preservation**: Non-alphabetic characters (numbers, punctuation, spaces) remain unchanged
- **Case Sensitivity**: Maintains original case (uppercase/lowercase) of letters
- **Input Validation**: Ensures shift values are valid integers

## Usage

### Running the Program

```bash
python3 caesar_cipher.py
```

The program will present an interactive menu with the following options:
1. Encrypt text
2. Decrypt text
3. Exit

### Example Usage

**Encryption:**
```
Enter your choice (1-3): 1
Enter the message to encrypt: Hello World!
Enter shift value (integer): 3
Original message: Hello World!
Shift value: 3
Encrypted message: Khoor Zruog!
```

**Decryption:**
```
Enter your choice (1-3): 2
Enter the message to decrypt: Khoor Zruog!
Enter shift value (integer): 3
Encrypted message: Khoor Zruog!
Shift value: 3
Decrypted message: Hello World!
```

## How It Works

The Caesar Cipher is a simple substitution cipher where each letter is shifted by a fixed number of positions in the alphabet:

- **A** with shift 3 becomes **D**
- **Z** with shift 3 becomes **C** (wraps around)
- Non-alphabetic characters remain unchanged

The decryption process uses the same algorithm but with a negative shift value.

## Demo

Run the demonstration script to see various examples:

```bash
python3 demo.py
```

## Files

- `caesar_cipher.py` - Main program with interactive interface
- `demo.py` - Demonstration script showing various examples
- `README.md` - This documentation file
