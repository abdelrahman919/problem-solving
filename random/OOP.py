class Employee:

    def __init__(self,name,age,salary): 
        self.name = name 
        self.age = age 
        self.salary = salary

    def work(self):
        print(f"he is working")


class SoftwareEngineer(Employee):
    def __init__(self,name,age,salary):
        super().__init__(name,age,salary)
    def work(self):
        print(f"{self.name} is programming gamed gdn")


class Designer(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
    def work(self):
        print(f"{self.name} is designing gamed gdn")

se1= SoftwareEngineer('hmada',26,10)
d1 = Designer('btts',25,70)


se1.work()
d1.work()
        
    