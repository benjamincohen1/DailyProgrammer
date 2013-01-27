import re
def main():
	s=input()
	p=re.sub('\w\*\w',"",s)
	p=re.sub('\w\*',"",p)
	p=re.sub('\*\w',"",p)
	print(p)


main()