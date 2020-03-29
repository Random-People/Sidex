import traceback

import keyword
# We don't want any Python keywords appearing
# in a Sidex program.

import sys, random

code = open(sys.argv[1]).read()

code = code.split("\n") # For easy shuffling

out = []

for i in code:
	if len(i) == 0:
		continue
	if i[0] != "#":
		out.append(i)
	for j in keyword.kwlist:
		if j in i:
			raise(SyntaxError) # Refuse to interpret 

code = out

# Executing in random order!
# For every iteration, it tries to execute
# every single instruction.

random.shuffle(code)

# Implements a single cycle without garbage collection

while code != []:
	try:
		# print(code)
		exec(code[0])
		del code[0]
	except NameError as e: # Undefined latch
		if code[0][-4:]!="#ERR":
			code[0]+="#ERR" # Memoize the error
			x = code[0]
			del code[0]
			code.append(x)
			continue
		# print(code)
		undef = str(e).split("'")[1]
		if undef == "read":
			read = input()
	