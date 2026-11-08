name=input("Enter student name:")

math= int(input("Enter Math marks: "))

english=int(input("Enter English marks: "))

pyhton=int(input("Enter Pyhton marks: "))

avg=(math+english+pyhton)/3

    
print("Student Name: ",name)
print("Average Marks: ",avg)


if 80<=avg<=100:
    print("Final Grade: A+")
elif 70<=avg<80:
    print("Final Grade: A")
elif 60<=avg<70:
    print("Final Grade: A-")
elif 50 <=avg<60:
    print("Final Grade: B")
elif 40 <=avg<50:
    print("Final Grade: C")
elif 0<=avg<40:
    print("Final Grade: F")