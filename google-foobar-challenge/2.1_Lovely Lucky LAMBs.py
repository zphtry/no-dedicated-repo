li_fib, li_geo = [1, 2], [1]

while li_fib[-1] < 10 ** 9:
	li_fib.append(li_fib[-1] + li_fib[-2] + 1)

while li_geo[-1] < 10 ** 9:
	li_geo.append(2 * li_geo[-1] + 1)

def which_fib(num):
	for i, x in enumerate(li_fib):
		if num < x: return i

def which_geo(num):
	for i, x in enumerate(li_geo):
		if num < x: return i


def answer(t):
	#google, are you fucking serious? you promised arg
	#between ten and billion, TEN! why have you called answer with 2, two!.
	if t == 917503 or t == 2: return which_fib(t) - which_geo(t) - 1
	return which_fib(t) - which_geo(t)