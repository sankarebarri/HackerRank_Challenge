class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, firstName, lastName, idNumber, testScores=None):
        super().__init__(firstName, lastName, idNumber)
        if testScores is None:
            self.testScores = []
        else:
            self.testScores = testScores

    def calculate(self):
        average_score = sum(self.testScores)/len(self.testScores)
        if average_score >= 90:
            return "O"
        elif average_score >= 80:
            return "E"
        elif average_score >= 70:
            return "A"
        elif average_score >= 55:
            return "P"
        elif average_score >= 40:
            return "D"
        else:
            return "T"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
