import os

def generate_one_time_pad(length):
    """Generate a one-time pad consisting of random digits for a number station."""
    return ''.join(str(os.urandom(1)[0] % 10) for _ in range(length))

def encode_message(message, pad):
    """Encode the numeric message using the one-time pad."""
    encoded_message = []
    for m, p in zip(message, pad):
        encoded_digit = (int(m) + int(p)) % 10
        encoded_message.append(str(encoded_digit))
    return ''.join(encoded_message)

def text_to_numbers(text):
    """Convert a text message to a numeric message."""
    char_map = {char: str(idx).zfill(2) for idx, char in enumerate(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 :.,?!'()@#$%&*+-/=", start=1)}
    char_map[' '] = '63'  # Space maps to '63'
    return ''.join(char_map.get(char, '00') for char in text.upper())

# Input the original message
original_text_message = input("Enter the message you want to send: ")

# Convert to numeric format
numeric_message = text_to_numbers(original_text_message)

# Generate one-time pad
pad = generate_one_time_pad(len(numeric_message))

# Encode the numeric message
encoded_message = encode_message(numeric_message, pad)

# Output the results
print(f"\nOriginal Text Message: {original_text_message}")
print(f"Numeric Message: {numeric_message}")
print(f"One-Time Pad: {pad}")
print(f"Encoded Message: {encoded_message}")
