# Define the Person class
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        return f"ID: {self.id}, Name: {self.name}"

# Define the Manager class inheriting from Person
class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        return f"ID: {self.id}, Name: {self.name}, Title: {self.title}"

# Define the Employee class inheriting from Person
class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        return f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}"

# Test cases
if __name__ == "__main__":
    # Test Person class
    p1 = Person(1, "Alice")
    p2 = Person(2, "Bob")
    print(p1.printInfo())  # Expected: ID: 1, Name: Alice
    print(p2.printInfo())  # Expected: ID: 2, Name: Bob

    # Test Manager class
    m1 = Manager(3, "Charlie", "Team Lead")
    m2 = Manager(4, "Diana", "Project Manager")
    print(m1.printInfo())  # Expected: ID: 3, Name: Charlie, Title: Team Lead
    print(m2.printInfo())  # Expected: ID: 4, Name: Diana, Title: Project Manager

    # Test Employee class
    e1 = Employee(5, "Eve", "Python")
    e2 = Employee(6, "Frank", "Java")
    print(e1.printInfo())  # Expected: ID: 5, Name: Eve, Skill: Python
    print(e2.printInfo())  # Expected: ID: 6, Name: Frank, Skill: Java

    # Additional tests
    m3 = Manager(7, "Grace", "HR Manager")
    e3 = Employee(8, "Hank", "C++")
    print(m3.printInfo())  # Expected: ID: 7, Name: Grace, Title: HR Manager
    print(e3.printInfo())  # Expected: ID: 8, Name: Hank, Skill: C++

    p3 = Person(9, "Ivy")
    print(p3.printInfo())  # Expected: ID: 9, Name: Ivy