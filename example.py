class Human:
    head =1
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'name is {self.name}\n'\
               f'age is {self.age}'
    def run(self):
        print(f'{self.run} is running')
hum = Human('Sadir', 36)
print(hum)
hum.run()


class Student(Human):
    pass
student=Student('Daniel', 60)
print(student)



