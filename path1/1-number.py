a=5
b=2
print("Addition - {}".format(a+b))
print("Difference - {}".format(a-b))
print("Mulitply - {}".format(a*b))
print("Division - {}".format(a/b))
print("Floor Division - {}".format(a//b))
print("Modulus - {}".format(a%b))

dog= 2
cat = 1
sum = dog + cat
print(f"I have {sum} pets in the house.")

'''
The names you use when creating labels need to follow a few rules:
1. Names can not start with a number.
2. There can be no spaces in the name, use _ instead.
3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
4. It's considered best practice (PEP8) that names are lowercase.
5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), 
   or 'I' (uppercase letter eye) as single character variable names.
6. Avoid using words that have special meaning in Python like "list" and "str"

Python lets you add, subtract, multiply and divide numbers with reassignment using +=, -=, *=, and /=.
example:
'''
num = 2
num += 10
print("Output by shortcut - {}".format(num))

'''
You can check what type of object is assigned to a variable using Python's built-in type() function. Common data types include:
    int (for integer)
    float
    str (for string)
    list
    tuple
    dict (for dictionary)
    set
    bool (for Boolean True/False)
'''
i = 123; f = 10.54 ; s = 'name'; l = [1,2,3] ; t = (1,2,3) ; d = {(1,'a'),(2,'b')} ; myset = {1,2,3} ; b = True;
print(type(i))
print(type(f))
print(type(s))
print(type(l))
print(type(d))
print(type(t))
print(type(t))
print(type(myset))
print(type(b))

# https://docs.python.org/3/tutorial/introduction.html#numbers