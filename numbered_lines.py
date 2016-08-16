#!/usr/bin/env python3
def numbered_lines(filename):
	with open(filename, 'r') as fin:
		lines = fin.readlines()
	with open('new_' + filename, 'w') as fout:
		n = 1
		for line in lines:
			if line != '\n':
				fout.write(str(n) + " " + line)
			n += 1

def main():
    numbered_lines('small.txt')

if __name__ == "__main__":
    main()
