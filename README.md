<br><b>The best practice to meet your favorite unknown person online IRL is to USE this time pad and microdots with the encoded msg</br></b>


# One-Time Pad Encoder/Decoder for Number Stations

This repository contains Python scripts for encoding and decoding messages using a one-time pad (OTP). It simulates the concept of number stations by converting messages into numeric form, encoding them with a randomly generated OTP, and then allowing for decoding of those messages.
```markdown
## Features

- Encode messages into numeric form.
- Generate a unique one-time pad for each message.
- Decode numeric messages back into the original text.
- Supports alphanumeric characters, spaces, and special characters (e.g., `:`, `.`, `,`, etc.).

## Requirements

- Python 3.x
- No additional libraries are required as the code uses built-in Python modules.
```
## Usage

### Encoding a Message

1. Clone this repository:
   ```bash
   git clone https://github.com/valinux/Number-Station.git
   cd repo-name
   ```

2. Run the encoding script:
   ```bash
   python timepad1.py
   ```

3. When prompted, enter the message you want to encode. For example:
   ```
   Enter the message you want to send: MEET ME AT 09:00
   ```

4. The output will display:
   - The original text message.
   - The numeric representation of the message.
   - The generated one-time pad.
   - The encoded numeric message.

### Decoding a Message

1. Run the decoding script:
   ```bash
   python timepad2.py
   ```

2. When prompted, enter the encoded message and the one-time pad you received from the encoding step:
   ```
   Enter the encoded message: [your_encoded_message]
   Enter the one-time pad: [your_one_time_pad]
   ```

3. The output will show:
   - The decoded numeric message.
   - The decoded text message.

## Example

### Encoding Example
```plaintext
Enter the message you want to send: MEET ME AT 09:00

Original Text Message: MEET ME AT 09:00
Numeric Message: 13050520631305270964096300
One-Time Pad: 83618460785701243067285794
Encoded Message: 99668974417103620451089694
```

### Decoding Example
```plaintext
Enter the encoded message: 99668974417103620451089694
Enter the one-time pad: 83618460785701243067285794

Decoded Numeric Message: 13050520631305270964096300
Decoded Text Message: MEET ME AT 09:00
```

## Important Note
- **One-Time Pad Security**: Each one-time pad must be unique and used only once. Reusing a one-time pad can compromise the security of the encoded messages.
