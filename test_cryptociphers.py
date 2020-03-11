# -*- coding: utf-8 -*-
from cryptociphers import decrypt_atbash, encrypt_atbash, \
                          decrypt_caesar, encrypt_caesar, \
                          encrypt_vigenere, decrypt_vigenere, \
                          decrypt_a1z26, encrypt_a1z26, \
                          bin_string, string_bin

def atbash_test():
    atbash_encrypt_test = 'paper jam dipper says: "auughwxqhgadsaduh!"'.upper()
    atbash_decrypt_test = 'KZKVI QZN WRKKVI HZBH: "ZFFTSDCJSTZWHZWFS!"'.upper()
    atbash_encrypt_result = encrypt_atbash(atbash_encrypt_test).upper()
    atbash_decrypt_result = decrypt_atbash(atbash_decrypt_test).upper()
    print('')
    print('Atbash Tests')
    print('Atbash Decrypt matches Encrypt (', atbash_decrypt_test == atbash_encrypt_result, ') ', atbash_decrypt_result)
    print('Atbash Encrypt matches Decrypt (', atbash_encrypt_test == atbash_decrypt_result, ') ', atbash_encrypt_result)

def caesar_test():
    caesar_encrypt_test = 'STAN IS NOT WHAT HE SEEMS'.upper()
    caesar_decrypt_test = 'VWDQ LV QRW ZKDW KH VHHPV'.upper()
    caesar_decrypt_result = encrypt_caesar(24, caesar_decrypt_test).upper()
    caesar_encrypt_result = decrypt_caesar(4, caesar_encrypt_test).upper()
    print('')
    print('Caesar Tests')
    print('Caesar Decrypt matches Encrypt (', caesar_decrypt_result == caesar_encrypt_test, ') ', caesar_decrypt_result, caesar_encrypt_test)
    print('Caesar Encrypt matches Decrypt (', caesar_encrypt_result == caesar_decrypt_test, ') ', caesar_encrypt_result, caesar_decrypt_test)

def vigenere_test():
    vigenere_encryption_key = 'GRAVITY'
    vigenere_encrypt_test = 'MABEL EATS SPRINKLES'
    vigenere_decrypt_test = 'SRBZT XYZJ SKZBLQCEN'
    vigenere_encrypt_result = encrypt_vigenere(vigenere_encryption_key, vigenere_encrypt_test).upper()
    vigenere_decrypt_result = decrypt_vigenere(vigenere_encryption_key, vigenere_decrypt_test).upper()
    print('')
    print('Vigerene Tests')
    print('Vigenere Decrypt matches Encrypt (', vigenere_decrypt_result == vigenere_encrypt_test, ') ', vigenere_decrypt_result)
    print('Vigenere Encrypt matches Decrypt (', vigenere_encrypt_result == vigenere_decrypt_test, ') ', vigenere_encrypt_result)


def a1z26_test():
    a1z26_decrypt_test = '18-5-22-5-18-19-5 20-8-5 3-9-16-8-5-18-19-!'
    a1z26_encrypt_test = 'reverse the ciphers!'.upper()
    a1z26_encrypt_result = encrypt_a1z26(a1z26_encrypt_test)
    a1z26_decrypt_result = decrypt_a1z26(a1z26_decrypt_test).upper()
    print('')
    print('A1Z26 Tests')
    print('A1Z26 Decrypt matches Encrypt (', a1z26_decrypt_result == a1z26_encrypt_test, ') ', a1z26_decrypt_result)
    print('A1Z26 Encrypt matches Decrypt (', a1z26_encrypt_result == a1z26_decrypt_test, ') ', a1z26_encrypt_result)


def binary_test():
    string2bin_test = 'Hello there!'
    bin2string_test = '010010000110010101101100011011000110111100100000011101000110100001100101011100100110010100100001'
    string2bin_result = string_bin(string2bin_test)
    bin2string_result = bin_string(bin2string_test)
    print('')
    print('Binary to String Tests')
    print('Binary to String Test (', string2bin_test == bin2string_result, ') ', bin2string_result)
    print('String to Binary Test (', bin2string_test == string2bin_result, ') ', string2bin_result)

[ test() for test in [atbash_test, caesar_test, vigenere_test, a1z26_test, binary_test]]