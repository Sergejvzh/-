grades = [[5, 3, 3, 5, 4],[2, 2, 2, 3],[4, 5, 5, 2],[4, 4, 3],[5, 5, 5, 4, 5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
students = sorted(students)
print(students)
average_grades = {'Aaron': [5, 3, 3, 5, 4],'Bilbo': [2, 2, 2, 3],'Johnny': [4, 5, 5, 2]
                  ,'Khendrik': [4, 4, 3],'Steve': [5, 5, 5, 4, 5]}
print(average_grades)
sredny0 = sum(list(grades[0])) / len(grades[0])
print(students[0],sredny0)
sredny1 = sum(list(grades[1])) / len(grades[1])
print(students[1],sredny1)
sredny2 = sum(list(grades[2])) / len(grades[2])
print(students[2],sredny2)
sredny3 = sum(list(grades[3])) / len(grades[3])
print(students[3],sredny3)
sredny4 = sum(list(grades[4])) / len(grades[4])
print(students[4],sredny4)