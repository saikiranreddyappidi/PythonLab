from statistics import mean, stdev

import numpy, pandas

arr = numpy.random.randint(15, 25, (3, 4))
results = [[], [], [], []]
for i in arr:
	results[0].append(min(i))
	results[1].append(max(i))
	results[2].append(mean(i))
	results[3].append(stdev(i))
# print(results)
student_individual = arr.transpose()
student_total = []
for i in student_individual:
	student_total.append(sum(i))
# print(student_total)
stud = ["student1", "student2", "student3", "student4"]
df = pandas.DataFrame({"Student Name": stud, "Exam1": arr[0], "Exam2": arr[1], "Exam3": arr[2], "Sum": student_total})
print(df)
Exam = ["Exam1", "Exam2", "Exam3"]
result_df = pandas.DataFrame({"Exam": Exam,
                              "Minimum": results[0],
                              "Maximum": results[1],
                              "Average": results[2],
                              "Standard Deviation": results[3]
                              })
print(result_df)
