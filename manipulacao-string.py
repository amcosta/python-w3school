word = 'Hello World'

# print character by character
i = 0
while i < len(word):
    print(word[i])
    i += 1

# count occurrence
print('count occurrence'.title())
print(word.count('l'))
print(word.count(' '))

print('slice text'.title())
print(word[0])          #get one char of the word
print(word[0:1])        #get one char of the word (same as above)
print(word[0:3])        #get the first three char
print(word[:3])         #get the first three char
print(word[-3:])        #get the last three char
print(word[3:])         #get all but the three first char
print(word[:-3])        #get all but the three last character

print('split'.title())
print(word.split(' '))

print('repeat'.title())
print('.*'*10)

print('replace'.title())
print(word.replace('Hello', 'Goodbye'))

print('reverse'.title())
print(''.join(reversed(word)))
print(word[::-1])

print('strip'.title())
print('   abc   '.strip())
print('   abc   '.lstrip(' '))
print('   abc   '.rstrip(' '))

print('join'.title())
print(':'.join(word))
