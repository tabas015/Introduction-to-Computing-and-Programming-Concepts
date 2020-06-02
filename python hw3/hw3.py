#Name: Fahia Tabassum

# Problem A: Bark Scale
#==========================================================================================================================
# Purpose:
# Printing out string for dog's different weight values
# Input parameter(s):
# Weight = Tqhe weight of the dog
# Return value:
# Returns a string representing what the dog's bark would sound like based on a scale
#==========================================================================================================================

def sound(weight):
    x = weight
    if x<13:
        return ("'Yip'")
    elif 13<=x<=30:
        return ("'Ruff'")
    elif 31<=x<=70:
        return ("'Bark'")
    elif x>70:
        return ("'Boof'")

# Problem B: Text Adventure Choice
#===========================================================================================================================
# Purpose:
# Making choices by using text commands
# Input parameter(s):
# Text = A string representing the prompt for a choice in a text adventure game
# Option1 = a string representing possible option 1
# Option2 = a string representing possible option 2
# Option3 = a string representing possible option 3
# Return value:
# Returns the choices user made  
#===========================================================================================================================
def choice(text,option1,option2,option3):
    print(text)
    print("1.",option1)
    print("2.",option2)
    print("3.",option3)
    n = input("choose 1, 2 or 3:")
    while n != "1" and n != "2" and n != "3":
        print ("invalid option")
        n = input("choose 1, 2 or 3:")
    return n
        
# Problem C: Text Adventure Game
#===========================================================================================================================
# Purpose:
# Developing text-based adventure game
# Input parameter(s):
# no parameter
# Return value:
# Returns the bollean value 
#=============================================================================================================================

def adventure():
    n = choice("You have entered level 3", "You want to continue?", "Enter the cave alone?", "Enter the cave after making a team")
    if n == "1":
        print ("Can not continue without saving level 2")
        return False

    elif n == "2":
        n = choice("There is a dragon in the entrance of the cave", "light up to see in the dark of cave", "check your weapons to fight against the dragon", "Prepare yourself to fight")
        if n == "1":
            print ("Lighting up can easily make the dragon sense your presence in cave")
            return True
        elif n == "2" or "3":
            n = choice("Fight against the dragon" , "Shoot with gun", "Throw Fireballs", "Feast Fight")
            if n == "1":
                print ("Shooting will make the dragon angry")
                return True
            elif n == "2":
                n = choice("Rescue your territory" , "Hide","Fight untill you get dragon's territory", "Save your territory")
                if n == "1":
                    print (" Hide from the dragon until it leaves")
                    return True
                elif n == "2":
                    print(" May lead you to death")
                    return False
                else:
                    print (" Hide from the dragon until it leaves")
                    return True
            else:
                print("feast fight will kill you")
                return False   
        
    else:
        n = choice("Team up as a group", "Leave the team", "Make a plan to fight together ", "Lead the team")
        if n == "1":
            print ("Can not leave now")
            return False
        elif n == "2":
            n = choice("Fight against the dragon" , "Shoot with gun", "Throw Fireballs", "Feast Fight")
            if n == "1":
                print ("Shooting will make the dragon angry")
                return True
            elif n == "2":
                n =choice("Rescue your territory" , "Hide","Fight untill you get dragon's territory", "Save your territory")
                if n == "1":
                    print (" Hide from the dragon until it leaves")
                    return True
                elif n == "2":
                    print(" May lead you to death")
                    return False
                else:
                    print (" Hide from the dragon until it leaves")
                    return True
            else:
                print("feast fight will kill you")
                return False   
            
        else:
            n =choice("Rescue your territory" , "Hide","Fight untill you get dragon's territory", "Save your territory")
            if n == "1":
                print (" Hide from the dragon until it leaves")
                return True
            elif n == "2":
                 print(" May lead you to death")
                 return False
            else:
                print (" Hide from the dragon until it leaves")
                return True
                
#=============================================================================================================== =====           
     
    
       
    
