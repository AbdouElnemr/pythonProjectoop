import Person


class Employee(Person):

    def __init__(self, id, car, email, salary, distanceToWork):
        self.id = id
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self):
        print(" I'am in Employee work ")

    def drive(self):
        print(" I'am in Employee drive ")

    def reFuel(self):
        print(" I'am in Employee reFuel ")

    def sendEmail(self):
        print(" I'am in Employee sendEmail ")


