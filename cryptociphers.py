# -*- coding: utf-8 -*-
import re
import math


letters = 'abcdefghijklmnopqrstuvwxyz'
special_characters = '[\d.?\'\":\,\-!\ ’]'


def bin2num(binary_str, bit_width):
    accumulator = len(binary_str)-1
    out = 0
    if len(binary_str):
        for n in binary_str:
            if n == '1':
                out = out + math.pow(2, accumulator)
                accumulator = accumulator - 1
            elif n == '0':
                accumulator = accumulator - 1
            else:
                raise ValueError('input must consist of 1s and 0s')
        return int(out)
    else:
        raise ValueError('input must be string')


def i2bin(number, bit_width):
    bit_width = bit_width + 1
    remainder = int(number)
    out = ''
    accumulator_list = [i for i in range(1, bit_width)]
    list.reverse(accumulator_list)
    for n in accumulator_list:
        current_place = int(math.pow(2, n))
        lower_place = int(math.pow(2, n-1))
        if (current_place > remainder) and (lower_place <= remainder):
            remainder = int(remainder - lower_place)
            out = out + '1'
        else:
            out = out + '0'
    return out


# reverse = True for Atbash
# reverse = False for caesar
def shift_alphabet(offset, reverse, concat):
    shifted = []
    for i in range(0, len(letters)):
        op = ''
        if 0 > (i - offset):
            index = len(letters) + (i - offset)
            op = 'n'
        elif (len(letters) - 1) < (i - offset):
            index = (i - offset) - (len(letters) - 1)
            op = 'g'
        else:
            index = i - offset
            op = 'e'
        shifted.append(letters[index])
    if reverse:
        shifted.reverse()
    if concat:
        shifted = ''.join(shifted)
    return shifted


def decrypt_atbash(cryptogram):
    atbash_cipher = shift_alphabet(0,True,True)
    atbash_decrypted = []
    for l in cryptogram:
        if re.match(special_characters, l) is not None:
            atbash_decrypted.append(l)
        else:
            atbash_decrypted.append(letters[atbash_cipher.index(l.lower())])
    return ''.join(atbash_decrypted).upper()


def encrypt_atbash(message):
    atbash_cipher = shift_alphabet(0,True,True)
    atbash_encrypted = []
    for l in message:
        if re.match(special_characters, l) is not None:
            atbash_encrypted.append(l)
        else:
            atbash_encrypted.append(atbash_cipher[letters.index(l.lower())])
    return ''.join(atbash_encrypted).lower()


def decrypt_caesar(shift_index, cryptogram):
    possible_answers = []
    for i in range(0, len(letters)):
        new_letters = shift_alphabet(i, False, True)
        new_content = []
        for word in re.split(' ', cryptogram):
            for l in word:
                if re.match(special_characters, l) is not None:
                    new_content.append(l)
                else:
                    new_content.append(letters[new_letters.index(l.lower())-1])
            new_content.append(' ')
        possible_answers.append(''.join(new_content))
    if shift_index is None:
        return possible_answers
    else:
        return possible_answers[shift_index].strip()


def encrypt_caesar(shift_index, message):
    possible_answers = []
    for i in range(0, len(letters)):
        new_letters = shift_alphabet(i, False, True)
        new_content = []
        for word in re.split(' ', message):
            for l in word:
                if re.match(special_characters, l) is not None:
                    new_content.append(l)
                else:
                    new_content.append(letters[new_letters.index(l.lower())-1])
            new_content.append(' ')
        possible_answers.append(''.join(new_content))
    if shift_index == None:
        return possible_answers
    else:
        return possible_answers[shift_index].strip()


def encrypt_vigenere(cipher_word, message):
    vigenere_cipher = []
    for i in range(0,len(letters)):
        row = shift_alphabet(i, False, True)
        vigenere_cipher.append(row)
    vigenere_cipher.sort()

    parts = list(range(0,len(message)))
    for i in range(0,len(message)):
        if re.match(special_characters, message[i]):
            parts[i] = {
                'type': 'punct',
                'data': message[i],
                'index': i
            }
        else:
            parts[i] = {
                'type': 'letter',
                'data': message[i],
                'index': i,
                'encrypted': ''
            }

    cryptogram_message = list(filter(lambda l: l['type'] == 'letter', parts))

    vigenere_key = ''
    cipher_word = ''.join(list(filter(lambda i: i != ' ', [i for i in cipher_word])))
    if len(cipher_word) < len(cryptogram_message):
        while len(vigenere_key) < len(cryptogram_message):
            if (len(vigenere_key) + len(cipher_word)) <= len(cryptogram_message):
                vigenere_key = vigenere_key + cipher_word
            elif (len(vigenere_key) + len(cipher_word)) > len(cryptogram_message):
                subchunk = (len(cryptogram_message) - len(vigenere_key))
                sub = cipher_word[0:subchunk]
                vigenere_key = vigenere_key + sub
    elif len(cipher_word) > len(cryptogram_message):
        vigenere_key = cipher_word[0:len(cryptogram_message)]
    else:
        vigenere_key = cipher_word
    decrypted_message = []

    for i in range(0, len(cryptogram_message)):
        if cryptogram_message[i]['data'] == ' ':
            decrypted_message.append(' ')
        elif re.match(special_characters, cryptogram_message[i]['data']) is not None:
            decrypted_message.append(cryptogram_message[i]['data'])
        else:
            # vigenere_key[i]
            alphabet_index = letters.index(vigenere_key[i].lower())
            alphabet_select = vigenere_cipher[alphabet_index]
            cryptogram_message[i]['encrypted'] = alphabet_select[letters.index(cryptogram_message[i]['data'].lower())]

    crypto_letters = [data['data'] for data in parts]

    for i in range(0, len(cryptogram_message)):
        index = cryptogram_message[i]['index']
        crypto_letters[index] = cryptogram_message[i]['encrypted']

    return ''.join(crypto_letters).strip()


def decrypt_vigenere(cipher_word, cryptogram):
    vigenere_cipher = []
    for i in range(0,len(letters)):
        row = shift_alphabet(i, False, True)
        vigenere_cipher.append(row)
    vigenere_cipher.sort()

    parts = list(range(0,len(cryptogram)))
    for i in range(0,len(cryptogram)):
        if re.match(special_characters, cryptogram[i]):
            parts[i] = {
                'type': 'punct',
                'data': cryptogram[i],
                'index': i
            }
        else:
            parts[i] = {
                'type': 'letter',
                'data': cryptogram[i],
                'index': i,
                'decrypted': ''
            }

    cryptogram_message = list(filter(lambda l: l['type'] == 'letter', parts))

    vigenere_key = ''
    cipher_word = ''.join(list(filter(lambda i: i != ' ', [i for i in cipher_word])))
    if len(cipher_word) < len(cryptogram_message):
        while len(vigenere_key) < len(cryptogram_message):
            if (len(vigenere_key) + len(cipher_word)) <= len(cryptogram_message):
                vigenere_key = vigenere_key + cipher_word
            elif (len(vigenere_key) + len(cipher_word)) > len(cryptogram_message):
                subchunk = (len(cryptogram_message) - len(vigenere_key))
                sub = cipher_word[0:subchunk]
                vigenere_key = vigenere_key + sub
    elif len(cipher_word) > len(cryptogram_message):
        vigenere_key = cipher_word[0:len(cryptogram_message)]
    else:
        vigenere_key = cipher_word
    encrypted_message = []

    for i in range(0, len(cryptogram_message)):
        if cryptogram_message[i]['data'] == ' ':
            encrypted_message.append(' ')
        elif re.match(special_characters, cryptogram_message[i]['data']) is not None:
            encrypted_message.append(cryptogram_message[i]['data'])
        else:
            alphabet_index = letters.index(vigenere_key[i].lower())
            alphabet_select = vigenere_cipher[alphabet_index]
            cryptogram_message[i]['decrypted'] = letters[alphabet_select.index(cryptogram_message[i]['data'].lower())]

    crypto_letters = [data['data'] for data in parts]

    for i in range(0, len(cryptogram_message)):
        index = cryptogram_message[i]['index']
        crypto_letters[index] = cryptogram_message[i]['decrypted']

    return ''.join(crypto_letters).strip()


def decrypt_a1z26(content, reversed=False):
    decrypted_content = []
    if reversed:
        cipher = shift_alphabet(0,True,True)
    else:
        cipher = letters
    word_count = 0
    for word in re.split(' ', content):
        tmp_word = []
        num = ''
        for l in word:
            l = l.lower()
            if re.match('\d', l):
                num = num + l
            elif re.match('-', l):
                tmp_word.append(num)
                num = ''
            elif re.match(special_characters, l):
                tmp_word.append(num)
                num = ''
                tmp_word.append(l)
        if num != '':
            tmp_word.append(num)

        tmp_word = list(filter(lambda w: len(w) > 0, tmp_word))
        converted = []
        for word in tmp_word:
            try:
                num = int(word)
                let = cipher[num-1]
                converted.append(let)
            except:
                converted.append(word)

        decrypted_content.append(''.join(converted))
    return ' '.join(decrypted_content).strip()


def encrypt_a1z26(content, reversed=False):
    encrypted_content = []
    if reversed:
        cipher = shift_alphabet(0, True, True)
    else:
        cipher = letters
    for word in re.split(' ', content):
        word_temp = []
        for l in word:
            l = l.lower()
            if re.match(special_characters, l) is not None:
                word_temp.append(l)
            else:
                word_temp.append(str(letters.index(l)+1))
        encrypted_content.append('-'.join(word_temp))
    return ' '.join(encrypted_content).strip()


def bin_string(bstring):
    if len(bstring) % 8 == 0:
        chunk = 0
        nums = []
        while chunk < len(bstring):
            nums.append(chr(bin2num(bstring[chunk:chunk+8],8)))
            chunk = chunk + 8
        return ''.join(nums)


def string_bin(bstring):
    nums = []
    for l in bstring:
        nums.append(i2bin(ord(l), 8))
    return ''.join(nums)

def decrypt_combined(shift, cryptogram):
    return decrypt_caesar(shift,
             decrypt_atbash(
               decrypt_a1z26(cryptogram)))

__name__ = 'cryptociphers'
__all__ = ['shift_alphabet', 'decrypt_combined'
           'encrypt_atbash', 'decrypt_atbash',
           'decrypt_caesar', 'encrypt_caesar',
           'encrypt_vigenere', 'decrypt_vigenere',
           'decrypt_a1z26', 'encrypt_a1z26',
           'bin_string', 'string_bin']
