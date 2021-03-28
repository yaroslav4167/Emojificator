import binascii
import base64


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


emojies = {
    '0': ':grinning:',
    '1': ':smiley:',
    '2': ':smile:',
    '3': ':grin:',
    '4': ':laughing:',
    '5': ':sweat_smile:',
    '6': ':joy:',
    '7': ':rofl:',
    '8': ':relaxed:',
    '9': ':blush:',
    'a': ':innocent:',
    'b': ':zany_face:',
    'c': ':thinking:',
    'd': ':face_with_monocle:',
    'e': ':sunglasses:',
    'f': ':face_with_hand_over_mouth:'
}


def emojificate(txt):
    enc_hex = encode_to_hex(txt)
    emojificated = ''
    for char in enc_hex:
        emojificated += emojies[char]
    return emojificated


def deemojificate(txt):
    txt = txt.replace(' ', '')
    for x, y in zip(emojies.keys(), emojies.values()):
        txt = txt.replace(y, x)
    decoded = decode_from_hex(txt)
    return decoded


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
