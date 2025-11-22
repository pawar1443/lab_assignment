# List of marks obtained in subjects
marks = [85, 90, 78, 92, 88]

# Total marks for each subject (assuming 100)
total_per_subject = 100

# Calculate total marks obtained
total_obtained = sum(marks)

# Calculate total maximum marks
total_maximum = total_per_subject * len(marks)

# Calculate average marks
average_marks = total_obtained / len(marks)

# Calculate percentage
percentage = (total_obtained / total_maximum) * 100

print(f"Average Marks: {average_marks}")
print(f"Percentage: {percentage}%")
