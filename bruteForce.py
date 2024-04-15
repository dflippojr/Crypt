from collections import Counter

def frequency_analysis(ciphertext):
    # create a list with english letters in order of their typical frequency
    english_freq = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c',
                    'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']
    # Count the frequency of each letter in the given ciphertext
    cipher_freq = Counter(ciphertext)
    # create a list of the letters in the ciphertext sorted by frequency
    sorted_cipher_freq = sorted(cipher_freq, key=cipher_freq.get, reverse=True)
    # Create a mapping from the sorted ciphertext letters to English letters using list comprehension
    key = {sorted_cipher_freq[i]: english_freq[i]
           for i in range(len(sorted_cipher_freq))}
    return key


def decipher(ciphertext, key):
    # create string to build the output into
    plaintext = ""
    # swap each letter in the ciphertext with the mapping given by the key
    for char in ciphertext:
        if char in key:
            plaintext += key[char]
        else:
            plaintext += char
    return plaintext


ciphertext = open("clean.txt", "r").read()
key = frequency_analysis(ciphertext)
plaintext = decipher(ciphertext, key)
print(str(key) + "\n" + plaintext)
