import random
#Integers
print(random.randint(1,10))

print(type('Sam')) #returns the type of class
if isinstance(5, int):
    print('An integer')

#Strings
print('''Hello 
world''')

print('Hello world'.split(' '))
word = "Sharma's Kitchen"
print(word)
print(word.replace('Kitchen', 'Family'))
print(word[3])
wordLen = len(word)
print(wordLen)
print(word[3:wordLen:2])


#Boolean
a = True
b = False
if a:
    print('a is true')
    print('no')
if b:
    print('b is true')
    print("hello")
else:
    print('b is false')

