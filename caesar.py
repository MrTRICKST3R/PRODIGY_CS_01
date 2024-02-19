#Caesar Cipher

def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (an integer): "))
    mode = input("Enter 'encrypt' or 'decrypt': ").lower()

    if mode == 'encrypt':
        encrypted_text = caesar_cipher(text, shift)
        print("Encrypted text:", encrypted_text)
    elif mode == 'decrypt':
        decrypted_text = caesar_cipher(text, -shift)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
