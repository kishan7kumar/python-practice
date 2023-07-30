class Employee:
    # declaring constructor and self is the reference for which the method inside the class is called
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # get salary method
    def getSalary(self):
        return self.salary


employee1 = Employee("Roman", "23232")
print(employee1.name)
print(employee1.getSalary())
