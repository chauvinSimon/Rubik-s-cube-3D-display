# To express the color scan in another order:
# -input: string using the notation where the unfolded cube is read line by line 
# -output: string using the notation where the unfolded cube is read block by block (U + R + F + D + L + B) 

def convert_line_to_cube(input):
	R =  input[15:18] + input[27:30] + input[39:42]
	L =  input[9:12] + input[21:24] + input[33:36]
	F =  input[12:15] + input[24:27] + input[36:39]
	B =  input[18:21] + input[30:33] + input[42:45]
	U = input[0:9]
	D = input[45:54]
	output = "" + U + R + F + D + L + B
	return(output)