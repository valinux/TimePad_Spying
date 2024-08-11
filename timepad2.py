def decode_message(encoded_message, pad):
    """Decode the encoded message using the one-time pad."""
    decoded_message = []
    for e, p in zip(encoded_message, pad):
        decoded_digit = (int(e) - int(p)) % 10
        decoded_message.append(str(decoded_digit))
    return ''.join(decoded_message)

def numbers_to_text(numbers):
    """Convert a numeric message back to text."""
    num_map = {str(idx).zfill(2): char for idx, char in enumerate(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 :.,?!'()@#$%&*+-/=", start=1)}
    num_map['63'] = ' '  # '63' maps to space
    # Split numeric message into two-digit groups
    return ''.join(num_map.get(numbers[i:i+2], '?') for i in range(0, len(numbers), 2))

# Input the encoded message and the one-time pad
encoded_message = input("Enter the encoded message: ")
pad = input("Enter the one-time pad: ")

# Decode the numeric message
decoded_numeric_message = decode_message(encoded_message, pad)

# Convert the decoded numeric message back to text
decoded_text_message = numbers_to_text(decoded_numeric_message)

# Output the decoded message
print(f"\nDecoded Numeric Message: {decoded_numeric_message}")
print(f"Decoded Text Message: {decoded_text_message}")
