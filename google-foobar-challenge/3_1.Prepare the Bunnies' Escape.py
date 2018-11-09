



# m = [[0, 0, 0, 0, 0, 0],
# 	 [1, 1, 1, 1, 1, 0],
# 	 [0, 0, 1, 0, 0, 0],
# 	 [0, 1, 1, 0, 1, 1],
# 	 [0, 1, 1, 0, 1, 1],
# 	 [0, 0, 0, 0, 0, 0]]

# m = [[0, 0, 1, 1, 1, 1],
# 	 [1, 0, 1, 1, 1, 1],
# 	 [1, 0, 1, 0, 0, 0],
# 	 [1, 0, 1, 0, 1, 0],
# 	 [1, 0, 0, 0, 1, 0],
# 	 [1, 1, 1, 1, 1, 0]]

#   -->
# |
# v

ma = [[0, 1, 1, 1],
	  [0, 0, 0, 1],
	  [1, 1, 0, 0],
	  [1, 1, 1, 0]]

# ma = [[0, 0, 0, 0, 0, 0],
# 	 [1, 1, 1, 1, 1, 0],
# 	 [0, 0, 0, 0, 0, 0],
# 	 [0, 1, 1, 1, 1, 1],
# 	 [0, 1, 1, 1, 1, 1],
# 	 [0, 0, 0, 0, 0, 0]]



def answer(m):
	h, w = len(m), len(m[0])

	li = [(0, 0)]

	can_destroy = True

	while li[-1] != (h - 1, w - 1) :

		i, j = li[-1]

		if i + 2 < h:
			if m[i + 2][j] == 0:
				li.append((i + 1, j))
				can_destroy = False
				continue

		if j + 2 < w:
			if m[i][j + 2] == 0:
				li.append((i, j + 1))
				can_destroy = False
				continue

		if i + 1 < h:
			if m[i + 1][j] == 0:
				li.append((i + 1, j))
				continue

		if j + 1 < w:
			if m[i][j + 1] == 0:
				li.append((i, j + 1))
				continue

	return len(li)

print(answer(ma))
