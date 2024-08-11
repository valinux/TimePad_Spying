import json
from cryptography.fernet import Fernet

def load_encrypted_mapping(filename, key):
    """Load and decrypt the mapping from a JSON file."""
    fernet = Fernet(key)
    with open(filename, 'rb') as f:
        encrypted_mapping = f.read()
    
    decrypted_mapping = fernet.decrypt(encrypted_mapping).decode()
    return json.loads(decrypted_mapping)

def decode_message(encoded_message, pad):
    """Decode the encoded message using the one-time pad."""
    decoded_numeric = []
    for e, p in zip(encoded_message, pad):
        decoded_digit = (int(e) - int(p)) % 10
        decoded_numeric.append(str(decoded_digit))
    return ''.join(decoded_numeric)

def numbers_to_text(numeric_message, mapping):
    """Convert a numeric message back to text using the word-to-number mapping."""
    inverted_mapping = {v: k for k, v in mapping.items()}  # Invert mapping
    words = []
    
    # Split numeric message into chunks of 4 digits
    for i in range(0, len(numeric_message), 4):
        number = numeric_message[i:i+4]
        word = inverted_mapping.get(number, '')
        if word:
            words.append(word)
    
    return ' '.join(words)

def format_with_spaces(message):
    """Format a string of digits to include spaces every four digits."""
    return ' '.join(message[i:i+4] for i in range(0, len(message), 4))

# Input the encoded message and one-time pad
encoded_message = input("Enter the encoded message: ")
one_time_pad = input("Enter the one-time pad (space-separated): ").replace(" ", "")  # Remove spaces for processing
key = input("Enter the encryption key: ").encode()  # Key must be bytes

# Load the encrypted word mapping from the JSON file
word_mapping = load_encrypted_mapping('word_mapping.json', key)

# Decode the numeric message
decoded_numeric_message = decode_message(encoded_message.replace(" ", ""), one_time_pad)  # Remove spaces for decoding

# Convert back to text
decoded_text_message = numbers_to_text(decoded_numeric_message, word_mapping)

# Format the decoded numeric message with spaces
formatted_decoded_numeric_message = format_with_spaces(decoded_numeric_message)

# Output the results
print(f"\nDecoded Numeric Message: {formatted_decoded_numeric_message}")
print(f"Decoded Text Message: {decoded_text_message}")
