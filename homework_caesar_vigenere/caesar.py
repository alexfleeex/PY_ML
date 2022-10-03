import typing as tp
from string import ascii_lowercase, ascii_uppercase


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if i in ascii_lowercase:
            ciphertext += ascii_lowercase[(ascii_lowercase.find(i) + shift) % len(ascii_lowercase)]
        elif i in ascii_uppercase:
            ciphertext += ascii_uppercase[(ascii_uppercase.find(i) + shift) % len(ascii_uppercase)]
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if i.isalpha():
            pos, add = None, None
            if i in ascii_lowercase:
                pos = ascii_lowercase.find(i) - shift
                if pos<0:
                    pos = len(ascii_lowercase) + pos
                add =ascii_lowercase[pos]
            else:
                pos = ascii_uppercase.find(i) - shift
                if pos < 0:
                    pos = len(ascii_uppercase) + pos
                add = ascii_uppercase[pos]
            plaintext += add
        else:
            plaintext += i
    # PUT YOUR CODE HERE
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
