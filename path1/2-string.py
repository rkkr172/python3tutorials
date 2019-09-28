'''
Strings are used in Python to record text information, such as names. Strings in Python are actually a sequence,
which basically means Python keeps track of every element in the string as a sequence. For example, Python understands
the string "hello' to be a sequence of letters in a specific order. This means we will be able to use indexing to grab
particular letters (like the first letter, or the last letter)
https://docs.python.org/3/tutorial/introduction.html#strings
'''

s = 'Hello World'

print(type(s))
print("length of string is: {}".format(len(s)))

print(s[0])
print(s[1:])
print(s[:-1])
# step size with ::
print(s[::1])
print(s[::2])
print(s[::3])
print(s[::-1])

for c in s:
    if c == ' ':
        continue
    print(c)

'''
 https://docs.python.org/3/library/stdtypes.html#textseq
 https://docs.python.org/3/library/stdtypes.html#old-string-formatting
'''
print(s.capitalize())
print(s.upper())
print(s.lower())
x = 'Py' in 'Python'
print(x)



