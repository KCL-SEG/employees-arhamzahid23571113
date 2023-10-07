"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

class Salary_Contract(Employee):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary
    def get_pay(self):
            return self.salary

    def __str__(self):
            return (f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.salary}.")
class Hourly_Contract(Employee):
    def __init__(self,name,hours,rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate
    def get_pay(self):
            return self.hours*self.rate
    def __str__(self):
            return (f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour. Their total pay is {self.hours*self.rate}.")
class Salary_Bonus_Commission(Salary_Contract):
    def __init__(self, name, salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus

    def get_pay(self):
            return self.bonus+self.salary

    def __str__(self):
            return (f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}.  Their total pay is {self.bonus+self.salary}.")

class Hourly_Bonus_Commission(Hourly_Contract):
    def __init__(self, name, hours, rate,bonus):
        super().__init__(name,hours,rate)
        self.bonus = bonus
    def get_pay(self):
            return (self.hours*self.rate)+self.bonus

    def __str__(self):
            return (f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a bonus commission of {self.bonus}. Their total pay is {(self.hours*self.rate)+self.bonus}.")
class Salary_Contract_Commission(Salary_Contract):
    def __init__(self,name,salary,contracts,contract_rate):
        super().__init__(name,salary)
        self.contracts = contracts
        self.contract_rate = contract_rate

    def get_pay(self):
            return self.salary + (self.contracts*self.contract_rate)

    def __str__(self):
            return (f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.contract_rate}/contract. Their total pay is {self.salary + (self.contracts*self.contract_rate)}.")
class Hourly_Contract_Commission(Hourly_Contract):
    def __init__(self, name, hours, rate,contracts, contract_rate):
        super().__init__(name,hours,rate)
        self.contracts = contracts
        self.contract_rate = contract_rate
    def get_pay(self):
            return (self.hours*self.rate)+(self.contracts*self.contract_rate)

    def __str__(self):
            return (f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a commission for {self.contracts} contract(s) at {self.contract_rate}/contract. Their total pay is {(self.hours*self.rate)+(self.contracts*self.contract_rate)}.")





# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salary_Contract('Billie',4000)
print(billie.get_pay())
print(billie.__str__())
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly_Contract('Charlie',100,25)
print(charlie.get_pay())
print(charlie.__str__())
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Salary_Contract_Commission('Renee',3000,4,200)
print(renee.get_pay())
renee.__str__()
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hourly_Contract_Commission('Jan',150,25,3,220)
print(jan.get_pay())
print(jan.__str__())
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Salary_Bonus_Commission('Robbie',2000,1500)
print(robbie.get_pay())
print(robbie.__str__())
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hourly_Bonus_Commission('Ariel',120,30,600)
print(ariel.get_pay())
print(ariel.__str__())