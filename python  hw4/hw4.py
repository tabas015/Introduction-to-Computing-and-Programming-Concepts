#Name: Fahia Tabassum
# Problem A: find_password
#======================================================================
# Purpose:
# Given an encrypted file, tries every possible four letter lowercase
# password for that file until one works, and then returns the password.
# Input Parameter(s):
# filename is a string representing the name of the encrypted file.
# The file must be in the same folder as this script.
# Return Value:
# Returns the password that successfully decrypts the given file
#======================================================================

def find_password(filename):
    fp = open(filename)
    data = fp.read()

    #TODO: Try all possible four letter passwords, not just 'pwnd'
    for x0 in range(97,122):
        for x1 in range(97,122):
            for x2 in range(97,122):
                for x3 in range(97,122):
                    p = chr(x0)
                    q = chr(x1)
                    r = chr(x2)
                    s = chr(x3)
                    password = p+q+r+s
                    if decrypt(data,password):
                        return password



# Problem B: count_primes
#========================================================================================
# Purpose:
# Prints out all prime numbers between low and high, inclusve, and
# returns a count of how many there were.
# Input Parameter(s):
# low is a positive integer 
# high is a positive integer, which should be >= low
# Return Value:
# Returns the number of prime numbers between low and high, inclusive
#========================================================================================
def count_primes(low, high):
    if (low > high):
        return 0
    count = 0
    for i in range(low, high+1):
        if prime_number(i)==1:
            count = count + 1
            print (str(i) + " is prime")
    return count
#=========================================================================================
# Purpose:
# whether a single integer is prime
# Input Parameter(s):
# the integer value user puts
# Return Value:
# whether true or false on the result of 0 and 1
#==========================================================================================
def prime_number(n):
    if n==1:
        return 0
    sqrt_n = int (n**0.5)
    for i in range(2,sqrt_n+1):
        if (n%i)==0:
            return 0
    return 1


# Problem C: population
#=============================================================================================
# Purpose:
# Simulates the population of smallfish, middlefish, and bigfish over time
# Input Parameter(s):
# small is an integer, the initial number of smallfish in the lake
# middle is an integer, the initial number of middlefish in the lake
# big is an integer, the initial number of bigfish in the lake
# Return Value:
# Returns the number of weeks required for one of the populations to
# fall below 10, or 100 if the populations are all still >= 10 after
# 100 weeks
#============================================================================================
def population(small, middle, big):
    s = small
    m = middle
    b = big
    week = 0
    if ((int(s)<10)|(int(m)<10)|(int(b)<10)):
        return week
    
    while week <100 and int(s)>=10 and int(m)>=10 and int(b)>=10:
        ds = 0.1*s - 0.0002*s*m
        dm = -0.05*m + 0.0001*s*m - 0.00025*m*b
        db = -0.1*b + 0.0002*m*b
        s = s+ ds
        m =  m+ dm
        b =  b+ db
        print("week " + str(week+1) + " - " +"small: " + str(int(s))+" middle: " + str(int(m))+" big: " + str(int(b)))
        week += 1
    return week
            
      
        
#DO NOT EDIT ANYTHING BELOW THIS LINE
#Below are helper functions used for decrypting the text files.
#You don't have to understand how any of these work.

# decrypt
#==========================================
# Purpose:
# Check whether the password is correct for a given encrypted
# file, and print out the decrypted contents if it is.
# Input Parameter(s):
# data is a string, representing the contents of an encrypted file.
# password is a four letter lowercase string, representing the password
# used to encrypt/decrypt the file contents.
# Return Value:
# Returns True if the password is correct and the file contents
# were printed.  Returns False and prints nothing otherwise.
#=========================================================================
def decrypt(data, password):
    data = data.split('\n')
    if encode(password) == int(data[0]):
        print(vigenere(data[1],password))
        return True
    return False

# encode
#==========================================================================
# Purpose:
#   Turn a password into a ~9 digit number
# Input Parameter(s):
#   key is a four letter string representing a password
# Return Value:
#   Returns a number between 0 and 547120140, using modular exponentiation
#   to make it difficult to reverse engineer the password from the number.
#========================================================================
def encode(key):
    total = 0
    for ltr in key:
        total += ord(ltr)
        total *= 123
    return pow(total,2011,547120141)

# vigenere
#=====================================================================
# Purpose:
#   Decipher a message using the Vigenere cipher
# Input Parameter(s):
#   msg a string, representing the encrypted message
#   key is a four letter string, representing the cipher key
# Return Value:
#   Returns a string representing the deciphered text
#===================================================================
def vigenere(msg,key):
    i = 0
    out_msg = ''
    for ltr in msg:
        out_msg += chr((ord(ltr)-ord(key[i]))%28 +97)
        i = (i+1)%len(key)
    return out_msg.replace('{',' ').replace('|','.')


