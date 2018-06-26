from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    import string
    encrypt_text = ""
    for char in text:
        if char.isalpha():
            encrypt_char = rotate_character(char, rot)
            encrypt_text = encrypt_text + encrypt_char
        else:
            encrypt_char = char
            encrypt_text = encrypt_text + encrypt_char

    return encrypt_text

def main():
    text = raw_input("Type a message:")
    rot = raw_input("Rotate by:")
    rot = int(rot)
    print(encrypt(text, rot))

if __name__ == '__main__':
    main()
