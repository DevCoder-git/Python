#remove space without built in function
a=input("Enter a string : ")
for i in a:
    if(i==" "):
        continue
    else:
        print(i,end="")
