import os
import random
import json
import secrets
from cryptography.fernet import Fernet

def generate_strong_mapping(words):
    """Generate a mapping from words to unique numbers."""
    unique_numbers = set()
    mapping = {}

    for word in words:
        while True:
            number = secrets.randbelow(10000)  # Generate a number between 0 and 9999
            if number not in unique_numbers:
                unique_numbers.add(number)
                mapping[word] = str(number).zfill(4)  # Store the number
                break
                
    return mapping

def encode_message(message, pad):
    """Encode the numeric message using the one-time pad."""
    encoded_message = []
    for m, p in zip(message, pad):
        encoded_digit = (int(m) + int(p)) % 10
        encoded_message.append(str(encoded_digit))
    return ''.join(encoded_message)

def text_to_numbers(text, mapping):
    """Convert a text message to a numeric message using word-to-number mapping."""
    words = text.split()
    numeric_message = []
    
    for word in words:
        number = mapping.get(word.upper(), '0000')  # Default to '0000' if not found
        numeric_message.append(number)
    
    # Join numbers with spaces
    return ' '.join(numeric_message)

def format_with_spaces(message):
    """Format a string of digits to include spaces every four digits."""
    return ' '.join(message[i:i+4] for i in range(0, len(message), 4))

def save_encrypted_mapping(mapping, filename, key):
    """Encrypt and save the mapping to a JSON file."""
    fernet = Fernet(key)
    mapping_json = json.dumps(mapping).encode()
    encrypted_mapping = fernet.encrypt(mapping_json)
    
    with open(filename, 'wb') as f:
        f.write(encrypted_mapping)

# Input the original message
original_text_message = input("Enter the message you want to send: ")

# Generate word-to-number mapping from the original message
words = list(set(original_text_message.split()))  # Unique words
word_mapping = generate_strong_mapping(words)

# Convert to numeric format using word mapping
numeric_message = text_to_numbers(original_text_message, word_mapping)

# Generate a shorter one-time pad
pad = [str(secrets.randbelow(10)) for _ in range(len(numeric_message.replace(" ", "")))] # Length should match the numeric message without spaces
pad_str = ''.join(pad)

# Encode the numeric message
encoded_message = encode_message(numeric_message.replace(" ", ""), pad_str)  # Remove spaces for encoding

# Format the numeric message, one-time pad, and encoded message with spaces
formatted_numeric_message = format_with_spaces(numeric_message.replace(" ", ""))
formatted_pad = format_with_spaces(pad_str)
formatted_encoded_message = format_with_spaces(encoded_message)

# Output the results
print(f"\nOriginal Text Message: {original_text_message}")
print(f"Numeric Message: {formatted_numeric_message}")
print(f"One-Time Pad: {formatted_pad}")  # Display the one-time pad in chunks
print(f"Encoded Message: {formatted_encoded_message}")

# Generate a key for encryption
key = Fernet.generate_key()
# Save the encrypted word mapping to a JSON file
save_encrypted_mapping(word_mapping, 'word_mapping.json', key)

# Print the encryption key (store this securely for decoding)
print(f"Encryption Key (store securely): {key.decode()}")
