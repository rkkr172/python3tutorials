'''
Lists can be thought of the most general version of a sequence in Python. Unlike strings, they are mutable,
meaning the elements inside a list can be changed!
https://docs.python.org/3/tutorial/introduction.html#lists
'''
lst = [1,2,3]
print(type(lst))

print(lst[0])
lst[0] = 11     ## changing value
print(lst[0])   ## Acess value
print(lst[:])
print("Doubline List - {}".format(lst*2))

lst.append(5)   ## appending
lst = lst + ['NewItem']     ## Addition List
print(lst)

pop_item = lst.pop(4)
print(lst)
print(pop_item)

# https://en.wikipedia.org/wiki/Fibonacci_number
a = 0 ; b = 1
while a<5:
    print(a)
    a,b=b,a+b       # Here, (a << b) && (b << a+b)
#----------------------------------------------    
a,b = 0,1
while a < 5:
     a,b = b, a+b
     print(f"a={a}, b={b}")
#----------------------------------------------
l1 = [1,2,3] ; l2 = [4,5,6] ; l3 = [7,8,9]
matrix = [ l1 , l2 , l3]
print(matrix)
print(type(matrix))
print(matrix[0][0])

first_col = [ col[0] for col in matrix ]
print("printing First Column here : \n",first_col)

firt_row = matrix[0]
print("printing First Row here : \n",firt_row)
