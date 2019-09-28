# https://docs.python.org/3/tutorial/controlflow.html#for-statements
word = ['cat','Dog','Rat','Hello']

for w in word[:]:
    if len(w) > 4:
        word.insert(0,w)

print(word)

print(range(5))
print(list(range(5)))
print(tuple(range(5)))

for i in range(5):
    print(i)
