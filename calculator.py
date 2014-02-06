from arithmetic import *

start = raw_input("> ")

token = start.split(" ")
operator = token[0]
var1 = int(token[1])
var2 = int(token[2])

if operator == "+":
    print add(var1 , var2)
