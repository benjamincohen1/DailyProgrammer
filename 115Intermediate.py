def main():
	f=open("14.txt")
	pairs=int(f.readline())
	numArray=f.readline().split()
	target=int(f.readline())
	index=0
	m={}
	for x in range(pairs):
		#m[int(x)]=target-int(x)
		if str(target-int(numArray[x])) in numArray[x:]:
			print(numArray[x]+","+str(target-int(numArray[x])))

	print(m)
main()