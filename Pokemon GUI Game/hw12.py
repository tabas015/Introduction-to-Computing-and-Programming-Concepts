
# Name - Fahia Tabassum 
import tkinter as tk
import random


class Pokemon:
    def __init__(self,line):
        li = line.split(',')
        self.dex_number = li[0]
        self.species_name = li[1]   
        self.catch_rate = int(li[2])
        self.speed = int(li[3])
        
    def __str__(self):
        return str(self.species_name)
         
    
class SafariSimulator(tk.Frame):
    def __init__(self, master=None):
        fp = open('pokedex.csv')
        li = fp.readlines()
        fp.close()

        self.data = []
        for i in range(1, len(li)):    
            values = li[i].strip()
            self.data.append(Pokemon(values))
            i += 1

        self.caught_pokemon = 0
        self.caught = []
        self.current_pokemon = self.data[0]
        self.balls_left = 30 

        tk.Frame.__init__(self, master)
        master.minsize(width=275, height=350)
        master.maxsize(width=275, height=350)
        master.title("Safari Zone Simulator")
        self.pack()
        self.createWidgets()

        self.nextPokemon()       
        
    def createWidgets(self):
        
        self.throwbutton = tk.Button(self)      
        self.throwbutton["text"] = "Throw Safari Ball(30 left)"
        self.throwbutton["command"] = self.throwBall
        self.throwbutton.pack()

        
        self.runButton = tk.Button(self)        
        self.runButton["text"] = "Run Away"
        self.runButton["command"] = self.nextPokemon
        self.runButton.pack()
        
        self.messageLabel = tk.Label(bg="pink")  
        self.messageLabel.pack(fill="x", padx=5, pady=5)

        self.PokemonImageLabel = tk.Label(bg="white") 
        self.PokemonImageLabel.pack(fill="x", padx=5, pady=5)

        self.catchProbLabel = tk.Label(bg ="pink") 
        self.catchProbLabel.pack(fill="x", padx=5, pady=10)
        

    def nextPokemon(self):
        dex_number = random.randint(1,151)
        self.current_pokemon = self.data[dex_number -1]
        self.messageLabel["text"] = "You encounter a wild" + str(self.current_pokemon)
        self.photo = tk.PhotoImage(file = "sprites/" + str(self.current_pokemon.dex_number) + ".gif")
        self.PokemonImageLabel["image"] = self.photo
        chance = (min(self.current_pokemon.catch_rate+ 1,151)/449.5)*100
        self.catchProbLabel["text"] = "Your chance of catching it is " + str(round(chance))+ "%!"

        
        
        
    def endAdventure(self):
        self.messageLabel['text']="You're all out of balls, hope you had fun!"
        self.PokemonImageLabel.pack_forget()
        self.throwbutton.pack_forget()
        self.runButton.pack_forget()
        self.catchProbLabel['text'] = 'You caught ' + str(self.caught_pokemon) + ' Pokemon:'
        for pok in self.caught:
            self.catchProbLabel['text'] += '\n' + str(pok)

        

    def throwBall(self):
        self.balls_left -= 1
        if self.balls_left >= 0:
            self.throwbutton["text"] = "Throw Safari Ball (" + str(self.balls_left) + ' left)'
            chance = (min(self.current_pokemon.catch_rate+ 1,151)/449.5)
            if random.random()<chance:
                self.caught_pokemon += 1
                
                self.nextPokemon()
                self.caught.append(self.current_pokemon)
                print (self.caught_pokemon)
            else:
                self.messageLabel['text']='Aargh! It escaped'

        if self.balls_left == 0:
            self.endAdventure()
        
        
       
app = SafariSimulator(tk.Tk())
app.mainloop()
