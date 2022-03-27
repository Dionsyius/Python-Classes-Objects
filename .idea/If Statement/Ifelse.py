School = input("Enter Your School : ")
print("                       " + School)
name = input("Enter Student Name : ")
print(" " + name)
ID = input("Enter Student ID : ")
print (" " + ID)
Dept = input("Student Department : ")
print(" " + Dept)


def testAvg(test_list):
    total = 0
    for x in test_list:
        total +=x
    average = total/len(test_list)
    return average



def letterGrade(test_average):
    average = 'F'
    if test_average >=90:
        average = 'A'
    elif test_average >= 80:
        average = 'B'
    elif test_average >= 70:
       average = 'C'
    elif test_average >= 60:
     average = 'D'

    return average
test_list = []
while(True):
    scores = input('Enter The Students Test Grades and say "STOP" to find the grade : ')
    if scores == "STOP":
       break
    test_list.append(float(scores))
test_average = testAvg(test_list)
letter_grade = letterGrade(test_average)


print("The School is : " + School)
print("The Name is : " + name)
print ("The Student ID is : " + ID)
print("The Department is : " + Dept)
print("The Student final Grade is "+ str(test_average) + '  and received an  ' + str (letter_grade) + ' in this course')






