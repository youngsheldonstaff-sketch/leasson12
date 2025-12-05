char1 = int(input ("enter a number: "))

t= char1
numlen = 0

while (t>0):
    numlen = numlen + 1
    t= int(t/10)

if numlen >=4:
    numlen = int(numlen/2)
    chk=0
    while char1>0:
        rem = char1 % 10
        if chk == numlen:
            midone = rem
        elif chk == (numlen -1):
            mid2 = rem
        char1 = int (char1/10) 
        chk = chk +1
    prod = midone * mid2
    print(" the product of the middle 2 digits is:", prod) 
else:
    print ("please enter a number with atleast 4 digits")
