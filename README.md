## [Sidex](https://github.com/A-ee/Sidex)
This post aims to be the only practical language in this thread. (That means it isn't as hard to write in as the esolangs, but it's still challenging given that you are new to the language. I'll *try* to write an interpreter if I have time.)

Sidex is a **practical** language (feel free to disagree on that) with a primary focus on concurrency. On every iteration, Sidex tries to execute every line at a random order. It will halt (as well as outputting the global variable scheme) only if it fails, or a halting thread(i.e. line) is executed. The filename extension is `.six`.

## Execution
Sidex is quite similar to [Whenever](https://www.dangermouse.net/esoteric/whenever.html). However, Sidex does not have clauses specifying executing a line conditionally.

Sidex doesn't have any control flow other than an implicitly-wrapped infinite loop; instead, the only form of sequential control flow isn't sequential; they might execute at any order.

## Latches

A latch acts similarly with a variable. It consists of an identifier starting with a letter, and the remaining of the identifier is either a number or a character (like JavaScript, for example). Unlike variables, it can be locked (that means its value is unaccessible) after its value is assigned. Latches are initially locked. If they are open, their initial value is `0`. If a thread tries to access a locked latch, the thread will be skipped without throwing an error.

Sidex will skip a line if the latch isn't open. If the latch still isn't open after a complete execution, it continues. If all accessed latches are locked, it raises a deadlock exception (in order to participate in the deadlock challenge).

If a latch is unlocked, assigned a value, then locked, if you unlock that latch, you will still be able to obtain the value; the value isn't discarded.

The input is a special latch that is only unlocked whenever a line of input is entered. If there are no more inputs, all threads using this latch will always be locked. The name of the input latch is simply referred to as `input`.

## Garbage collection
(Considering that writing Sidex can potentially be unhalting, Sidex implements a terrible garbage collection system.)

In order to make sure that scripts are running at the optimal speed, Sidex will delete the process that consumes the most resources after every step. However, if two processes use an equal amount of resources, both of then will be deleted. Deleted threads will no longer exist in the source code, therefore they won't be executed anymore.

The number of resources consumed of a process is counted as the number of non-whitespace bytes in a line.
## Function reference
All of the functions take one single operand. These functions can nest.

* <code>unlock()</code> Takes a single string as an operand. It tries to open the latch that is specified in the string.
* <code>lock()</code> Opposite of `unlock()`. It tries to close the latch that is specified in the string.
* <code>print()</code> Prints the body expression to STDOUT.
* <code>read</code> A latch that is only unlocked right after a line of input is executed.
* <code>str()</code> converts the number to a string.
* <code>thread()</code> appends a new thread to the source code.

## Operator reference
* <code>+</code>
* <code>-</code>
* <code>*</code>
* <code>/</code>
* <code>%</code>
* <code>=</code> Opens a latch if it isn't open (latches are initially of the value 1); Assign the value to the latch.
* <code>:=</code> If there is already a value in the latch, do nothing. Otherwise, assign the operand to the latch.
## Example programs
### Collatz sequence
```
thread("1+1"*100)
# Add a thread to prevent garbage collection from collecting away the main processes

n := read
# Comments have to start with a new line.

unlock("S" + str(n % 2))
# Resources: 15. [open, (, ", S, ", concat, ", $, {, n, %, 2, }, ", )].
# Usually every symbol is a lexical item, unless that is an identifier, a number, or part of a string.

# You can't concatenate a string with an integer.

n = S0 + 3 * n + 1
# If that isn't unlocked.
n = S1 + n / 2
# Likewise, this execution is also conditional.

print(S0 + n)
print(S1 + n)
# n is either even or odd, so this will happen after the S. latch is unlocked.

lock("S0")
# Won't execute if S0 is already closed
lock("S1")
# Won't execute if S1 is already closed

# Sidex automatically locks all latches at the end of an iteration.
```
(Compressed:)
```
thread("1+1"*100)
n:=read
unlock("S"+str(n % 2))
n=S0+3*n+1
n=S1+n/2
print(S0+n)
print(S1+n)
```
### Who Goes There
```
print("Halt!\nWho goes there?")
print("You may pass, "+read+00)

# On the next iteration the latch "read" is undefined, therefore it halts.
```
### Count up by 1s
```
thread("1+1"*100)
I = I + 1
print(I)
lock("I")
```
