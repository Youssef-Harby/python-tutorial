# Taking the number of subjects and storing it in a variable.
subnum = int(input("Enter number of subjects :"))
idstuList = []
subList = []


def subgradeSTud():
    '''
    def subgradeSTud():
        for st in range(1, 6):
            subList = []
            for sub in range(1, subnum + 1):
    '''
    for st in range(1, 6):
        subList = []
        for sub in range(1, subnum + 1):
            #sub range user inputs for student range(5)
            grade = float(
                input("Student " + str(st) + " Grade Of Sub " + str(sub) + " is :"))
            # print("Grade " + str(grade))
            subList.append(grade)
            # print("append " + str(subList))
        idstuList.append(st)
        idstuList.append(subList)

subgradeSTud()
# print(idstuList)


def gradeListByID(iid=1):
    ind = idstuList.index(iid)
    return idstuList[ind + 1]  # Return Grade as List [50,60]

# Fun Average Grade By Student ID
def averGrad(sID):
    return sum(gradeListByID(sID)) / len(gradeListByID(sID))  # average grade *float 15.0

# Find the number of students whose grade is more than average

avGradeList = []
for sID in range(1, 6):
    avGradeList.append(averGrad(sID))
    sumGradeAverage = sum(avGradeList)/len(avGradeList)
    # print (sumGradeAverage)
    # print(avGradeList)

count = 0
for i in avGradeList:
    if i > sumGradeAverage:
        count = count +1
print("The Number of Students Whose Grade is More Than Average : " + str(count))

# Grade by ID 

while True:
    try:
        sID = int(input("Enter Student ID :"))
        if 50 > averGrad(sID) > 0:
            print('Fail')
        elif 50 >= averGrad(sID) < 65:
            print('Pass')
        elif 65 >= averGrad(sID) < 75:
            print('Good')
        elif 75 >= averGrad(sID) < 85:
            print('Very good')
        elif 85 <= averGrad(sID) <= 100:
            print('Excellent')
        else:
            print('Invalid Degree %')
    except:
        print("That's not a valid number!")
