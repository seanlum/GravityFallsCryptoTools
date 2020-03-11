# -*- coding: utf-8 -*-
# made to solve these cryptograms
# https://gravityfalls.fandom.com/wiki/List_of_cryptograms#Number_codes
from cryptociphers import decrypt_atbash, decrypt_caesar, decrypt_vigenere, decrypt_a1z26, bin_string


def combined(shift, cryptogram):
    return decrypt_caesar(shift, decrypt_atbash(decrypt_a1z26(cryptogram)))

cryptograms = [
    {
        'entry': 'Theme Song',
        'cryptogram':  'VWDQ LV QRW ZKDW KH VHHPV',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Tourist Trapped',
        'cryptogram': 'ZHOFRPH WR JUDYLWB IDOOV',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'The Legend of the Gobblewonker',
        'cryptogram': 'QHAW ZHHN: UHWXUQ WR EXWW LVODQG.',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Headhunters',
        'cryptogram': 'KH\'V VWLOO LQ WKH YHQWV. ',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'The Hand That Rocks The Mabel',
        'cryptogram': 'FDUOD, ZKB ZRQ\'W BRX FDOO PH? ',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'The Inconveniencing',
        'cryptogram': 'RQZDUGV DRVKLPD! ',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Dipper vs. Maliness',
        'cryptogram': 'PU. FDHVDULDQ ZLOO EH RXW QHAW ZHHN. PU. DWEDVK ZLOO VXEVWLWXWH. ',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Double Dipper',
        'cryptogram': 'KZKVI QZN WRKKVI HZBH: "ZFFTSDCJSTZWHZWFS!" ',
        'type': 'atbash'
    },
    {
        'entry': 'Irrational Treasure',
        'cryptogram': 'V. KOFIRYFH GIVNYOVB.',
        'type': 'atbash'
    },
    {
        'entry': 'The Time Traveler\'s Pig',
        'cryptogram': 'MLG S.T. DVOOH ZKKILEVW. ',
        'type': 'atbash'
    },
    {
        'entry': 'Fight Fighters',
        'cryptogram': 'HLIIB, WRKKVI, YFG BLFI DVMWB RH RM ZMLGSVI XZHGOV. ',
        'type': 'atbash'
    },
    {
        'entry': 'Little Dipper',
        'cryptogram': 'GSV RMERHRYOV DRAZIW RH DZGXSRMT. ',
        'type': 'atbash'
    },
    {
        'entry': 'Summerween',
        'cryptogram': 'YILFTSG GL BLF YB SLNVDLIP: GSV XZMWB.',
        'type': 'atbash'
    },
    {
        'entry': 'Boss Mabel',
        'cryptogram': 'SVZEB RH GSV SVZW GSZG DVZIH GSV UVA. ',
        'type': 'atbash'
    },
    {
        'entry': 'Bottomless Pit!',
        'cryptogram': '14-5-24-20 21-16: "6-15-15-20-2-15-20 20-23-15: 7-18-21-14-11-12-5\'19 7-18-5-22-5-14-7-5." ',
        'type': 'a1z26'
    },
    {
        'entry': 'The Deep End',
        'cryptogram': '22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14-1. ',
        'type': 'a1z26'
    },
    {
        'entry': 'Carpet Diem',
        'cryptogram': 'SXEHUWB LV WKH JUHDWHVW PBVWHUB RI DOO DOVR: JR RXWVLGH DQG PDNH IULHQGV.',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Carpet Diem (2)',
        'cryptogram': '2-21-20 23-8-15 19-20-15-12-5 20-8-5 3-1-16-5-18-19? ',
        'type': 'a1z26'
    },
    {
        'entry': 'Boyz Crazy',
        'cryptogram': '8-1-16-16-25 14-15-23, 1-18-9-5-12? ',
        'type': 'a1z26'
    },
    {
        'entry': 'Land Before Swine',
        'cryptogram': 'OLHV',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Land Before Swine (2)',
        'cryptogram': '9-20 23-15-18-11-19 6-15-18 16-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-7-19!',
        'type': 'a1z26'
    },
    {
        'entry': 'Dreamscaperers',
        'cryptogram': 'PBVWHUB VKDFN',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Dreamscaperers (2)',
        'cryptogram': 'SLWW',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Dreamscaperers (3)',
        'cryptogram': 'EWTUG AQW OCTKNAP',
        'type': 'caesar',
        'shift': 25
    },
    {
        'entry': 'Dreamscaperers (4)',
        'cryptogram': '20-15 2-5 3-15-14-20-9-14-21-5-4... ',
        'type': 'a1z26'
    },
    {
        'entry': 'Gideon Rises',
        'cryptogram': 'ELOO LV ZDWFKLQJ ',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Gideon Rises (2)',
        'cryptogram': '18-5-22-5-18-19-5 20-8-5 3-9-16-8-5-18-19 ',
        'type': 'a1z26'
    },
    {
        'entry': 'Gideon Rises (5)',
        'cryptogram': '5-19-23-6-21-16 18-9-6 4-16-19 22-12-15-10-20-19-25-19 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Candy Monster (2)',
        'cryptogram': 'IURP WKH ILUVW XQWLO WKH ODVW VHDUFK WKH ',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Lefty (2)',
        'cryptogram': 'WKHP DOO ZHOFRPH WR JUDYLWB IDOOV ',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Tooth (2)',
        'cryptogram': 'FRGHV RI FUHGLWV SDVW RQH PHDQV RQH VR VHDUFK ',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Scary-oke (1)',
        'cryptogram': '5-19-23-6-21-16 18-9-6 4-16-19...',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Scary-oke (2)',
        'cryptogram': '6-12-1-7',
        'type': 'a1z26'
    },
    {
        'entry': 'Scary-oke (3)',
        'cryptogram': 'TEV FP TBKAV PL MBOCBZQ',
        'type': 'caesar',
        'shift': 4
    },
    {
        'entry': 'Scary-oke (4)',
        'cryptogram': 'ZDWFK RXW',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Scary-oke (5)',
        'cryptogram': 'NLOO PH SOHDVH',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Scary-oke (6)',
        'cryptogram': '4-16-19 11-23-10 20-9-1-10-5-4-23-15-6-5 15-5 2-19-6-25 21-12-19-2-19-6',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Scary-oke (7)',
        'cryptogram': '21-23-10 16-19 16-15-20-19 16-15-5 8-12-23-10-5 18-9-6-19-2-19-6?',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Into the Bunker',
        'cryptogram': '01010000011101010111010000100000011000010110110001101100001000000111001101101001011110000010000001110000011010010110010101100011011001010111001100100000011101000110111101100111011001010111010001101000011001010111001000100001',
        'type': 'binstring'
    },
    {
        'entry': 'Into the Bunker (4)',
        'cryptogram': 'OOIY DMEV VN IBWRKAMW BRUWLL ',
        'type': 'vigenere',
        'key': 'SHIFTER'
    },
    {
        'entry': 'Into the Bunker (5)',
        'cryptogram': '15-11-8-6-9-8-19-6 3-5-19 9-18 11-23-21-16-15-10-19-6-25 21-9-3-12-20',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Into the Bunker (6)',
        'cryptogram': '12-19-23-20 4-9 3-4-4-19-6 21-23-4-23-5-4-6-9-8-16-19 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'The Golf War',
        'cryptogram': 'NLMXQWWN IIZ LZFNF',
        'type': 'vigenere',
        'key': 'WHATEVS'
    },
    {
        'entry': 'The Golf War (2)',
        'cryptogram': '9-12-20 11-23-10 5-12-19-19-8-15-10-17 9-10 4-16-19 17-6-19-19-10 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'The Golf War (3)',
        'cryptogram': '21-23-10\'4 16-19-12-8 22-3-4 1-9-10-20-19-6 1-16-23-4 16-19\'5 5-19-19-10',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Sock Opera',
        'cryptogram': 'KFIV VMVITB, MLG HPRM ZMW YLMV',
        'type': 'atbash'
    },
    {
        'entry': 'Sock Opera (2)',
        'cryptogram': 'IRHRMT ORPV GSV HSVKZIW GLMV',
        'type': 'atbash'
    },
    {
        'entry': 'Sock Opera (3)',
        'cryptogram': 'ZLGGOH',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Sock Opera (4)',
        'cryptogram': 'VKLIWHU',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Sock Opera (5)',
        'cryptogram': 'ZKDWHYV',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Sock Opera (6)',
        'cryptogram': 'EHDUR',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Sock Opera (7)',
        'cryptogram': 'YM\'KL ECN PPK WFOM UBR KQVXNLK, DCI SIK\'U VDA JFTOTA AYQ BWL VVCT "EBTGGB BHWKGZH" HVV: TMEASZFA LOS YCDT PRWKTIYEKGL DBV XQDTYRDGVI ',
        'type': 'vigenere',
        'key': 'CIPHER'
    },
    {
        'entry': 'Sock Opera (8)',
        'cryptogram': '10-9 8-3-8-8-19-4 5-4-6-15-10-17-5 21-23-10 16-9-12-20 11-19 20-9-1-10',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Sock Opera (9)',
        'cryptogram': '5-9 8-23-4-15-19-10-4-12-25 15 1-23-4-21-16 4-16-15-5 4-9-1-10',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Sock Opera (10)',
        'cryptogram': '23-22-10-9-6-11-23-12 5-9-9-10 1-15-12-12 22-19 4-16-19 10-9-6-11',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Sock Opera (11)',
        'cryptogram': '19-10-14-9-25 4-16-19 21-23-12-11 22-19-18-9-6-19 4-16-19 5-4-9-6-11 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Soos and the Real Girl',
        'cryptogram': 'VWDQ LV QRW ZKDW KH VHHPV',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Soos and the Real Girl (2)',
        'cryptogram': '0101001101010000010000010100001101000101010010100100000101001101010101000101011101001111',
        'type': 'binstring'
    },
    {
        'entry': 'Soos and the Real Girl (3)',
        'cryptogram': 'BRTYMEMNX QBR HRRQPEE',
        'type': 'vigenere',
        'key': 'BEARO'
    },
    {
        'entry': 'Soos and the Real Girl (4)',
        'cryptogram': '1-15-10-10-15-10-17 16-19-23-6-4-5 22-25 20-23-25-12-15-17-16-4',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Soos and the Real Girl (5)',
        'cryptogram': '8-9-5-5-19-5-5-15-10-17 6-9-22-9-4-5 22-25 11-9-9-10-12-15-17-16-4',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Soos and the Real Girl (6)',
        'cryptogram': '16-19-6 19-11-9-4-15-9-10-23-12 22-23-17-17-23-17-19 15-5 23 6-19-23-12 18-6-15-17-16-4',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Soos and the Real Girl (7)',
        'cryptogram': '5-16-19 16-23-5 4-16-19 9-10-19 10-23-11-19 17-15-18-18-23-10-25',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Little Gift Shop of Horrors',
        'cryptogram': 'PVREK BIG QF. JCDQZRF\' ZNVEFH OBCX: "C BEWRS VVUTBFL BT BKNX CVAY BKNX CVAY BKNX"',
        'type': 'vigenere',
        'key': 'NONCANON'
    },
    {
        'entry': 'Little Gift Shop of Horrors (2)',
        'cryptogram': '23-12-12 23-10-15-11-23-4-15-9-10',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Little Gift Shop of Horrors (3)',
        'cryptogram': '15-5 22-12-23-21-13 11-23-17-15-21',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Society of the Blind Eye',
        'cryptogram': 'YROO XRKSVI! GIRZMTOV!',
        'type': 'atbash'
    },
    {
        'entry': 'Society of the Blind Eye (2)',
        'cryptogram': 'MXNGVEECW MW SLAWW. SUL FPZSK MW SOJMRX.',
        'type': 'vigenere',
        'key': 'ERASE'
    },
    {
        'entry': 'Society of the Blind Eye (3)',
        'cryptogram': '17-15-20-19-9-10\'5 4-23-10-4-6-3-11-5, 11-15-5-5-8-19-12-12-19-20 4-23-4-4-9-9-5,',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Society of the Blind Eye (4)',
        'cryptogram': '5-16-23-10-20-6-23\'5 6-19-14-19-21-4-15-9-10-5, 5-9-21-15-19-4-25\'5 2-15-19-1-5,',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Society of the Blind Eye (5)',
        'cryptogram': '23 18-19-23-6 9-18 1-15-4-21-16-19-5, 23 12-15-18-19 9-18 6-19-17-6-19-4,',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Society of the Blind Eye (6)',
        'cryptogram': '4-16-19-5-19 23-6-19 4-16-19 4-16-15-10-17-5 4-16-23-4 4-16-19-25 4-6-25 4-9 18-9-6-17-19-4',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Blendin\'s Game',
        'cryptogram': 'FOC\'T FW MVV VIBE EZBAV KF NOW KTB\'K FO IHG BBAV VIBE.',
        'type': 'vigenere',
        'key': 'CAPACITOR'
    },
    {
        'entry': 'Blendin\'s Game (2)',
        'cryptogram': '14-9-15-10 4-16-19 4-15-11-19 8-23-6-23-20-9-26 23-2-9-15-20-23-10-21-19 19-10-18-9-6-21-19-11-19-10-4 5-7-3-23-20-6-9-10! ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Blendin\'s Game (3)',
        'cryptogram': '17-6-19-23-4 16-9-3-6-5! ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Blendin\'s Game (4)',
        'cryptogram': '5-9-12-15-20 22-19-10-19-18-15-4-5! ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Blendin\'s Game (5)',
        'cryptogram': '5-15-17-10 3-8 25-19-5-4-19-6-20-23-25!',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'The Love God',
        'cryptogram': 'O SAM KVGS',
        'type': 'vigenere',
        'key': 'GOATANDAPIG'
    },
    {
        'entry': 'The Love God (2)',
        'cryptogram': '23-4 4-16-19 8-12-23-25 9-6 23-4 4-16-19 18-23-15-6,',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'The Love God (3)',
        'cryptogram': '15 23-12-1-23-25-5 5-19-19 4-16-19-11 5-4-23-10-20-15-10-17 4-16-19-6-19 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'The Love God (4)',
        'cryptogram': '20-6-19-5-5-19-20 15-10 22-12-23-21-13 4-16-19-25\'6-19 9-10 11-25 12-23-1-10, ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'The Love God (5)',
        'cryptogram': '22-3-4 1-16-19-10 15 4-3-6-10 11-25 16-19-23-20 4-16-19-25\'6-19 17-9-10-19',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Northwest Mansion Mystery',
        'cryptogram': 'PYOL YS QH LLFDJW: UAH DNCVFW ZTCKW XKG WFFWWKNLLMRP? WISAGCXJ AR WKUISW! DPX WDSUKXR: LLH UBFO. ',
        'type': 'vigenere',
        'key': 'CURSED'
    },
    {
        'entry': 'Northwest Mansion Mystery (2-4)',
        'cryptogram': '5-4-23-10-15-5-10-9-4-1-16-23-4-16-19-5-19-19-11-5',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Not What He Seems (2)',
        'cryptogram': 'JXYDPHQW',
        'type': 'caesar',
        'shift': 24
    },
    {
        'entry': 'Not What He Seems (3)',
        'cryptogram': 'LAR ZPUHTFTY XWEUPJR GHGZT',
        'type': 'vigenere',
        'key': 'STNLYMBL'
    },
    {
        'entry': 'Not What He Seems (4)',
        'cryptogram': '4-16-15-6-4-25 25-19-23-6-5 23-10-20 10-9-1 16-19\'5 22-23-21-13 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Not What He Seems (5)',
        'cryptogram': '4-16-19 11-25-5-4-19-6-25 15-10 4-16-19 11-25-5-4-19-6-25 5-16-23-21-13 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'A Tale of Two Stans',
        'cryptogram': 'TIZOLHAJSIW CKMMWZPMKQ: GLY KJQBH ',
        'type': 'vigenere',
        'key': 'SIXER'
    },
    {
        'entry': 'A Tale of Two Stans (2)',
        'cryptogram': '23 5-4-3-22-22-9-6-10 4-9-3-17-16 10-19-1 14-19-6-5-19-25 10-23-4-15-2-19 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'A Tale of Two Stans (3)',
        'cryptogram': '18-15-12-22-6-15-21-13 1-23-5-10\'4 4-9-9 21-6-19-23-4-15-2-19 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'A Tale of Two Stans (4)',
        'cryptogram': '16-23-2-15-10-17 4-1-15-10-5 1-23-5 10-9-4 16-15-5 8-12-23-10 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'A Tale of Two Stans (5)',
        'cryptogram': '5-9 16-19 14-3-5-4 5-16-6-3-17-17-19-20 23-10-20 10-23-11-19-20 22-9-4-16 5-4-23-10 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'A Tale of Two Stans (6)',
        'cryptogram': 'YROO XRKSVI GIRZMTOV',
        'type': 'atbash'
    },
    {
        'entry': 'Dungeons, Dungeons, and More Dungeons',
        'cryptogram': 'VXFQLKB-AYRTHHEJ!',
        'type': 'vigenere',
        'key': 'RADMASTER'
    },
    {
        'entry': 'Dungeons, Dungeons, and More Dungeons (2)',
        'cryptogram': '18-3-10 23-10-20 17-23-11-19-5 23-6-19 17-6-19-23-4 20-15-5-4-6-23-21-4-15-9-10-5 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Dungeons, Dungeons, and More Dungeons (3)',
        'cryptogram': '22-3-4 5-11-23-12-12 4-16-15-10-17-5 21-23-10 16-23-2-19 21-16-23-15-10 6-19-23-21-4-15-9-10-5 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'The Stanchurian Candidate',
        'cryptogram': 'CWZSQVQBEWZSQVQBEWZSQVQMPHKD \'MZ! ',
        'type': 'vigenere',
        'key': 'WORKINIT'
    },
    {
        'entry': 'The Stanchurian Candidate (2)',
        'cryptogram': '22-19 1-23-6-25 9-18 1-16-9-11 25-9-3 22-19-12-15-4-4-12-19 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'The Stanchurian Candidate (3)',
        'cryptogram': '22-15-17 8-6-9-22-12-19-11-5 21-23-10 5-4-23-6-4 9-3-4 1-15-20-20-12-19 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'The Last Mabelcorn (4)',
        'cryptogram': 'S UPYTYH DIP GAVO QETHI MCBK OHK XEXJB VRW YOUWCHIA VRSV OQ LRDIA',
        'type': 'vigenere',
        'key': 'SCHMENDRICK'
    },
    {
        'entry': 'The Last Mabelcorn (5)',
        'cryptogram': '15-10 21-15-8-16-19-6\'5 17-23-11-19 16-19 10-19-19-20-5 23 8-23-1-10 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'The Last Mabelcorn (6)',
        'cryptogram': '22-19 5-3-6-19 4-9 13-10-9-1 1-16-15-21-16 5-15-20-19 25-9-3\'6-19 9-10 ',
        'type': 'combined',
        'shift': 24
    },
# print(decrypt_vigenere('DOPPER','))
    {
        'entry': 'Roadside Attraction',
        'cryptogram': 'VCDH, PZNS P CSSOS VDPUHB GTXILSKTV, VYSCIYROZN USLQR WXW NDM WDQVZOGS, EEG PTUVZHBSTH R WOAZMEJ PJAPURU PCH JDGHN GRW OADRX WVT LEP',
        'type': 'vigenere',
        'key': 'DOPPER'
    },
    {
        'entry': 'Roadside Attraction (2)',
        'cryptogram': '21-23-6-12-23 11-21-21-9-6-13-12-19 6-19-4-3-6-10-19-20 23-12-12 16-15-5 18-12-9-1-19-6-5',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Roadside Attraction (3)',
        'cryptogram': '11-23-6-15-12-25-10 20-15-2-9-6-21-19-20 16-15-11 23-18-4-19-6 9-10-12-25 5-15-26 16-9-3-6-5 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Roadside Attraction (4)',
        'cryptogram': '22-19-23-4-6-15-21-19 5-12-23-8-8-19-20 16-15-11 18-9-6 22-19-15-10-17 23 21-23-20 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Roadside Attraction (5)',
        'cryptogram': '9-12-20 17-9-12-20-15-19\'5 4-16-19 22-19-5-4 17-15-6-12-18-6-15-19-10-20 5-4-23-10 19-2-19-6 16-23-20',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Dipper and Mabel vs. the Future (5)',
        'cryptogram': 'ETX CPI ASTD GI?',
        'type': 'vigenere',
        'key': 'BLUEBOOK'
    },
    {
        'entry': 'Dipper and Mabel vs. the Future (6)',
        'cryptogram': '4-16-19 8-6-9-8-16-19-21-25 5-19-19-11-19-20 18-23-6 23-1-23-25 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Dipper and Mabel vs. the Future (7)',
        'cryptogram': '22-3-4 18-15-10-23-12-12-25 1-19]\'2-19 6-19-23-21-16-19-20 4-16-19 20-23-25. ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Dipper and Mabel vs. the Future (8)',
        'cryptogram': '17-15-2-19 3-8 4-16-19 8-23-5-4. 19-11-22-6-23-21-19 4-16-19 5-4-6-23-10-17-19. ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Dipper and Mabel vs. the Future (9)',
        'cryptogram': '19-2-19-6-25-4-16-15-10-17 25-9-3 21-23-6-19 23-22-9-3-4 1-15-12-12 21-16-23-10-17-19. ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Weirdmageddon Part 1',
        'cryptogram': 'KB HTMT IHOV 1,000 AMLCT NDY XZOM MLCG\'H TSCGKFWFA IV VVEWYDUQIBXV, CVO HIMC OI\'J DINV, IM\'H NSZPO EZ CM KLVP EZLYLG ',
        'type': 'vigenere',
        'key': 'CILLBIPHER'
    },
    {
        'entry': 'Weirdmageddon Part 1 (2)',
        'cryptogram': '17-23-11-19 15-5 9-2-19-6, 23-10-20 15 1-9-10 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Weirdmageddon Part 1 (3)',
        'cryptogram': '10-9-1 15-4\'5 4-15-11-19 4-9 5-4-23-6-4 4-16-19 18-3-10',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Weirdmageddon Part 1 (4)',
        'cryptogram': '15 23-12-1-23-25-5 12-9-2-19 21-9-6-6-3-8-4-15-10-17 12-15-2-19-5',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Weirdmageddon Part 1 (5)',
        'cryptogram': '10-9-1 12-19-4\'5 5-19-19 1-16-15-21-16 8-15-10-19-5 5-3-6-2-15-2-19-5 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Weirdmageddon 2: Escape From Reality',
        'cryptogram': 'FZPO YSU BQSHZ LTLY FR LV UCC IFJ CIYHO LTEYWKQWUW II P KFASJ JKQASPJE\'W LLOMKXQNFR FLWEDGI ',
        'type': 'vigenere',
        'key': 'DIPPYFRESH'
    },
    {
        'entry': 'Weirdmageddon 2: Escape From Reality (2)',
        'cryptogram': '1-16-19-10 9-10-19 17-19-4-5 4-6-23-8-8-19-20 15-10-5-15-20-19 4-16-19 8-23-5-4 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Weirdmageddon 2: Escape From Reality (3)',
        'cryptogram': '20-6-19-23-11-5 21-23-10 4-3-6-10 4-9 10-15-17-16-4-11-23-6-19-5 18-23-5-4 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Weirdmageddon 3: Take Back The Falls',
        'cryptogram': 'KVOU VTKSE XVREOW DQTMJKGD MF KNLJH CVE 900 YCHJZ OH XXFB PJPSKC FVQUSIOV LHP: FRNLLCDBFBF ',
        'type': 'vigenere',
        'key': 'SHACKTRON'
    },
    {
        'entry': 'Weirdmageddon 3: Take Back The Falls (2)',
        'cryptogram': '4-19-10 5-25-11-22-9- 5 8-12-23-21-19-20 23-6-9-3-10-20 23 1-16-19-19-12',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Weirdmageddon 3: Take Back The Falls (3)',
        'cryptogram': '16-23-10-20 15-10 16-23-10-20 4-16-19-25\'12-12 22-9-10-20 4-16-19 5-19-23-12 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Weirdmageddon 3: Take Back The Falls (4)',
        'cryptogram': '22-3-4 22-6-19-23-13 4-16-19 21-16-23-15-10, 23-10-20 8-23-25 4-16-19 21-9-5-4 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Weirdmageddon 3: Take Back The Falls (5)',
        'cryptogram': '4-16-19 8-6-9-8-16-19-21-25 1-15-12-12 23-12-12 22-19 12-9-5-4 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Weirdmageddon 4: Somewhere in the Woods',
        'cryptogram': 'ZMFUIGV PSHP IGK AGTAYAG TRMNE VVGSQW KLE JOJXU GIMWZ',
        'type': 'vigenere',
        'key': 'HIDDEN DEEP WITHIN THE WOODS A BURIED TREASURE WAITS'
    },
    {
        'entry': 'Weirdmageddon 4: Somewhere in the Woods (2)',
        'cryptogram': 'GLCOPRP GOOGWMJ FXZWG',
        'type': 'vigenere',
        'key': 'AXOLOTL'
    },
    {
        'entry': 'Weirdmageddon 4: Somewhere in the Woods (3)',
        'cryptogram': '18-23-20-19-20 8-15-21-4-3-6-19-5 22-12-19-23-21-16-19-20 22-25 5-3-10 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Weirdmageddon 4: Somewhere in the Woods (4)',
        'cryptogram': '4-16-19 4-23-12-19\'5 4-9-12-20, 4-16-19 5-3-11-11-19-6\'5 20-9-10-19 ',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Weirdmageddon 4: Somewhere in the Woods (5)',
        'cryptogram': '15-10 11-19-11-9-6-15-19-5 4-16-19 8-15-10-19-5 5-4-15-12-12 8-12-23-25',
        'type': 'combined',
        'shift': 24
    },
    {
        'entry': 'Weirdmageddon 4: Somewhere in the Woods (6)',
        'cryptogram': '9-10 23 5-3-10-10-25 5-3-11-11-19-6\'5 20-23-25 ',
        'type': 'combined',
        'shift': 24
    }
]

for entry in cryptograms:
    if len(entry['cryptogram']) > 0:
        if entry['type'] == 'caesar':
            print(entry['entry'] + ':\n\t' + decrypt_caesar(entry['shift'], entry['cryptogram']).upper() + '\n')
        elif entry['type'] == 'atbash':
            print(entry['entry'] + ':\n\t' + decrypt_atbash(entry['cryptogram']).upper() + '\n')
        elif entry['type'] == 'a1z26':
            print(entry['entry'] + ':\n\t' + decrypt_a1z26(entry['cryptogram']).upper() + '\n')
        elif entry['type'] == 'combined':
            print(entry['entry'] + ':\n\t' + combined(entry['shift'], entry['cryptogram']).upper() + '\n')
        elif entry['type'] == 'binstring':
            print(entry['entry'] + ':\n\t' + bin_string(entry['cryptogram']).upper() + '\n')
        elif entry['type'] == 'vigenere':
            print(entry['entry'] + ':\n\t' + decrypt_vigenere(entry['key'], entry['cryptogram']).upper() + '\n')
