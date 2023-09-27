class Student:

  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # sort the list of student in descending order of CGPA
   sorted_student = sorted(student_list, 
 key=lambda Student:Student.cgpa,
 reverse=True)
   return sorted_student


# Example usage:
student = [ 
  Student("Hari", "A123", 7.8),
  Student("Srikanth", "A124", 8.9),
  Student("sowmiya", "A125", 9.1),
  Staudent("Abinaya", "A126", 9.9),
]

sorted_students = sort_students(student)

# Print the sorted list of student
for student in sorted_students:
 print("Name: {},Roll Number: {},CGPA: {}".format(student.name,student.roll_number,student.cgpa))
