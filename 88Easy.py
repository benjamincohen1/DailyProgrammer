def main():
	key="GLADOS"
	word="THECAKEISALIE"

	keyArray=[]
	for l in key:
		keyArray.append(ord(l))
		print(l + " "+str(ord(l)))
	newArray=[]
	print(keyArray)
	count=-1
	for l in word:
		count+=1
		newArray.append((ord(l)+keyArray[count%len(keyArray)]%len(keyArray))+65)
		tmp=ord(l)+keyArray[count%len(keyArray)]%26
		print(l + " " + chr((keyArray[count%len(keyArray)])) )
		print(ord(l) + keyArray[count%len(keyArray)])

	for l in newArray:
		x = chr(l%26 + 65)
		print(str(x))

main()