# caesar-decrypt

decrypting a Caesar Cipher ciphertext, with no information about the key

Currently its looping through all letters inside the ciphertext, processing the current character, shifting it back by i'th value , and adding it to the result array where contains the all possible shifts and its corresponding plaintext.

I will modify this by using words_alpha.txt file to check if the results in the results array contains valid words from this file, and only print out the ones with valid english words to filter and reduce the possibilities.
