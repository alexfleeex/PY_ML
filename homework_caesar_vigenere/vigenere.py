from string import ascii_uppercase, ascii_lowercase

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword=(keyword*len(plaintext))[:len(plaintext)]
    for i in range(len(plaintext)):
        if plaintext[i] in ascii_lowercase:
            ciphertext+=ascii_lowercase[(ascii_lowercase.find(plaintext[i]) + ascii_lowercase.find(keyword[i])) % 26]
        elif plaintext[i] in ascii_uppercase:
            ciphertext += ascii_uppercase[(ascii_uppercase.find(plaintext[i]) + ascii_uppercase.find(keyword[i])) % 26]
        else:
            ciphertext+=plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = (keyword * len(ciphertext))[:len(ciphertext)]
    for i in range(len(ciphertext)):
        if ciphertext[i] in ascii_lowercase:
            plaintext += ascii_lowercase[(ascii_lowercase.find(ciphertext[i]) - ascii_lowercase.find(keyword[i])+26) % 26]
        elif ciphertext[i] in ascii_uppercase:
            plaintext += ascii_uppercase[(ascii_uppercase.find(ciphertext[i]) - ascii_uppercase.find(keyword[i]) + 26) % 26]
        else:
            plaintext += ciphertext[i]
    return plaintext

