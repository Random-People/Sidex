import sys, re, random

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
random.shuffle(code)
print("\n".join(code))