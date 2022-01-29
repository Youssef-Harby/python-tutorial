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
            print("Grade " + str(grade))
            subList.append(grade)
            print("append " + str(subList))
        idstuList.append(st)
        idstuList.append(subList)

subgradeSTud()
print(idstuList)


def dataByID(iid=1):
    ind = idstuList.index(iid)
    return idstuList[ind + 1]  # Return Grade as List [50,60]


def averGrad():
    return sum(dataByID(sID)) / len(dataByID(sID))  # average grade *float 15.0


while True:
    try:
        sID = int(input("Enter Student ID :"))
        if 50 > averGrad() > 0:
            print('Fail')
        elif 50 >= averGrad() < 65:
            print('Pass')
        elif 65 >= averGrad() < 75:
            print('Good')
        elif 75 >= averGrad() < 85:
            print('Very good')
        elif 85 <= averGrad() <= 100:
            print('Excellent')
        else:
            print('Invalid Degree %')
    except:
        print("That's not a valid number!")

# Find the number of students whose grade is more than average

# def stuData():
#     # for studentID in range(0,len(idstuList),2):
#         # print (idstuList[studentID])

#     for studentGrade in range(1,len(idstuList),2):
#         print (idstuList[studentGrade])
        
# stuData()
