grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
#Sort the grades in descending order and display the sorted list.
grades.sort()   
print(grades)
#Calculate the average grade and display it.
average_grade = len(grades)// 2  
print(average_grade)
#Replace any grade below 80 with the value Failed.
grades[0] = "Failed"    
grades[1] = "Failed"
grades[2] = "Failed"
print(grades)