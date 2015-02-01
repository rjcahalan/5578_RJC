## Code It- Week 2
## Enter a user input and count the characters if input is a string

uput = input('Enter input: ')
if isinstance(uput, str) == True: print 'string'
elif isinstance(uput, int) == True: print 'integer'
elif isinstance(uput, float) == True: print 'float'
else: print 'not sure what it is'

ulist = []
udic = dict()

## counts the letters in a string by adding to a dictionary
if isinstance(uput, str) == True:
    for l in uput:
        if l not in udic:  ##adds the letter to the dictionary if it is not already there
            udic[l] = 1
        else:
            udic[l] = udic[l] + 1

print udic       

print "*" * len(uput)
print uput
print "*" * len(uput)




