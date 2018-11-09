# (1, 1)

# (2, 1)

# (3, 1)							| (2, 3)
# 								|
# (4, 1)		   | (3, 4)			| (5, 3)		 | (2, 5)
# 			   |				|				 |
# (5, 1)  (4, 5) | (7, 4)  (3, 7) | (8, 3)  (5, 8) | (7, 5)  (2, 7)


def answer_new(M, N):
	M, N = int(M), int(N)
	if M < 1e50 and N < 1e50:
		res = 0
		while M > 0 and N > 0:
			if M > N:
				res += M // N
				M %= N
			else:
				res += N // M
				N %= M
			if M == 1 or N == 1: return str(res - 1)
	return 'impossible'

def answer_old(M, F):
	M, F = int(M), int(F)
	if M < 1e50 and F < 1e50:
		n = 0
		while M > 0 and F > 0:
			d = abs(M - F)
			if M > F: M = d
			else: F = d
			if M == 1 or F == 1: return str(n + max(M, F))
			n += 1
			# print(M, F, '   ', n)
	return 'impossible'


# print(answer_new('123454343423534', '123454343423534'))

print(answer_old('23333353647', '519898923465'))







