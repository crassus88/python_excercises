#! /usr/bin/env python3

import traceback

def print_type(x):
    """Prints the value and type of an object in a formatted way."""
    print("{0} is a(n) {1}".format(x, type(x)))


print('The "type() function prints an object\'s type"')  # Don't pay attention to the string constant now
i = 2
print_type(i)

print("-"*20)

print("In python 2.X '/' means integer division if both operands are int and float division if at least one of them is float")
print("In python 3.X it is always float division")
a = i/3
b = i/2
c = i/2.0
print_type(a)
print_type(b)
print_type(c)

print("-"*20)

print("Both in python 2.X and 3.X '//' means integer division, even if the operands are float")
a = i//3
b = i % 3
c = i//3.0
print_type(a)
print_type(b)
print_type(c)

print("-"*20)
print("-"*20)

s = "spam"
print_type(s)

print("-"*20)

print("You can use double or single quotes to denote a string and use the other type inside the string without escaping it.")
print("It's?")
print('"My hovercraft is full of eels." - The Hungarian with the faulty phrasebook')

print("-"*20)

s = r"""You can use triple quotes to avoid having to add linefeed characters ('\n') manually.
And it also let's you use both kinds of quotation marks inside your string.
The character 'r' before a string denotes a "raw string". This means that characters having a special meaning in strings
are treated like simple characters. Such character sequences are \ and {}."""
print(s)
print("\nTriple quoted strings also serve the special purpose of documenting functions, as you can see in the function above")
