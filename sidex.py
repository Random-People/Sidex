import traceback

import sys, random

code = open(sys.argv[1]).read()

code = code.split("\n") # For easy shuffling

out = []

for i in code:
	if len(i) == 0:
		continue
	if i[0] != "#":
		out.append(i)

code = out

# Executing in random order!
# For every iteration, it tries to execute
# every single instruction.

random.shuffle(code)

# Implements a single cycle without garbage collection

while code != []:
	try:
		print(code[0])
		exec(code[0])
		del code[0]
	except NameError as e: # Undefined latch
		code.append(code.pop())
		undef = str(e).split("'")[1]
		if undef == "read":
			pass
	