def encrypt_withkey(text, keytext):
    import string
    keycount = len(keytext)
    index = 0
    encrypt_text = ""
    for char in text:
        if char.isalpha():
            if index >= keycount:
                rot = keytext[(index % keycount)]
            else:
                rot = keytext[index]
            rot = alphabet_position(rot)
            encrypt_char = rotate_character(char, rot)
            encrypt_text = encrypt_text + encrypt_char
            index = index + 1
        else:
            encrypt_char = char
            encrypt_text = encrypt_text + encrypt_char
    return encrypt_text

def main():
    text = input("Type a message:")
    keytext = input("Encryption Key:")
    print(encrypt_withkey(text, keytext))

if __name__ == '__main__':
    main()
