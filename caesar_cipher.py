#!/usr/bin/env python3
"""
Caesar Cipher Program
Creates a program that can encrypt and decrypt text using the Caesar Cipher algorithm.
Allows users to input a message and a shift value to perform encryption and decryption.
"""


def caesar_encrypt(text, shift):
    """
    Encrypt text using Caesar Cipher algorithm.
    
    Args:
        text (str): The text to encrypt
        shift (int): The number of positions to shift each letter
    
    Returns:
        str: The encrypted text
    """
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            if char.isupper():
                # Shift uppercase letters (A-Z)
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Shift lowercase letters (a-z)
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result


def caesar_decrypt(text, shift):
    """
    Decrypt text using Caesar Cipher algorithm.
    
    Args:
        text (str): The text to decrypt
        shift (int): The number of positions that were used to shift each letter
    
    Returns:
        str: The decrypted text
    """
    # Decryption is just encryption with negative shift
    return caesar_encrypt(text, -shift)


def get_valid_shift():
    """
    Get a valid shift value from user input.
    
    Returns:
        int: A valid shift value
    """
    while True:
        try:
            shift = int(input("Enter shift value (integer): "))
            return shift
        except ValueError:
            print("Error: Please enter a valid integer for the shift value.")


def main():
    """
    Main function to run the Caesar Cipher program with user interaction.
    """
    print("=== Caesar Cipher Program ===")
    print("This program can encrypt and decrypt text using the Caesar Cipher algorithm.")
    print()
    
    while True:
        print("\nChoose an operation:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            # Encryption
            message = input("\nEnter the message to encrypt: ")
            shift = get_valid_shift()
            encrypted = caesar_encrypt(message, shift)
            print(f"\nOriginal message: {message}")
            print(f"Shift value: {shift}")
            print(f"Encrypted message: {encrypted}")
            
        elif choice == '2':
            # Decryption
            message = input("\nEnter the message to decrypt: ")
            shift = get_valid_shift()
            decrypted = caesar_decrypt(message, shift)
            print(f"\nEncrypted message: {message}")
            print(f"Shift value: {shift}")
            print(f"Decrypted message: {decrypted}")
            
        elif choice == '3':
            print("\nThank you for using the Caesar Cipher program!")
            break
            
        else:
            print("\nError: Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()