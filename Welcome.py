from cryptociphers import decrypt_caesar, decrypt_vigenere, decrypt_combined
from cryptograms import get_puzzle_by_name, just_give_me_the_books

print('Testing various settings of the cryptogram module\n\r')

puzzle = get_puzzle_by_name('Theme Song', 1)

print('First cryptogram (just the title):')
print(str(puzzle) + '\n\r')

#----------------------------------------------

puzzle = get_puzzle_by_name('Tourist Trapped', 3)
decrypted_puzzle = decrypt_caesar(24, puzzle['cryptogram']).upper()

print('Second cryptogram: (title, cryptogram, and cipher type)')
print(str(puzzle) + '\n\r')
print('Cryptogram puzzle: ' + puzzle['cryptogram'])
print('Decrypted ciphertext: ' + decrypted_puzzle + '\n\r')

#----------------------------------------------

puzzle = get_puzzle_by_name('The Love God', 9001)
decrypted_puzzle = decrypt_vigenere(puzzle['key'], puzzle['cryptogram'])

print('Third cryptogram [vigenere]: (full spoiler)')
print(str(puzzle) + '\n\r')
print('Cryptogram puzzle: ' + puzzle['cryptogram'])
print('Decrypted ciphertext: ' + decrypted_puzzle.upper() + '\n\r')

#----------------------------------------------

puzzle = get_puzzle_by_name('Weirdmageddon 4: Somewhere in the Woods (4)', 2)
decrypted_puzzle = decrypt_combined(24, puzzle['cryptogram']).upper() + '\n'
excerpt_len = int(len(decrypted_puzzle)/2)
excerpt = decrypted_puzzle[0:excerpt_len-2]

print('A part of Weirdmageddon')
print('\tDecrypted combined cipher: ' + excerpt)

#----------------------------------------------

print('\n\r...And Then...\n\r')
print('Dark magic! Just give me the books!' + '\n\r')

all_the_stuff = just_give_me_the_books()

print('The first one~')
print(str(all_the_stuff[0]) + '\n\r')
print('The second one~~')
print(str(all_the_stuff[1]) + '\n\r')
print('That is all that is there~~' + '\n\r')