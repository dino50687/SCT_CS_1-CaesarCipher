#!/usr/bin/env python3
"""
Demo script to showcase the Caesar Cipher functionality
"""

from caesar_cipher import caesar_encrypt, caesar_decrypt

def demo_caesar_cipher():
    """Demonstrate Caesar Cipher encryption and decryption"""
    print("=== Caesar Cipher Demo ===\n")
    
    # Demo cases
    demo_cases = [
        ("Hello World!", 3),
        ("Python Programming", 5),
        ("The quick brown fox jumps over the lazy dog", 13),
        ("ABC xyz 123!", 1)
    ]
    
    for i, (message, shift) in enumerate(demo_cases, 1):
        print(f"Demo {i}:")
        print(f"Original Message: '{message}'")
        print(f"Shift Value: {shift}")
        
        # Encrypt
        encrypted = caesar_encrypt(message, shift)
        print(f"Encrypted: '{encrypted}'")
        
        # Decrypt
        decrypted = caesar_decrypt(encrypted, shift)
        print(f"Decrypted: '{decrypted}'")
        
        # Verify
        print(f"Verification: {'✓ SUCCESS' if message == decrypted else '✗ FAILED'}")
        print("-" * 50)

if __name__ == "__main__":
    demo_caesar_cipher()