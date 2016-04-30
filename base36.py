class Base36(object):

	@staticmethod
	def encode(number):
		if not isinstance(number, (int)):
			raise TypeError('ERROR: Number is not integer')
		if number < 0:
			raise ValueError('ERROR: Number is not positive')

		alphabet, base36 = ['0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', '']

		while number:
			number, i = divmod(number, 36)
			base36 = alphabet[i] + base36

		return base36 or alphabet[0]
	
	@staticmethod
	def decode(number):
		return int(number, 36)

