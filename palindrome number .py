fh=open("output 7.txt",'w')
a=input("enter the value of a:")
reverse=a[:: -1]
if(a==reverse):
    fh.write("it is a palindrome number"+str(a))
else:
    fh.write(a"is not a palindrome number"+str(a))