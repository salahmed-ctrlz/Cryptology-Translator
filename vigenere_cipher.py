def vigenere_cipher(text, keyword, decode=False):
    result = []
    keyword = keyword.upper()
    keyword_length = len(keyword)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(keyword[i % keyword_length]) - 65
            shift = -shift if decode else shift
            shift_base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            result.append(char)
    return ''.join(result)
