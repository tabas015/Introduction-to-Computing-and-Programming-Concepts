# Name: Fahia Tabassum


#Problem A: ​Relativistic Length Contraction 
#================================================================
# Purpose:
# Finding the contracted distance between two objects 
# Input Parameter(s):
# Distance: The original distance between two objects
# Speed: the speed at which we are travelling relative to the two object
# Return Value(s):
# the distance between two objects from our reference frame
#=================================================================
def length_contract(dist, speed):
    L0 = dist
    S = speed
    v = 3*10**8
    return L0*(1-(S**2/v**2))**0.5




# Problem B:The Bessel Run
#=================================================================
# Purpose:
# Figuring out the time required to traverse the segment
# Input Parameter(s):
# speed: bessel's average speed in the run
# Return Value(s):
# the time required to traverse the segment, seen by Bessel, in years
#===================================================================
def bessel_run(speed):
    x = 12*3.086*10**16
    y = x/speed
    print (y/31557600)
    return (length_contract(x,speed)/speed)/31557600




# Problem C: Who needs loops?
#===================================================================
# Purpose:
# Printing "Who needs loop?" for 5 times
# Input Parameter(s):
# No parameter
# Return value(s):
# no return value
#============================================
def print_5():
    print("Who needs loop?")
    print("Who needs loop?")
    print("Who needs loop?")
    print("Who needs loop?")
    print("Who needs loop?")

#===========================================
# Purpose:
# Printing "Who needs loop?" for 10 times by calling the function print_5() for 2 times
# Input Parameter(s):
# No parameter
# Return value(s):
# no return value
#=============================================
def print_10():
    print_5()
    print_5()

#=============================================
# Purpose:
# Printing "Who needs loop?" for 20 times by calling the function print_10() for 2 times
# Input Parameter(s):
# No parameter
# Return value(s):
# no return value
#=============================================

def print_20():
    print_10()
    print_10()

#=============================================
# Purpose:
# Printing "Who needs loop?" for 100 times by calling the function print_20() for 5 times
# Input Parameter(s):
# No parameter
# Return value(s):
# no return value
#=============================================  
def print_100():
    print_20()
    print_20()
    print_20()
    print_20()
    print_20()
    
    
