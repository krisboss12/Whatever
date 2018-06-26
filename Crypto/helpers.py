def alphabet_position(letter):
    import string
    if letter.islower():
        position = string.ascii_lowercase.index(letter)
    else:
        position = string.ascii_uppercase.index(letter)
    return position

def rotate_character(char, rot):
    import string
    new_char = alphabet_position(char)
    new_char = new_char + rot
    new_char = new_char % 26
    if char.islower():
        new_char = string.ascii_lowercase[new_char]
    else:
        new_char = string.ascii_uppercase[new_char]
    return new_char
