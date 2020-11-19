# GravityFallsCryptoTools - Python data tool for Gravity Falls Cryptograms
## [test_cryptociphers.py](test_cryptociphers.py)
Tests the ciphers and their encrypt / decrypt capabilities

## [gravity_falls_cryptograms_decryptor_(spoilers).py](gravity_falls_cryptograms_decryptor_(spoilers).py)
Cryptograms not included: Bill's Symbols, Author's Symbols, Combined Symbol Ciphers

Spoiler alert! If you have not solved the Gravity Falls cryptograms, and don't want any cryptospoilers, don't read this.

Spoiler alert! This file contains most of the Gravity Falls cryptograms, with their cipher and cipher information, executing the file reveals their secrets.

Cryptograms came from: https://gravityfalls.fandom.com/wiki/List_of_cryptograms#Number_codes

## [cryptociphers.py](cryptociphers.py)

```
Available tools:
	Alphabet:
		shift_alphabet   - Tool which slides alphabets by an offset, useful for caesar ciphers
	
	atbash:
		encrypt_atbash   - Encrypt plaintext using an atbash cipher
		decrypt_atbash   - Decrypt atbash cryptograms using an atbash cipher

	caesar:
		encrypt_caesar   - Encrypt plaintext using a caesar cipher, shift must be supplied, or all possibilities are returned
		decrypt_caesar   - Decrypt plaintext using a caesar cipher, shift must be supplied, or all possibilities are returned

	vigenere:
		encrypt_vigenere - Encrypt plaintex using a vigenere cipher, and supplied key
		decrypt_vigenere - Decrypt to plaintext using a vigenere cipher, and supplied key

	a1z26:
		encrypt_a1z26    - Encrypt plaintext using an a1z26 cipher
		decrypt_a1z26    - Decrypt to plaintext using an a1z26 cipher

	binary:
		bin_string       - Turn binary strings into text
		string_bin	 - Turn text strings into binary strings
```

# Example
![Puzzle in show](Welcome-Show-Clip.png "Puzzle in show")
![Puzzle solved with code](Welcome.png "Puzzle solved with code")




