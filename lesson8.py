import numpy as np
grades = [[5, 3, 3, 5, 4],[2, 2, 2, 3],[4, 5, 5, 2],[4, 4, 3],[5, 5, 5, 4, 5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
students_sorted = sorted(students)
average_grades = dict(zip(students_sorted,map(np.mean,grades)))
print(average_grades)
