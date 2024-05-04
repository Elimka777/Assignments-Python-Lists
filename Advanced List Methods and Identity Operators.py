submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
#Find out which students both submitted their assignments and attended the class.
both_submitted_and_attended = [student for student in submitted if student in attended]
print("Students who both submitted assignments and attended class:", both_submitted_and_attended)
#Check if the two lists are identical in terms of their content, regardless of order.
print(submitted is attended)
#Using list methods, remove any student from the attended list who did not submit their assignment.
not_submitted = [student for student in attended if student not in submitted]
print("Attended list after removing students who didn't submit their assignment:", not_submitted)