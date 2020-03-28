## Sidex
This post aims to be the only practical language in this thread. (That means it isn't as hard to write in as the esolangs, but it's still challenging given that you are new to the language. I'll *try* to write an interpreter if I have time.)

Sidex is a domain-specific **practical** language (feel free to disagree on that) with a primary focus on concurrency. On every iteration, Sidex tries to execute every line at a random order. It will halt (as well as outputting the global variable scheme) only if it fails, or a halting thread(i.e. line) is executed. The filename extension is `.six`.

## Execution
Sidex is quite similar to [Whenever](https://www.dangermouse.net/esoteric/whenever.html). However, Sidex does not have clauses specifying executing a line conditionally.

In Sidex, every line of code executes at a random order. However, if two lines are connected with an unterminated string, they are not executed at a different order. Instead, these two lines still act as just one line and are connected together.

Sidex doesn't have any control flow other than an implicitly-wrapped infinite loop; instead, the only form of sequential control flow isn't sequential; they might execute at any order. As a complement, the whole program is wrapped in an infinite loop.

## Latches

A latch acts similarly with a variable. It consists of an identifier starting with a letter, and the remaining of the identifier is either a number or a character (like JavaScript, for example). Unlike variables, it can be locked (that means its value is unaccessible) after its value is assigned. Latches are initially locked. If they are open, their initial value is `0`. If a thread tries to access a locked latch, the thread will be skipped without throwing an error.

Sidex will skip a line if the latch isn't open. If the latch still isn't open after a complete execution, it continues. If all accessed latches are locked, it raises a deadlock exception (in order to participate in the deadlock challenge).

If a latch is unlocked, assigned a value, then locked, if you unlock that latch, you will still be able to obtain the value; the value isn't discarded.

The input is a special latch that is only unlocked whenever a line of input is entered. If there are no more inputs, all threads using this latch will always be locked. The name of the input latch is simply referred to as `input`.

## Garbage collection [todo]
(Considering that writing Sidex can be unintuitive, Sidex implements a terrible garbage collection system.)

In order to make sure that scripts are running at the optimal speed, Sidex will delete the process that consumes the most resources after every step. However, if two processes use an equal amount of resources, both of then will be deleted. Deleted threads will no longer exist in the source code, therefore they won't be executed anymore.

The number of resources consumed of a process is counted as the number of lexical items in that line of process. String interpolation also count as separate items.
## Function reference
All of the functions take one single operand. These functions can nest.
* <code>open()</code> Takes a single string as an operand. It tries to open the latch that is specified in the string.

## Operator reference
## Example programs
### Collatz sequence for 1 iteration
```
# Comments have to start with a new line.
open("S" + "${n % 2}")
# Resources: 15. [open, (, ", S, ", concat, ", $, {, n, %, 2, }, ", )].
# Usually every symbol is a lexical item, unless that is an identifier, a number, or part of a string.

# You can't concatenate a string with an integer.

S0 + 3 * n + 1 -> n
# If that isn't unlocked.
S1 + n / 2     -> n
# Likewise, this execution is also conditional.

close("S0")
# Won't execute if S0 is already closed
close("S1")
# Won't execute if S1 is already closed

assert(n != 1)

open("O" + "P" + "E" + "N")
# We need to make sure that this goes on for at least 1 iteration.
```
### Who Goes There
```
print("Halt!
Who goes there?")
print("You may pass, ${input}")
# This employs string interpolation inside strings.
```
