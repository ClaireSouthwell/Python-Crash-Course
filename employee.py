class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount
        print(f"Your new salary is ${self.salary}. ")


'''brad = Employee('Brad', 'Pitt', 5000000)

brad.give_raise()
brad.give_raise(1000000)'''
