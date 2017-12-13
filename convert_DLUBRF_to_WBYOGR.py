# Optional script: converting colors to face notations
# Useful to check and solve the cube with [Kociemba's Algorithm in JS](http://cube.rcombs.me)

def convert_DLUBRF_to_WBYOGR(face):
	dict_DLUBRF = {"D" : "W", "L" : "B", "U" : "Y", "B" : "O", "R" : "G", "F" : "R"}
	config_DLUBRF = ""
	for elm in face:
		config += my_dict[elm]
	return config