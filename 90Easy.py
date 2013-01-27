import math
def main():
	p="5 5 PESPESPESPESPNNNNPWSPWSPWSPWSP"

	draw(p)
def draw(str):
	c=int(str[0])
	c2=int(str[2])
	outer=[]
	for x in range(0,c):
		inner=[]
		for y in range(0,c2):
			inner.append(0)
		outer.append(inner)

	pos=(0,0)
	for c in str:
		if(c=="P"):
			outer[pos[0]][abs(pos[1])]=1
		elif(c=="E"):
			pos=(pos[0]+1,pos[1])
		elif(c=="W"):
			pos=(pos[0]-1,pos[1])
		elif(c=="N"):
			pos=(pos[0],pos[1]+1)
		elif(c=="S"):
			pos=(pos[0],pos[1]-1)

		#lets print

	for x in range(0,len(outer)):
		print(outer[x])



main()