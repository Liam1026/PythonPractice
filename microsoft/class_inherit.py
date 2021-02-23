class Person():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('Hello, ' + self.name)


class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def sing_school_song(self):
        print('Sing the song of ' + self.school)

    def say_hello(self):
        super().say_hello()
        print('Tired at school.')

    def __str__(self):
        return f'{self.name} attends {self.school}'


student = Student('Madoka', 'Shu')
student.say_hello()
student.sing_school_song()

print(isinstance(student, Student))
print(isinstance(student, Person))
print(issubclass(Student, Person))

print(f'Is this a student? {isinstance(student, Student)}')
print(f'Is this a person? {isinstance(student, Person)}')
print(f'Is student a person? {issubclass(Student, Person)}')
print(student)
