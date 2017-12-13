import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

from convert_block_to_line import convert_block_to_line

# -input: string representing the colors of each square - like "ROOGYGORRGYBRGOBYRGYWRRBOOWBGRBWBOBYYRYGBWGWWYYGWOWBOW"
# -output: none. Prompt a windows where the 3D plot is made

def display3D(scan):
	
	# Two string representations are possible:
	# if using the notation where the unfolded cube is read line by line 
	# input = scan
	
	# if using the notation where the unfolded cube is read block by block (U + R + F + D + L + B) 
	input = convert_block_to_line(scan)

	# color codes for the plot
	colour_dict = {"B" : "blue", "W" : "white", "R" : "red", "G" : "lawngreen", "Y" : "yellow", "O" : "orange"}

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	# nodes on the cube
	pts = np.array([
	[0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
	[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3],
	[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	])

	# elementary translation
	x_shift = [
		[1, 0, 0],
		[1, 0, 0], 
		[1, 0, 0],
		[1, 0, 0]
	]
	y_shift = [
		[0, 1, 0],
		[0, 1, 0], 
		[0, 1, 0],
		[0, 1, 0]
	]
	z_shift = [
		[0, 0, 1],
		[0, 0, 1], 
		[0, 0, 1],
		[0, 0, 1]
	]

	# Processing each face
	# Face U
	vert0U = [
		[0, 2, 3],
		[1, 2, 3], 
		[1, 3, 3],
		[0, 3, 3]
	]
	vertsU = []
	colorU = input[0:9]
	shiftsU = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [0, -1, 0], [1, -1, 0], [2, -1, 0], [0, -2, 0], [1, -2, 0], [2, -2, 0], [0, -3, 0], [1, -3, 0], [2, -3, 0]]
	for i in range(9):
		verts_temp = np.add(vert0U, np.multiply(x_shift,shiftsU[i][0]))
		verts_temp  = np.add(verts_temp , np.multiply(y_shift,shiftsU[i][1]))
		verts_temp  = np.add(verts_temp , np.multiply(z_shift,shiftsU[i][2]))
		ax.add_collection3d(Poly3DCollection([verts_temp], facecolors=colour_dict[colorU[i]]))

	# Face D
	vert0D = [
		[0, 2, 0],
		[1, 2, 0], 
		[1, 3, 0],
		[0, 3, 0]
	]
	LD1=input[45:48]
	LD2=input[48:51]
	LD3=input[51:54]
	vertsD = []
	colorD = LD3 + LD2 + LD1
	shiftsD = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [0, -1, 0], [1, -1, 0], [2, -1, 0], [0, -2, 0], [1, -2, 0], [2, -2, 0], [0, -3, 0], [1, -3, 0], [2, -3, 0]]
	for i in range(9):
		verts_temp = np.add(vert0D, np.multiply(x_shift,shiftsD[i][0]))
		verts_temp  = np.add(verts_temp , np.multiply(y_shift,shiftsD[i][1]))
		verts_temp  = np.add(verts_temp , np.multiply(z_shift,shiftsD[i][2]))
		ax.add_collection3d(Poly3DCollection([verts_temp], facecolors=colour_dict[colorD[i]]))

	# Face R
	vert0R = [
		[3, 0, 3],
		[3, 0, 2], 
		[3, 1, 2],
		[3, 1, 3]
	]
	vertsR = []
	colorR = input[15:18] + input[27:30] + input[39:42] 
	shiftsR = [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 0, -1], [0, 1, -1], [0, 2, -1], [0, 0, -2], [0, 1, -2], [0, 2, -2], [0, 0, -3], [0, 1, -3], [0, 2, -3]]
	for i in range(9):
		verts_temp = np.add(vert0R, np.multiply(x_shift,shiftsR[i][0]))
		verts_temp  = np.add(verts_temp , np.multiply(y_shift,shiftsR[i][1]))
		verts_temp  = np.add(verts_temp , np.multiply(z_shift,shiftsR[i][2]))
		ax.add_collection3d(Poly3DCollection([verts_temp], facecolors=colour_dict[colorR[i]]))

	# Face L
	vert0L = [
		[0, 3, 3],
		[0, 2, 3], 
		[0, 2, 2],
		[0, 3, 2]
	]
	vertsL = []
	colorL = input[9:12] + input[21:24] + input[33:36] 
	shiftsL = [[0, 0, 0], [0, -1, 0], [0, -2, 0], [0, 0, -1], [0, -1, -1], [0, -2, -1], [0, 0, -2], [0, -1, -2], [0, -2, -2], [0, 0, -3], [0, -1, -3], [0, -2, -3]]
	for i in range(9):
		verts_temp = np.add(vert0L, np.multiply(x_shift,shiftsL[i][0]))
		verts_temp  = np.add(verts_temp , np.multiply(y_shift,shiftsL[i][1]))
		verts_temp  = np.add(verts_temp , np.multiply(z_shift,shiftsL[i][2]))
		ax.add_collection3d(Poly3DCollection([verts_temp], facecolors=colour_dict[colorL[i]]))

		
	# Face F
	vert0F = [
		[0, 0, 2],
		[1, 0, 2], 
		[1, 0, 3],
		[0, 0, 3]
	]
	vertsF = []
	colorF = input[12:15] + input[24:27] + input[36:39]
	shiftsF = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [0, 0, -1], [1, 0, -1], [2, 0, -1], [0, 0, -2], [1, 0, -2], [2, 0, -2], [0, 0, -3], [1, 0, -3], [2, 0, -3]]
	for i in range(9):
		verts_temp = np.add(vert0F, np.multiply(x_shift,shiftsF[i][0]))
		verts_temp  = np.add(verts_temp , np.multiply(y_shift,shiftsF[i][1]))
		verts_temp  = np.add(verts_temp , np.multiply(z_shift,shiftsF[i][2]))
		ax.add_collection3d(Poly3DCollection([verts_temp], facecolors=colour_dict[colorF[i]]))

	# Face B
	vert0B = [
		[0, 3, 2],
		[1, 3, 2], 
		[1, 3, 3],
		[0, 3, 3]
	]
	vertsB = []
	LB1=input[18:21]
	LB2=input[30:33]
	LB3=input[42:45]

	colorB = LB1[::-1] + LB2[::-1] + LB3[::-1]
	shiftsB = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [0, 0, -1], [1, 0, -1], [2, 0, -1], [0, 0, -2], [1, 0, -2], [2, 0, -2], [0, 0, -3], [1, 0, -3], [2, 0, -3]]
	for i in range(9):
		verts_temp = np.add(vert0B, np.multiply(x_shift,shiftsB[i][0]))
		verts_temp  = np.add(verts_temp , np.multiply(y_shift,shiftsB[i][1]))
		verts_temp  = np.add(verts_temp , np.multiply(z_shift,shiftsB[i][2]))
		ax.add_collection3d(Poly3DCollection([verts_temp], facecolors=colour_dict[colorB[i]]))

	# nodes
	c, m = ('k', 'o')
	for i in range(2,6):
		ax.scatter(pts[0], pts[1], pts[i], c=c, marker=m)

	# Plot
	plt.title('3D plot Rubik-s-Cube')
	plt.show()