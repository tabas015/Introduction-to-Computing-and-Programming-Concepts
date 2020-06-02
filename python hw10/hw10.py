
# Name- Fahia Tabassum

# Problem A.Complex Class
# ==========================================================================
# Purpose:
#    Creating a class named Complex that models a complex number, numbers of the form x+yi,
#    where x and y are real numbers, and i is the imaginary unit equal to the square root of -1.
# Input Parameter(s):
#   Two instance variables (real and imag) where real represents the real number and
#   imag represents the imaginary number 
# Return Value(s):
#  returns the complex number in a + bi form where a and b are real numbers and i is the imaginary unit
#============================================================================

class Complex:
    def __init__(self, real, imag):
        self.real= real
        self.imag= imag

    def get_real(self):
        return self.real

    def get_imag(self):
        return self.imag

    def set_real (self, new_real):
        self.real = new_real

    def set_imag(self, new_imag):
        self.imag = new_imag

    def  __str__(self):
        return str(self.real) + ' + ' + str(self.imag) + 'i'

    def __add__(self, other):
        return Complex(self.real +other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - (self.imag * other.imag), self.real*other.imag + self.imag*other.real)
        
    def __eq__(self,other):
        return self.real == other.real and self.imag == other.imag



# Problem B.  Employee Database
# Part 1
#===========================================================================
# Purpose:
#   Creating a class named  Employee
# Input Parameter(s):
#   name -  is a string representing the employee’s first name 
#   position - is a string representing the employee’s job title (the second column)
#   salary - is a floating point number representing the employee’s annual salary in USD (the third column).
#   seniority- is a floating point number representing the number of years the employee has worked at that
#              branch of the company (the fourth column).
#   value - is a floating point number representing an estimate of the average annual earnings that the
#           employee generates for the company.(he fifth column))

# Return Value(s):
#   the class named Employee with all its processed information
#============================================================================

class Employee:
    def __init__(self,line):
        li = line.split(',')
        self.name = li[0]
        self.position = li[1]
        self.salary =  li[2]
        self. seniority = li[3]
        self.value = li[4]
    def __str__(self):
        return str(self.name) + ', ' + str(self.position)
        
    def net_value(self):
        return float(self.value) - float(self.salary)
    
    def __lt__(self,other):
        return self.net_value() < other.net_value()



# part 2
#===========================================================================
# Purpose:
#   Creating a class named Branch
# Input Parameter(s):
#   location - is a string, representing the city in which the branch is located
#   upkeep - is a float, representing the annual upkeep cost of the building
#   team -  is a list of Employee objects, representing every employee working at the branch.
# Return Value(s):
#  the class named Branch with all its processed informations
#============================================================================

class Branch:
    def __init__(self,fname):
        fp = open (fname)
        values = fp.readlines()
        self.location = values[0].split(',')[1].strip()
        self.upkeep =float( values[1].split(',')[1].strip())
        team_list = values[3:]
        
        self.team = []
        for line in team_list:
            self.team .append(Employee(line))

    def __str__(self):
        output = self.location 
        for emp in self.team:
            output += '\n' +str(emp)
        return output
        
        
    def profit(self):
        total = 0
        for ls in self.team:
            total += ls.net_value()
        return total - self.upkeep

    def __lt__(self,other):
        return self.profit() < other.profit()
        
    def cut(self, num):
        self.team.sort()
        self.team = self.team[num:]
        


# Part 3
#===========================================================================
# Purpose:
# Creating a class named Company
# Input Parameter(s):
#  name - is a string, representing the name of the company
# branches - is a list of Branch objects, representing all of the branches associated with the company
# Return Value(s):
#   the class named Company with all its processed informations
#============================================================================

class Company:
    def __init__(self,name,branches):
        self.branches = branches
        self.name = name
        
    def __str__ (self):
        new = self.name
        for name in self.branches:
            new += '\n'+ '\n' + str(name)
        return new

    def synergize(self):
        self.branches.sort()
        first = self.branches[0]
        half = len (first.team)// 2
        first.cut(half)
        
        


