class Employee:
    te=0
    def __init__(self,name):
        self.name=name
        Employee.increment()

    @classmethod
    def increment(cls):
        cls.te+=1

e1=Employee('vedant')
e2=Employee('parth')
e3=Employee('ajay')
print(f"total number of employees are {Employee.te}")


