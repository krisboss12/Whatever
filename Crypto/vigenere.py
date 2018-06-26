from helpers import alphabet_position, rotate_character

def encrypt(text, keytext):
    import string
    keycount = len(keytext)
    index = 0
    encrypt_text = ""
    for char in text:
        if char.isalpha():
            rot = keytext[(index % keycount)]
            rot = alphabet_position(rot)
            encrypt_char = rotate_character(char, rot)
            encrypt_text = encrypt_text + encrypt_char
            index = index + 1
        else:
            encrypt_char = char
            encrypt_text = encrypt_text + encrypt_char
    return encrypt_text

def main():
    text = raw_input("Type a message:")
    keytext = raw_input("Encryption Key:")
    print(encrypt(text, keytext))

if __name__ == '__main__':
    main()
