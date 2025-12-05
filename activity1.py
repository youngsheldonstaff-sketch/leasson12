ip= input("enter a string:")

char = input ("enter your own charecter: ")

i=0
count=0

while (i<len(ip)):
    if (ip[i]== char):
        count = count + 1
    i= i+1

print ("the total number of times",char ,"has appread is",count)
