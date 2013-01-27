def main():
	x=10
	s=0
	for z in range (0,x+1):
		if(z%3!=0 and z%14!=0 and z%100!=0):
			s+=1
	print(s)
main()