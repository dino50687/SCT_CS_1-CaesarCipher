````markdown
# Caesar Cipher – Classic Encryption Tool

> **SkillCraft Cybersecurity Internship – Task 1**  
> **Author:** Cherupalli Mani Karthik  
> **Domain:** Cybersecurity

---

## 🚀 Project Overview

Welcome to the **Caesar Cipher Tool**!  
This Python-based command-line utility enables you to **encrypt**, **decrypt**, and **crack** messages using the classical Caesar Cipher algorithm—a foundational concept in cryptography. Developed as part of my internship at SkillCraft Technology, this project demonstrates classical encryption principles, ethical brute-force decryption, and the importance of secure key management.

---

## ✨ Features

- 🔒 **Encrypt messages** with a user-defined key  
- 🔓 **Decrypt messages** using a known key  
- 🕵️‍♂️ **Brute-force decryption** when the key is unknown  
- 🖥️ Simple and intuitive **command-line interface**  
- ✅ Handles only **uppercase English letters (A–Z)**; spaces and symbols remain unchanged

---

## 🎯 Learning Outcomes

- Gained practical knowledge of classical substitution ciphers  
- Implemented encryption and decryption logic in Python  
- Practiced ethical brute-force decryption techniques  
- Enhanced skills in code structure and user-friendly CLI design

---

## 🛠️ Usage Examples

### 1. Encrypt a Message

```bash
python main.py encrypt --text "HELLO WORLD" --key 3
```
**Output:**
```
Original Text : HELLO WORLD  
Encrypted Text: KHOOR ZRUOG
```

---

### 2. Decrypt with a Known Key

```bash
python main.py decrypt --text "KHOOR ZRUOG" --key 3
```
**Output:**
```
Encrypted Text: KHOOR ZRUOG  
Decrypted Text: HELLO WORLD
```

---

### 3. Brute-force Decryption (Unknown Key)

```bash
python main.py brute --text "KHOOR ZRUOG"
```
**Output:**
```
Trying all possible keys...  
Key 1: JGNNQ YQTNF  
Key 2: IFMMP XPSME  
Key 3: HELLO WORLD  <-- Most likely correct  
Key 4: GDKKN VNQKC  
Key 5: FCJJM UMPJB  
...
Key 25: IDMMN XPTME
```

---

## ⚠️ Notes

- **Only uppercase English letters (A–Z) are encrypted**—spaces and symbols remain unchanged  
- **Key must be between 1 and 25** (due to the 26-letter English alphabet rotation)
- The tool is intended for educational and ethical use only

---

## 📚 About the Caesar Cipher

The Caesar Cipher is one of the simplest and most widely known encryption techniques. It’s a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down the alphabet. While not suitable for modern security, it's a great way to learn the basics of cryptography!

---

> **Explore. Encrypt. Educate.**  
> *Thank you for checking out this project!*

````
