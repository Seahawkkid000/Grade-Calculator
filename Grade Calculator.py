a=int(input("How many marks did you get"))
b=int(input("How many marks were available"))
print("You got", a*100//b, "%")
if 80<=a/b*100<=100:
    print("You got an A! Congratulations!")
elif 60<=a/b*100<80:
    print("You got a B! Not Bad But Could Be Better!")
elif 40<=a/b*100<60:
    print("You got a C! Better Luck Next Time!")
elif 0<=a/b*100<40:
    print("You got a D! Needs Improvement!")
else:
    print("Invalid Score! Please Try Again!")
    
