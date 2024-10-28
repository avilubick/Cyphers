# CipherTool

## Overview

CipherTool is a Python application designed to perform text encryption and decryption using various cipher techniques. The tool supports both Caesar and substitution ciphers, allowing users to easily encode and decode messages. 

## Features

- **Caesar Cipher**: A simple encryption technique where each letter in the plaintext is shifted a certain number of places down or up the alphabet.
- **Substitution Cipher**: A method where each letter in the plaintext is replaced with a corresponding character or sequence of characters.
- **Dynamic Input Handling**: Users can specify whether they want to encrypt or decrypt text, and select the cipher type interactively.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CipherTool
   ```

2. Ensure you have Python 3 installed on your machine.

## Usage

### Running the Application

1. Open your terminal or command prompt.
2. Navigate to the directory where you cloned the repository.
3. Run the main script:
   ```bash
   python file1.py
   ```

### Interactive Prompt

- The application will prompt you to specify the action:
  - Enter `cypher` to perform encryption/decryption.
  - Enter `detection` to identify the type of cipher used.
- Follow the prompts to input the text, choose the cipher type (Caesar or substitution), and specify whether you want to encrypt or decrypt the text.

### Example Usage

1. To encrypt text using the Caesar cipher:
   ```
   text: hello
   cypher type? (ceaser/substitution): ceaser
   encrypt/decrypt?: encrypt
   ```
   Output: `svool`

2. To decrypt text using the substitution cipher:
   ```
   text: 596475
   cypher type? (ceaser/substitution): substitution
   encrypt/decrypt?: decrypt
   ```
   Output: `dude`

## Important Notes

- **Exit**: You can exit the application at any time by typing `exit` when prompted for text input.
- **Error Handling**: The application includes basic error handling for invalid inputs. Ensure to follow the prompts carefully to avoid errors.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
