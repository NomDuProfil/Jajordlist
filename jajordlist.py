from itertools import product
import argparse, sys

letters_mapping = {
	'a': ['a', 'A', '@'],
	'b': ['b', 'B', '8'],
	'e': ['e', 'E', '3'],
    'i': ['i', 'I', '!'],
	'g': ['g', 'G', '6'],
	'l': ['l', 'L', '!'],
    'o': ['o', 'O', '0'],
	's': ['s', 'S', '$', '5'],
	't': ['t', 'T', '7'],
	'0': ['0'],
	'1': ['1'],
	'2': ['2'],
	'3': ['3'],
	'4': ['4'],
	'5': ['5'],
	'6': ['6'],
	'7': ['7'],
	'8': ['8'],
	'9': ['9']
}

def generate_map(basic, word):
	dict_final = {}
	for current_char in word:
		if current_char in basic:
			dict_final[current_char] = basic[current_char]
		else:
			dict_final[current_char] = [current_char, current_char.upper()]
	return dict_final

def pw_vars(pw, equivs):
	if not pw: return ('',)
	return (c + var for c in [pw[0]] + equivs.get(pw[0]) for var in pw_vars(pw[1:], equivs))

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--base", help="Basic word for generation in lower case. Example: \"enterprise\"", required=True)
parser.add_argument("--numberbefore", help="Number of numbers before the base word.")
parser.add_argument("--numberafter", help="Number of numbers after the base word.")

args = parser.parse_args()

if not len(sys.argv) > 1:
	parser.print_help()
	sys.exit(1)

basicword = args.base.lower()

numberbefore = 0
numberafter = 0

if args.numberbefore is not None:
	if args.numberbefore.isdigit():
		numberbefore = int(args.numberbefore)
	else:
		print("Error with \"numberbefore\"")
		sys.exit(1)
if args.numberafter is not None:
	if args.numberafter.isdigit():
		numberafter = int(args.numberafter)
	else:
		print("Error with \"numberafter\"")
		sys.exit(1)

mapping_generation = generate_map(letters_mapping, basicword)

start_list = [basicword, basicword+'!']
outputfile = open('jajesult.txt', 'w+')
outputfile.write(basicword+'\n')
outputfile.write(basicword+'!\n')

for current_result in list(dict.fromkeys(list(pw_vars(basicword, mapping_generation)))):
	outputfile.write(current_result+'\n')
	outputfile.write(current_result+'!\n')
	start_list.append(current_result)
	start_list.append(current_result+'!')

if numberbefore > 0:
	formatwithzero = "{:0"+str(numberbefore)+"d}"
	numberbefore = numberbefore*"9"
	for i in range(int(numberbefore)+1):
		for current in start_list:
			if len(str(i)) < len(str(numberbefore)):
				outputfile.write(formatwithzero.format(i)+current+'\n')
				outputfile.write(formatwithzero.format(i)+current+'!\n')
			outputfile.write(str(i)+current+'\n')
			outputfile.write(str(i)+current+'!\n')

if numberafter > 0:
	formatwithzero = "{:0"+str(numberafter)+"d}"
	numberafter = numberafter*"9"
	for i in range(int(numberafter)+1):
		for current in start_list:
			if len(str(i)) < len(str(numberafter)):
				outputfile.write(current+formatwithzero.format(i)+'\n')
				outputfile.write(current+formatwithzero.format(i)+'!\n')
			outputfile.write(current+str(i)+'\n')
			outputfile.write(current+str(i)+'!\n')

outputfile.close()

print('Done!')