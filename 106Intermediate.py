def main():
	jugs=[3,5]
	target=4;
	print(findSolution(jugs,target,""))

def findSolution(jugs,target,string):
	curJugs=jugs;
	if(curJugs[0]==target or curJugs[1]==target):
		return str
	else:
		string+="Pour "
		string+= str(jugs[0])
		string+=" gallons into other jug"
		curJugs=[0,curJugs[0]+curJugs[1]]
		#findSolution(curJugs,target,string)

main()