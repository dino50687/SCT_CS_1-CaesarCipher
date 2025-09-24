#!/usr/bin/env python3
"""
Enhanced Caesar Cipher Program
Allows users to encrypt and decrypt text with custom shift values
"""

def caesar_encrypt(text, shift):
    """
    Encrypts text using Caesar Cipher algorithm.
    
    Args:
        text (str): The message to encrypt
        shift (int): Number of positions to shift each letter
        
    Returns:
        str: The encrypted message
    """
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    """
    Decrypts text using Caesar Cipher algorithm.
    
    Args:
        text (str): The message to decrypt
        shift (int): Number of positions that were used to encrypt
        
    Returns:
        str: The decrypted message
    """
    return caesar_encrypt(text, -shift)

def get_valid_shift():
    """Get a valid shift value from user input."""
    while True:
        try:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Please enter a shift value between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_operation_choice():
    """Get the user's choice for encrypt or decrypt."""
    while True:
        choice = input("Choose operation:\n  [e] Encrypt\n  [d] Decrypt\n  Enter choice (e/d): ").lower().strip()
        if choice in ['e', 'encrypt']:
            return 'encrypt'
        elif choice in ['d', 'decrypt']:
            return 'decrypt'
        else:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

def display_header():
    """Display program header and information."""
    print("=" * 50)
    print("          CAESAR CIPHER PROGRAM")
    print("=" * 50)
    print("This program encrypts and decrypts text using the Caesar Cipher.")
    print("Features:")
    print("• Preserves letter case (uppercase/lowercase)")
    print("• Numbers and symbols remain unchanged")
    print("• Supports shift values from 1 to 25")
    print("-" * 50)

def demonstrate_cipher():
    """Show a quick example of how the cipher works."""
    print("\nQuick Example:")
    example_text = "Hello World!"
    example_shift = 3
    encrypted = caesar_encrypt(example_text, example_shift)
    decrypted = caesar_decrypt(encrypted, example_shift)
    
    print(f"Original:  '{example_text}'")
    print(f"Encrypted: '{encrypted}' (shift = {example_shift})")
    print(f"Decrypted: '{decrypted}'")
    print("-" * 50)

def main():
    """Main program function."""
    display_header()
    demonstrate_cipher()
    
    while True:
        print("\nEnter your message (or type 'quit' to exit):")
        message = input("Message: ")
        
        # Check for exit condition
        if message.lower() in ['quit', 'exit', 'q']:
            print("Thank you for using Caesar Cipher Program!")
            break
        
        # Validate non-empty message
        if not message.strip():
            print("Please enter a valid message.")
            continue
        
        # Get operation choice and shift value
        operation = get_operation_choice()
        shift = get_valid_shift()
        
        # Perform the operation
        if operation == 'encrypt':
            result = caesar_encrypt(message, shift)
            operation_name = "Encryption"
        else:
            result = caesar_decrypt(message, shift)
            operation_name = "Decryption"
        
        # Display results
        print("\n" + "=" * 40)
        print(f"Operation: {operation_name}")
        print(f"Shift Value: {shift}")
        print(f"Original:  '{message}'")
        print(f"Result:    '{result}'")
        print("=" * 40)
        
        # Ask if user wants to continue
        continue_choice = input("\nPerform another operation? (y/n): ").lower().strip()
        if continue_choice not in ['y', 'yes']:
            print("Thank you for using Caesar Cipher Program!")
            break

if __name__ == "__main__":
    main()