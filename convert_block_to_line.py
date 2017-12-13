# To express the color scan in another order:
# -input: string using the notation where the unfolded cube is read block by block (U + R + F + D + L + B)
# -output: string using the notation where the unfolded cube is read line by line 

def convert_block_to_line(s):
	up = s[0:9]
	right = s[9:18]
	forward = s[18:27]
	down = s[27:36]
	left = s[36:45]
	back = s[45:54]
	state = [0] * 54
	state[0:9] = up
	for i in range(0,3):
		for j in range(0,3):
			state[9 + i * 12 + j] = left[j + 3 * i]
			state[9 + i * 12 + j + 3] = forward[j + 3 * i]
			state[9 + i * 12 + j + 6] = right[j + 3 * i]
			state[9 + i * 12 + j + 9] = back[j + 3 * i]
	state[45:54] = down
	return state