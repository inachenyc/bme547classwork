# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def add(a, b):
    c = a + b
    d = a - b
    if c < 0:
        # return  # if c<0, return "None",
        # b/c return stops the func and return whatever is stored
        return "The answer is negative"  # python recognized strings
    return c, d  # can return a tuple (c,d)


answer = add(3, 5)
print(answer)
# if there is no return in function, will print "None"
# even if print(add(3,5)), if add() has no return, bash will return "None"

print(answer[0])
print(answer[1])  # can return one of the tuples by index
# or:
added, subtracted = add(3, 5)
print(added)
print(subtracted)
