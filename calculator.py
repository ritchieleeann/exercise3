from arithmetic import *

start = raw_input("> ")

token = start.split(" ")
operator = token[0]

if operator == "+":
    print add(int(token[1]) , int(token[2]))

if operator == "-":
    print subtract(int(token[1]) , int(token[2]))

if operator == "*":
    print multiply(int(token[1]) , int(token[2]))

if operator == "/":
    print divide(int(token[1]) , int(token[2]))

if operator == "square":
    print square(int(token[1]))

if operator == "cube":
    print cube(int(token[1]))

if operator == "pow":
    print power(int(token[1]) , int(token[2]))

if operator == "mod":
    print mod(int(token[1]) , int(token[2]))

