students_scores = {
	"Alice": [85,90,92],
	"Bob": [78,80,85],
	"Charlie": [92,88,95]}

student_grades = [students_scores["Alice"], students_scores["Bob"], students_scores["Charlie"]]

for student, grades in students_scores.items():
	print(student)
	for grade in grades:
		print(f'{grade}')
