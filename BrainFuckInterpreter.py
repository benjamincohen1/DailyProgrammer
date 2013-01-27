def main():
	#bf=input();  #get from user
	bf="++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>. "  #simple hello world
	#bf=">,[>,]<[.<]"  #reverse input
	#bf=">,[>>>++++++++[<[<++>-]<+[>+<-]<-[-[-<]>]>[-<]<,>>>-]<.[-]<<]"  #binary to ASCII
	#bf="++++++++[>++++[>++>+++>+++>+<<<<-]>+>->+>>+[<]<-]>>.>>---.+++++++..+++.>.<<-.>.+++.------.--------.>+.>++."  #hello world with line break

	#bf=">++++++++++>>+<+[[+++++[>++++++++<-]>.<++++++[>--------<-]+<<]>.>[->[<++>-[<++>-[<++>-[<++>-[<-------->>[-]++<-[<++>-]]]]]]<[>+<-]+>>]<<]" #powers of 2
	print("Calling BF interpreter on: "+bf)
	t=[]
	for x in range(0,100):
		t.append(0)
	interpret(bf,t,0)



def interpret(code,tape,index):
	index2=0
	for char in code:
		index2+=1
		remainingCode=code[index2:]
		if char==">":
			index+=1
		elif char=="<":
			if(index>0):
				index-=1
			else:
				print("Can't go negative")
				break
		elif char=="+":
			try:
				tape[index]+=1
			except:
				tape.insert(index,1)
		elif char=="-":
			try:
				tape[index]-=1
			except:
				print("Can't have negative value")
				break
		elif char==".":
			print(chr(tape[index]))
		elif char==",":
			inp=ord(input())
			try:
				tape[index]=inp
			except:
				tape.insert(index,inp)
		elif char=="[":
			c=getLoopCode(remainingCode)
			while (tape[index]>1):
				interpret(c,tape,index)
		elif char=="]":
			 pass
"""
def getLoopCode(code):
	opens=1
	tmp=""
	for c in code:
		if c=="]" and opens ==1:
			#tmp+="]"
			return tmp
		if c=="]" and opens!=1:
			opens-=1
			tmp+="]"
		elif c=="[":
			opens+=1
			tmp+="["
		else:
			tmp+=c

"""
def getLoopCode(code):
	openBrackets=1
	tmp=""
	for c in code:
		if c=="]":
			if openBrackets==1:
				return tmp
			else:
				openBrackets-=1
				tmp+="]"
		elif c=="[":
			openBrackets+=1
			tmp+="["
		else:
			tmp+=c


main()
