#!/usr/bin/env python3
"""
Quick test of the Caesar Cipher functions
"""

def caesar_encrypt(text, shift):
    """Encrypts text using Caesar Cipher algorithm."""
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    """Decrypts text using Caesar Cipher algorithm."""
    return caesar_encrypt(text, -shift)

# Test the functions
print("CAESAR CIPHER - FUNCTIONALITY TEST")
print("=" * 40)

# Test cases
test_cases = [
    ("Hello World!", 3),
    ("PYTHON", 5),
    ("test123!", 7),
    ("ABC xyz", 1),
    ("", 10)  # Empty string edge case
]

all_passed = True

for i, (message, shift) in enumerate(test_cases, 1):
    # Test encryption and decryption
    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    
    # Verify round-trip works
    test_passed = (message == decrypted)
    if not test_passed:
        all_passed = False
    
    status = "✓ PASS" if test_passed else "✗ FAIL"
    
    print(f"Test {i}: {status}")
    print(f"  Original:  '{message}'")
    print(f"  Shift:     {shift}")
    print(f"  Encrypted: '{encrypted}'")
    print(f"  Decrypted: '{decrypted}'")
    print(f"  Round-trip: {'SUCCESS' if test_passed else 'FAILED'}")
    print("-" * 40)

print(f"Overall Result: {'ALL TESTS PASSED ✓' if all_passed else 'SOME TESTS FAILED ✗'}")

# Show some practical examples
print("\nPRACTICAL EXAMPLES:")
print("-" * 40)

examples = [
    ("Meet me at midnight", 13),
    ("Secret Code", 4), 
    ("Python Programming!", 8)
]

for msg, shift in examples:
    encrypted = caesar_encrypt(msg, shift)
    print(f"'{msg}' → '{encrypted}' (shift {shift})")

print("\nThe Caesar Cipher program is ready to use!")