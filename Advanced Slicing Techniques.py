temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
#Extract the temperatures for the second week (7 days) of the month. Expected Outcome:
second_week = temperatures[7:14]
print(second_week)
#Extract all the temperatures above 100.
above_100 = temperatures[24:]
print(above_100)
#Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
temperatures.reverse()
print(temperatures)
segment = temperatures[5:10]
print(segment)