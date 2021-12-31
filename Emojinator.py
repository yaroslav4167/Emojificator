import binascii
import base64
from enc_pattern import emojies;


def encode_to_hex(txt):
    try:
        txt = base64.b64encode(txt.encode("UTF-8")).decode("UTF-8")
        output = ''.join("{:02x}".format(ord(c)) for c in txt)
    except:
        output = 'Ошибка кодирования.'
    return output


def decode_from_hex(txt):
    try:
        decode = ''.join([chr(int(''.join(c), 16))
                          for c in zip(txt[0::2], txt[1::2])])
        decoded = base64.b64decode(decode).decode()
    except:
        decoded = 'Ошибка декодирования.'
    return decoded


# emojies = {
#     '0': ':grinning:',
#     '1': ':smiley:',
#     '2': ':smile:',
#     '3': ':grin:',
#     '4': ':laughing:',
#     '5': ':sweat_smile:',
#     '6': ':joy:',
#     '7': ':rofl:',
#     '8': ':relaxed:',
#     #'9': ':blush:',
#     #'a': ':innocent:',
#     #'b': ':zany_face:',
#     #'c': ':thinking:',
#     #'d': ':face_with_monocle:',
#     #'e': ':sunglasses:',
#     #'f': ':face_with_hand_over_mouth:'
# }


def emojificate(txt):
    enc_hex = encode_to_hex(txt)
    enc_base = convert_base(enc_hex, len(emojies), 16)
    emojificated = ''
    for char in enc_base.lower():
        emojificated += emojies[char]
    return emojificated


def deemojificate(txt):
    txt = txt.replace(' ', '')
    for x, y in zip(emojies.keys(), emojies.values()):
        txt = txt.replace(y, x)
    hex = convert_base(txt, 16, len(emojies))
    decoded = decode_from_hex(hex)
    return decoded

def convert_base(num, to_base=10, from_base=10): # Thx, MaxU! https://ru.stackoverflow.com/questions/607802/%D0%9F%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4-%D0%B8%D0%B7-%D0%BB%D1%8E%D0%B1%D0%BE%D0%B9-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B-%D1%81%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2-%D0%BB%D1%8E%D0%B1%D1%83%D1%8E
    # first convert to decimal number
    n = int(num, from_base) if isinstance(num, str) else num
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n,m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]


menu = 'Выберите действие:\n' + \
    'e - Зашифровать текст\n' + \
    'd - Расшифровать текст\n' + \
    'exit - Выйти из программы'

exit = False
while not exit:
    print(menu)
    command = input('> ')
    if command == 'e':
        enc = emojificate(input('Enc text: '))
        print('=====\n' + enc + '\n=====')
    if command == 'd':
        dec = deemojificate(input('Dec text: '))
        print('=====\n' + dec + '\n=====')
    if command == 'exit':
        exit = True
