from abc import ABC, abstractmethod

class Employer(ABC):
    def salary(self):
        pass

class Hello(Employer):
    def salary(self):
        return 50000

class Hello1(Employer):
    def salary(self):
        return 60000
    
class Hello2(Employer):
    def salary(self):
        return 70000
    
obj=Hello2()
print(obj.salary())

obj=Hello1()
print(obj.salary())

obj=Hello()
print(obj.salary())