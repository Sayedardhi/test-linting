#!/usr/bin/env python3

"""
Stanford CS106A Crypto Project
"""

import sys

# provided ALPHABET constant - list of the regular alphabet
# in lowercase. Refer to this simply as ALPHABET in your code.
# This list should not be modified.
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def compute_slug(key):
    """
    Given a key string, compute and return the len-26 slug list for it.
    >>> compute_slug('z')
    ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> compute_slug('Bananas!')
    ['b', 'a', 'n', 's', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    >>> compute_slug('Life, Liberty, and')
    ['l', 'i', 'f', 'e', 'b', 'r', 't', 'y', 'a', 'n', 'd', 'c', 'g', 'h', 'j', 'k', 'm', 'o', 'p', 'q', 's', 'u', 'v', 'w', 'x', 'z']
    >>> compute_slug('Zounds!')
    ['z', 'o', 'u', 'n', 'd', 's', 'a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 't', 'v', 'w', 'x', 'y']
    """

    slug = []
    lows = key.lower()
    for i in range(len(key)):
        if lows[i].isalpha() and lows[i] not in slug:
            slug.append(lows[i])
    for l in range(len(ALPHABET)):
        if ALPHABET[k] not in slug:
            slug.append(ALPHABET[l])

    return slug






def encrypt_char(source, slug, ch):
    """
    Given source and slug lists,
    if the char ch is in source, return
    its encrypted form. Otherwise return ch unchanged.
    >>> # Compute 'z' slug, store it in a var named z_slug
    >>> # and pass that in as the slug for the tests.
    >>> z_slug = compute_slug('z')
    >>> encrypt_char(ALPHABET, z_slug, 'A')
    'Z'
    >>> encrypt_char(ALPHABET, z_slug, 'n')
    'm'
    >>> encrypt_char(ALPHABET, z_slug, 'D')
    'C'
    >>> encrypt_char(ALPHABET, z_slug, '.')
    '.'
    >>> encrypt_char(ALPHABET, z_slug, ' ')
    ' '
    """
    if ch.isalpha():
        if ch.lower() in source:
            chl = source.index(ch.lower())
            if ch.isupper():
                return slug[chl].upper()
            else:
                return slug[chl]
    return ch






def encrypt_str(source, slug, s):
    """
    Given source and slug lists and string s,
    return a version of s where every char
    has been encrypted by source/slug.
    >>> z_slug = compute_slug('z')
    >>> encrypt_str(ALPHABET, z_slug, 'And like a thunderbolt he falls.')
    'Zmc khjd z sgtmcdqanks gd ezkkr.'
    """
    encrypt_str = ''
    for ch in s:
        encrypt_str = encrypt_str + encrypt_char(source, slug, ch)

    return encrypt_str


def decrypt_str(source, slug, s):
    """
    Given source and slug lists and encrypted string s,
    return the decrypted form of s.
    >>> z_slug = compute_slug('z')
    >>> decrypt_str(ALPHABET, z_slug, 'Zmc khjd z sgtmcdqanks gd ezkkr.')
    'And like a thunderbolt he falls.'
    """
    return encrypt_str(slug, source, s)


def encrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the encrypted form of its lines.
    """
    slug = compute_slug(key)
    with open(filename) as f:
        for line in f:
            line = line.strip()
            print(encrypt_str(ALPHABET, slug, line))


def decrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the decrypted form of its lines.
    """
    slug = compute_slug(key)
    with open(filename) as f:
        for line in f:
            line = line.strip()
            print(decrypt_str(ALPHABET, slug, line))


def main():
    args = sys.argv[1:]
    # 2 command line argument patterns:
    # -encrypt key filename
    # -decrypt key filename
    # Call encrypt_file() or decrypt_file() based on the args.
    if len(args) == 3 and args[0] == '-encrypt':
        encrypt_file(arg[2], arg[1])

    if len(args) == 3 and args[0] == '-decrypt':
        encrypt_file(arg[2], arg[1])


# Python boilerplate.
if __name__ == '__main__':
    main()
