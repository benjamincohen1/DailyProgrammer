import random
import time
def main():

	wordspersec=[]
	trials=10
	for x in range(0,trials):
		start=time.clock()
		dic=[]
		words=[]
		lets1="abcdefghijklmnopqrstuvwxyz "
		lets=['th','he','an','re','er','in','on','at','nd','st','es','en','of','te','ed','of']
		lets+=['te','ed','or','ti','hi','as','to','ll','ee','ss','oo','tt','ff','rr','nn','pp','cc']
		for z in lets1:
			lets.append(z)
		#lets="aaaaaaaabcccddddeeeeeeeeeeefghhhhhiiiiiilllllmnnnnnooooooprrrrrsssssttttttttuuuvwwyefghijklmonpqrstuvqxyz " 
		for line in open("enable1.txt"):
			dic.append(line)
		curword=""
		while(len(words)<5):
			r=random.choice(lets1)

			#if(r==" "):
			#	print("Checking " + curword+"\n")

			if(r==" " and (curword+"\n") in dic and len(curword) >= 3):
				words.append(curword)
				curword=""
			elif(r==" " and (curword+"\n") in dic and len(curword) < 3):
				curword=""
			elif(r==" "):
				curword=""
			else:
				curword+=r


		print(words)
		t = time.clock()-start
		print("Got "+str(len(words)) + " words in "+str(t)+" seconds, averaging "+str(len(words)/t) + " words/s")
		wordspersec.append(len(words)/t)
	print(wordspersec)
	s=0;
	for i in wordspersec:
		s+=i
	average=s/trials;
	print("Average of averages is: "+str(average) + " words per second") 
main()