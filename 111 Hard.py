def main():
	print(jos(41,3))
	print(jos(123456789101112,4))

def jos(soldiers,count):
	s=[]
	for i in range(1,soldiers+1):
		s.append(i)
	return josHelper(s,count,0)

def josHelper(soldiers,count,ind):
	if len(soldiers)==1:
		return soldiers.pop(0)
	else:
		if (ind+count <= len(soldiers)):
			ind+=count-1
			x=soldiers.pop(ind)
			return josHelper(soldiers,count,ind)
		else:
			ind=(ind+count)%len(soldiers)-1
			z=soldiers.pop(ind)

			return josHelper(soldiers,count,ind)

main()