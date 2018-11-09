def int2base(x, base):
	digits = []
	while x:
		digits.append(x % base)
		x //= base
	return ''.join(reversed(list(map(str, digits))))

def answer(n, b):
	k = len(n)
	nums = [n]
	while True:
		asc, desc = sorted(n), sorted(n, reverse = True)
		# print(''.join(desc), ''.join(asc), ''.join(n))
		n = int2base(int(''.join(desc), b) - int(''.join(asc), b), b).rjust(k, '0')
		if n in nums: return len(nums) - nums.index(n)
		nums.append(n)

# print(answer('210022', 3))

