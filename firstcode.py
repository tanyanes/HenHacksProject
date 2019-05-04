#curve predicting code

NameGradeDict=dict()
numStudents = input("How many students are in your class? ")
numStudents = int(numStudents)
NameList = []
QuizList = []
TestList = []
HWList = []
WeightList = []

counter=0
while counter < numStudents:
    key = input("Enter the name of your student: ")
    NameList.append(key)
    #This has to be typed in the format of [XX,XX,XX]
    value = input("Enter their quiz, test1, and HwAvg respectively: ")
    NameGradeDict[key]=value
    counter=counter+1
    print(NameGradeDict)
    print(NameList)

for name in NameList:
    QuizList.append(int(NameGradeDict[name][1:3]))
    TestList.append(int(NameGradeDict[name][4:6]))
    HWList.append(int(NameGradeDict[name][7:9]))

print(QuizList)
print(TestList)
print(HWList)

counter2=0
while counter2 < 3:
    weight = input("what is your weighting at  " + str(counter2) + "? ")
    WeightList.append(float(weight))
    counter2=counter2+1

i=0
QuizAvg = 0
while i < numStudents:
    QuizAvg+=QuizList[i]
    i=i+1
QuizAvg=QuizAvg/numStudents
print("Your Quiz Average is: " + str(QuizAvg))

j=0
TestAvg = 0
while j < numStudents:
    TestAvg+=TestList[j]
    j=j+1
TestAvg=TestAvg/numStudents
print("Your Test Average is: " + str(TestAvg))

k=0
HwAvg=0
while k < numStudents:
    HwAvg+=HWList[k]
    k=k+1
HwAvg=HwAvg/numStudents
print("Your Homework Average is: " + str(HwAvg))


wtQuiz=WeightList[0]*QuizAvg
wtTest=WeightList[1]*TestAvg
wtHW=WeightList[2]*HwAvg

print("Weighted Quiz Avg: " + str(wtQuiz))
print("Weighted Test Avg: " + str(wtTest))
print("Weighted HW Avg: " + str(wtHW))

total_score = wtQuiz + wtTest + wtHW
print("Your total grade for the class of students is currently: " + str(total_score))

finalGrade = input("what avg grade do you expect students to get on the final?: ")
print("Gathering data on weight changes after the final...")

WeightListAfter=[]
q=0
while q < 4:
    weight = input("what is your weighting at  " + str(counter2) + "? ")
    WeightListAfter.append(float(weight))
    q=q+1

wtQuiz2=WeightListAfter[0]*float(QuizAvg)
wtTest2=WeightListAfter[1]*float(TestAvg)
wtHW2=WeightListAfter[2]*float(HwAvg)
wtFinal2=WeightListAfter[3]*float(finalGrade)

final_score = wtQuiz2 + wtTest2 + wtHW2 + wtFinal2

#I made this the default for now since this is a prototype,
#I do not currently have a function to get each student's personal avg grade
stDev = 4

#Bottom cutoff for each grade based on statistics
A=final_score + 3*stDev
A_m= final_score + 2*stDev
B_p= final_score + stDev
B= final_score
B_m= final_score - stDev
C_p= final_score - 2*stDev
C= final_score - 3*stDev
C_m= final_score - 4*stDev
D_p= final_score - 5*stDev
D= final_score - 6*stDev
D_m= final_score - 7*stDev
F= final_score - 8*stDev

print("Your total grade for the class of students will be: " + str(final_score))
print("An A starts at: " + str(A))
print("A A- starts at: " + str(A_m))
print("A B+ starts at: " + str(B_p))
print("A B starts at: " + str(B))
print("A B- starts at: " + str(B_m))
print("A C+ starts at: " + str(C_p))
print("A C starts at: " + str(C))
print("A C- starts at: " + str(C_m))
print("A D+ starts at: " + str(D_p))
print("A D starts at: " + str(D))
print("A D- starts at: " + str(D_m))
print("An F starts at: " + str(F))



