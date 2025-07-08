import numpy as np
#students grade in [math , physics , history , chemistry , geography] for each student in order : [lilli , ella , emma , mia , nina]

students=np.array([["lilli"],["ella"],["emma"],["mia"],["nina"]])
print("the list of students :\n\n",students,"\n\n")

courses=np.array([["math"],["physics"],["history"],["chemistry"],["geography"]])
print("the list of courses :\n\n",courses,"\n\n")

students_grade = np.array([[19,18,13,16,11],[10,12,20,12,19.5],[5,16,9,14,18.5],[20,14,13,16,11],[12,12,8,5,16]])
print(" grades :\n\n",students_grade,"\n\n")

student_average = np.mean(students_grade,axis=1) # average for each student 
print("list of average for each student :" ,student_average)

i=0
while(i<5):
           print("grade of ",students[i],"is ",students_grade[i], "and average score for" ,students[i],"is",student_average[i])
           i+=1 

print("\n\n")
courses_average=np.mean(students_grade,axis=0) #average for each course
print("list of average for each course : ",courses_average)
a=0
while(a<5):
        print("average for ",courses[a] ,"is :", courses_average[a])
        a+=1
        
print("\n\n")
print("for the math course the minmum, maximum, median, variance, standard deviation equal with :")
min_grade=np.min(students_grade[:,0])
print("minimum grade is ",min_grade)

max_grade = np.max(students_grade[:,0])
print("maximum grade is",max_grade)

print("the median of the scores is",np.median(students_grade[:,0]))
print("the variance of the scores is",np.var(students_grade[:,0]))
print("the standard deviation of the scores is",np.std(students_grade[:,0]))
