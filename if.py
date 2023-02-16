#if statement
x=12
marks=10
grade=57
if(x>0):
    print("The number is positive")
#if... else statement
if(marks>=50):
    print("You Passed")
else:
    print("You Failed")
#if.. elif.. else statement
if(grade>=30 and grade<=0):
    print("You Failed Terribly")
elif grade>=30 and grade<=49:
    print("You Passed")
elif grade>=50 and grade<=79:
    print("You have a credit")
elif grade>=80 and grade<=100:
    print("You have a distinction")
else:
    print("Incorrect grade input")

#if.. elif.. else statement
cluster=69
if(cluster>=0 and cluster<=20):
    print("Did not qualify")
elif cluster>20 and cluster<=40:
    print("Slightly below average")
elif cluster>40 and cluster<=60:
    print("Qualified for selected course")
elif cluster>60 and cluster<=80:
    print("Above average")
elif cluster>80 and cluster<=100:
    print("Overqualified candidate")
else:
    print("Enter valid cluster")






