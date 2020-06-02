# Name - Fahia Tabassum

# Problem A.  RPG Fight!

# Part 1
#==================================================================================================
# Purpose:
#   Creating a base named Adventurer class, which represents a jobless character template for all
#   of the job classes to build off of.
# Input Parameter(s):
#   Five arguments(name, level, strength, speed, power) where name is the name of the Adventurer and
#   should be a string. And (level, strength, speed, and power) should be integers that represent the
#   Adventurer’s ability levels.
# Return Value(s):
#    a jobless character template for all of the job classes to build off of.
#===================================================================================================

class Adventurer:
    def __init__(self, name, level, strength, speed, power):
        self.name = name
        self.level = level
        self.strength = strength
        self. speed = speed
        self.power = power
        self.hidden = False 
        self.HP = self.level*6

    def __repr__(self):
        return str(self.name) + ' - ' + 'HP: ' + str(self.HP)

#====================================================================================================
# Purpose:
# Finding out the damage the adventurer does if the target isn't hidden  
# Input Parameter(s):
#  another Adventurer object named target 
# Return Value(s):
#   none   
#====================================================================================================
       
    def attack(self,target):

        if target.hidden == True:
            print(str(self.name)+ " can't see "  + str(target.name))

        else:
            damage_amount = self.strength  + 4
            target.HP = target.HP - damage_amount
            print (str(self.name) + ' attacks ' + str(target.name) + ' for ' + str(damage_amount) + ' damage ')
            
    def __lt__(self,other):
        return self.HP < other.HP     


# Part-2 (Fighter)

class Fighter(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = self.level* 12

#====================================================================================================
# Purpose:
#   Finding out the damage the adventurer does if the target isn't hidden 
# Input Parameter(s):
#   another Adventurer object named target
# Return Value(s):
#  none 
#===================================================================================================
        

    def attack(self,target):
        if target.hidden == True:
            print(str(self.name)+ " can't see "  + str(target.name))

        else:
            damage_amount = (2*self.strength + 6)
            target.HP = target.HP - damage_amount
            
            print (str(self.name) +' attacks '+ str(target.name) +' for '+ str(damage_amount) +' damage ')
            
 
# Part 2 (Thief)
            
class Thief(Adventurer):
    
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self .HP = self.level * 8
        self.hidden = True
        
#===================================================================================================
# Purpose:
#   Finding out the damage the adventurer does if the target isn't hidden 
# Input Parameter(s):
#   another Adventurer object named target
# Return Value(s):
#   none
#===================================================================================================

    def attack(self,target):
        if self.hidden == False:
            Adventurer.attack(self,target)
            
        if self.hidden == True:
            if self.hidden == True and target.hidden == True and  self.speed < target.speed:
                print(str(self.name)+ " can't see "  + str(target.name))

            else:
                damage_amount = (self.speed  + self.level) * 5
                target.HP = target.HP - damage_amount
                target.hidden = False
                self.hidden = False
                print (str(self.name) + ' sneak attacks ' + str(target.name) + ' for ' + str(damage_amount) + ' damage ')
            

#Part 2 (Wizard)

class Wizard(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.fireballs_left = self.power
    
#================================================================================================
# Purpose:
#   Finding out the damage the adventurer does if the target isn't hidden 
# Input Parameter(s):
#   another Adventurer object target
# Return Value(s):
#   none
#===================================================================================================

    def attack(self,target):
        
        if self.fireballs_left == 0:
            Adventurer.attack(self,target)
        else:
            target.hidden = False
            damage_amount = self.level * 3
            target.HP = target.HP - damage_amount
            self.fireballs_left -= 1
            print(str(self.name) + ' casts fireball on ' + str(target.name) + ' for ' + str(damage_amount) + ' damage')




# Part 3
#======================================================================================================
# Purpose:
#  Creating a function (not part of any class) called duel which figures out which adventure object wins or loses
#  or both of them loses
# Input Parameter(s):
#  Two Adventurer objects adv1 and adv2 
# Return Value(s):
#   returns True if adv1 would win in a one-on- one fight, or False otherwise. 
#=========================================================================================================

def duel(adv1, adv2):
    Current_player = 'adv1'
    i = 0
    while adv1.HP > 0 and adv2.HP> 0:
        if Current_player == 'adv1':
            print(adv1)
            print(adv2)
            adv1.attack(adv2)
            if adv2.HP <=  0 and adv1.HP> 0:
                print(adv1)
                print(adv2)
                print(str(adv1.name) + ' wins! ')
                return True
            
            adv2.attack(adv1)
        i += 1

    if adv1.HP <=  0 and adv2.HP> 0:
        print(adv1)
        print(adv2)
        print(str(adv2.name) + ' wins! ')
        return False

    elif adv2.HP <=  0 and adv1.HP> 0:
        print(adv1)
        print(adv2)
        print(str(adv1.name) + ' wins! ')
        return True
    
    elif adv1.HP <=  0 and adv2.HP <= 0:
        print(adv1)
        print(adv2)
        print('Everyone loses! ')
        return False
    




# Problem B. The Ultimate Showdown

#=====================================================================================================
# Purpose:
#   implementing a tournament feature within the RPG with a scheme to keep the playing field as
#   balanced as possible despite widely varying ability levels: for each round, the
#   two Adventurers with the highest remaining HP will be forced to fight each other until one of them is eliminated.
# Input Parameter(s):
#   a single parameter(adv_list) which is a list of Adventurer objects 
# Return Value(s):
#   a single winner or none
#====================================================================================================
def tournament(adv_list):

    if len(adv_list) == 0:
        return None

    elif len(adv_list) == 1:
        return adv_list[0]

    else:
        adv_list.sort()
        highest_HP = adv_list[-1]
        second_highest_HP = adv_list[-2]
        a = duel(second_highest_HP,highest_HP)


        for i in range(len(adv_list)):
            if adv_list[i].HP < 1:
                del adv_list[i]
                return tournament(adv_list)
        
        
        
        
        
        
    
    
