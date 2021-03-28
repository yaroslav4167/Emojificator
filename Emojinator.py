import binascii, base64

def encode_to_hex(txt):
	try:
		txt = base64.b64encode(txt.encode("UTF-8")).decode("UTF-8")
		output = ''.join("{:02x}".format(ord(c)) for c in txt)
	except:
		output = 'Ошибка кодирования.'
	return output

def decode_from_hex(txt):
	try:
		decode = ''.join([chr(int(''.join(c), 16)) for c in zip(txt[0::2],txt[1::2])])
		decoded = base64.b64decode(decode).decode()
	except:
		decoded = 'Ошибка декодирования.'
	return decoded


menu = 'Выберите действие:\n' + \
	'e - Зашифровать текст\n' + \
	'd - Расшифровать текст\n' + \
	'exit - Выйти из программы'
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
exit = False
while not exit:
	print(menu)
	command = input('> ')
	if command == 'e': 
		enc_hex = encode_to_hex(input('Enc text: '))
		emojufucate = ''
		for char in enc_hex:
			emojufucate += emojies[char]
		print('=====\n'+emojufucate+'\n=====')
	if command == 'd':
		dec_txt = input('Dec text: ').replace(' ', '')
		for x, y in zip(emojies.keys(), emojies.values()):
			dec_txt = dec_txt.replace(y, x)
		dec_txt = decode_from_hex(dec_txt)
		print('=====\n'+dec_txt+'\n=====')
	if command == 'exit':
		exit = True