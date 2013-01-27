import random
def main():
	r=random.randint(1,100)
	x=0
	while(x!=r):
		x=int(input("Enter a guess: "))
		if(x>r):
			print("Try Lower")
		elif(x<r):
			print("Try Higher")
	print("Winner!")
main()