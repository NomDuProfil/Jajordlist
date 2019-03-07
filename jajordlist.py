from itertools import product

basicword = "abcde"

numberbefore = 4
numberafter = 0

wordlistfinal = []

wordlistupperlower = list(map(''.join, product(*(sorted(set((current.upper(), current.lower()))) for current in basicword))))

wordlistupperlowerwithnumber = []
if numberbefore > 0:
	formatwithzero = "{:0"+str(numberbefore)+"d}"
	numberbefore = numberbefore*"9"
	for i in range(int(numberbefore)+1):
		for current in wordlistupperlower:
			if len(str(i)) < len(str(numberbefore)):
				wordlistupperlowerwithnumber.append(formatwithzero.format(i)+current)
			wordlistupperlowerwithnumber.append(str(i)+current)

if numberafter > 0:
	numberafter = numberafter*"9"
	formatwithzero = "{:0"+str(numberafter)+"d}"
	for i in range(int(numberafter)+1):
		for current in wordlistupperlower:
			wordlistupperlowerwithnumber.append(current+str(i))
			if len(str(i)) < len(str(numberafter)):
				wordlistupperlowerwithnumber.append(formatwithzero.format(i)+current)

wordlistupperlowerandchar = []

for current in wordlistupperlowerwithnumber:
	wordlistupperlowerandchar.append(current.replace('a', '@'))
	wordlistupperlowerandchar.append(current.replace('o', '0'))
	wordlistupperlowerandchar.append(current.replace('e', '3'))
	wordlistupperlowerandchar.append(current.replace('a', '@').replace('o', '0').replace('e', '3'))
	wordlistupperlowerandchar.append(current.replace('a', '@').replace('o', '0'))
	wordlistupperlowerandchar.append(current.replace('a', '@').replace('e', '3'))
	wordlistupperlowerandchar.append(current.replace('o', '0').replace('e', '3'))

wordlistfinal = wordlistupperlower+wordlistupperlowerwithnumber+wordlistupperlowerandchar

outputfile = open('jajordlist.txt', 'w+')
for current in wordlistfinal:
	outputfile.write(current+'\n')
outputfile.close()
