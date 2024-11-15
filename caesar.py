def wordlist_create(name):
    wordlist = []
    file = open(name,"r")

    word = file.readline()

    while len(word) > 0:
        word = word.strip()
        wordlist.append(word)
        word = file.readline()
    return wordlist

def decipher_caesar_cipher(ciphertext):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    results = []

    for key in range(1, 26):
        plaintext = ''
        for char in ciphertext:
            if char.isalpha(): 
                is_upper = char.isupper()
                index = alphabet.index(char.lower())
                shifted_index = (index - key) % 26
                shifted_char = alphabet[shifted_index]
                plaintext += shifted_char.upper() if is_upper else shifted_char
            else:
                plaintext += char

        results.append((key, plaintext))

    return results



wordlist = wordlist_create("words_alpha.txt")
ciphertext = input("Enter the text you want to decipher: ") ## Enter UFTU ==> TEST on Key = 1
results = decipher_caesar_cipher(ciphertext)
print("Possible Results: ")
for key, text in results:
    print(f"Key {key}: {text}")


