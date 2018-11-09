y = [14, 27, 1, 4, 2, 50, 3, 1]
x = [2, 4, -4, 3, 1, 1, 14, 27, 50]
def answer(a, b):
	if len(a) > len(b): return [item for item in a if item not in b][0]
	else: return [item for item in b if item not in a][0]

print(answer(x, y))