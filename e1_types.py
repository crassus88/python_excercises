#! /usr/bin/env python3

import traceback

def print_type(x):
    """Prints the value and type of an object in a formatted way."""
    print("{0} is a(n) {1}".format(x, type(x)))


print('The "type() function returns an object\'s type"')  # Don't pay attention to the string constant now
i = 2
print_type(i)

print("-"*20)

print("In python 2.X '/' means integer division if both operands are int and float division if at least one of them is float")
print("In python 3.X it is always float division. In python 2.X this is achieved with the truediv() function.")
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

print("-"*20)

s = """A string is considered a list of characters thus it has some features in common with lists.
Fpr example characters in a string can be accessed by their position in the string via indexing."""
print(s)
print(s[0])

s = "Slicing is a neat feature in python. It is indexing a whole range at a time."
print(s)
print((s[13:17] + ", isn't it!?").capitalize())

print("-"*20)

s = """As seen in the previous example, strings can be added together. Another way of combining strings is the format() 
function. You can put placeholders in your string that will be populated when calling this function on said string.
format() actually has a whole mini language for specifying the appearance of the data put in these placeholders.
Read more about using format() at {}
Although parts of the documentation may read like chinese at first, it always has examples to clarify usage.
""".format("https://docs.python.org/3/library/string.html")
print(s)

s = """Throughout this code you can see that strings can not only be added together - which is called concatenation - 
but also multiplied by integers. They can not be divided however. Or be subtracted from one-another. And they also can
not be added to other types of objects."""
print(s)
try:
    print(s + 2)
except:
    traceback.print_exc()

print("-"*20)

# todo string functions starting with capitalize
