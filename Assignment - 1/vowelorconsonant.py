#write a program to check whether a character is vowel or consonant
#algorithm
#1. Start
#2. Read the character
#3. Check whether the character is vowel or consonant
#4. If it is vowel, print "Vowel"
#5. Else, print "Consonant"
#6. Stop

a=str(input("Enter a string : "))
if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u' or a=='A' or a=='E' or a=='I' or a=='O' or a=='U'):
    print("Vowel")
else:
    print("Consonant")
