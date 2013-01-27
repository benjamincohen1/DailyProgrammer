def main():
	n = int(input())

	for i in range(n):
	    board = []
	    for j in range(9):
	        board.append([int(k) for k in input().split()])
	    sudoku_solve(board)
	
def sudoku_solve(grid):
	board=[]
	for row in grid:
		row2=[]
		for x in row:
			if(x==0):
				row2.append(["-"])
			else:
				row2.append(int(x))
		board.append(row2)
	solution=backtrace(board)
	printBoard(solution)
def backtrace(config):
    if(isSolution(config)):
        return config
    else:
    	if(len(findPossibleSolutions(config))!=0):
	        for child in findPossibleSolutions(config):
	            solution=backtrace(child)
	            if solution is not None and isValid(solution):
	                return solution
    return None
def isSolution(board):
	try:
		return isValid(board) and board[8][8]!=["-"]
	except:
		return False
def findPossibleSolutions(board):
	numFreq=findNumFreq(board)
	poss=[]
	index="z"
	if(board[8][8]!=["-"]):
		return []
	for x in range(0,9):
		for y in range(0,9):
			if(board[x][y]==["-"]):
				index=(x,y)
				break
			if(index!="z"):
				break
		if(index!="z"):
			break
				
	if(index=="z"):
		return "None"
	for z in range(1,10):
		tmpboard=[]
		for x in range(0,9):
			row=[]
			for y in range(0,9):
				row.append(board[x][y])
			tmpboard.append(row)
		tmpboard[index[0]][index[1]]=numFreq[z-1]
		poss.append(tmpboard)
	pos2=[]
	for x in poss:
		if(isValid(x)):
			pos2.append(x)
	return pos2
def findNumFreq(board):
	freqs=[0,0,0,0,0,0,0,0,0]
	for row in board:
		for num in row:
			if num!=["-"]:
				freqs[int(num)-1]+=1
	dic={}
	arr=[]
	for x in range(0,9):
		dic[x+1]=freqs[x]

	for x in range(0,10):
		for z in sorted(dic):
			if dic[z]==x:
				arr.append(z)
	arr2=[]
	for x in range(0,len(arr)):
		arr2.insert(0,arr[x])
	return arr2
	#return freqs
def isValid(board):
	check=True
	for row in board:
		if(not isValidRow(row)):
			check=False
	for i in range(0,9):
		col=[]
		for x in board:
			col.append(x[i])
		if(not isValidRow(col)):
			check=False
	firstNine=[]
	a1,a2,a3,a4,a5,a6,a7,a8,a9=[],[],[],[],[],[],[],[],[]
	a1.append(board[0][:3])
	a1.append(board[1][:3])
	a1.append(board[2][:3])
	a2.append(board[0][3:6])
	a2.append(board[1][3:6])
	a2.append(board[2][3:6])
	a3.append(board[0][6:])
	a3.append(board[1][6:])
	a3.append(board[2][6:])
	a4.append(board[3][:3])
	a4.append(board[4][:3])
	a4.append(board[5][:3])
	a5.append(board[3][3:6])
	a5.append(board[4][3:6])
	a5.append(board[5][3:6])
	a6.append(board[3][6:])
	a6.append(board[4][6:])
	a6.append(board[5][6:])
	a7.append(board[6][:3])
	a7.append(board[7][:3])
	a7.append(board[8][:3])
	a8.append(board[6][3:6])
	a8.append(board[7][3:6])
	a8.append(board[8][3:6])
	a9.append(board[6][6:])
	a9.append(board[7][6:])
	a9.append(board[8][6:])
	tmp=[a1,a2,a3,a4,a5,a6,a7,a8,a9]
	for x in tmp:
		if(not isValidNine(x)):
			check = False
	return check
def isValidNine(inp):
	count=0
	already=[]
	for row in inp:
		for c in row:
			if(c!=["-"]):
				count+=1
				if int(c) not in already:
					already.append(int(c))
	return len(already)==count

def isValidRow(row):
	count=0
	already=[]
	for c in row:
		if(c!=["-"]):
			count+=1
			if int(c) not in already:
				already.append(int(c))
	return len(already)==count
def printBoard(brd):
	try:
		for x in range(0,9):
			line=""
			for y in brd[x]:
				if(y==["-"]):
					line+="0 "
				else:
					line+=str(y)+" "
			print(line)
		print("")
	except:
		pass
main()
