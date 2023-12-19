# We're making the game 20 Questions, but for numbers instead of letters. 
# However, you receive points for the 
# accuracy of your guesses (ie using Binary Search in 10 questions
# gives you a lower score). Also, you receive points for brevity: the quicker you find the answer,
# the more points you can potentially receive.


import sys

from re import search
from random import randint, random, choice
from csv import DictWriter, DictReader



points = 0
target_found = False
point_dict = {">" : 1,
              "<" : 1,
              "=" : 10,
              "|" : 5,
              "^" : 20
              }

powers_of_2 = [1]
powers_of_3 = [1]
squares = [0]
cubes = [0]
x = 0
while powers_of_2[-1] <= 1000:
    powers_of_2.append(2 ** x)
    x += 1

while powers_of_3[-1] <= 1000:
    powers_of_3.append(3 ** x)
    x += 1

while squares[-1] <= 1000:
    squares.append(x ** 2)
    x += 1

while cubes[-1] <= 1000:
    cubes.append(x ** 3)
    x += 1

for l in [powers_of_2, powers_of_3, squares, cubes]:
    l.remove(l[-1])

# This function displays the intro screen.
def intro():
    global state
    print("""--------------------------------------------------------------------------\nHello! Welcome to 20 Questions: Numbers Edition.\n[0] Rules \n[1] You Guess \n""")
    while True:    
        response = input()
        if response.strip() == "0":
            state = "Rules"
            break
        elif response.strip() == "1":
            state = "PlayerGuess"
            break
        else:
            print("Please enter a valid response.")
        
# This function prints the Rules for the game
def rules():
    global state
    print("""--------------------------------------------------------------------------
        Objective: Earn as many points as possible.

        This game works like the game 20 Questions, but instead of 
        people/places, you have to guess a number from 1 to 1000. Here are some
        possible questions you can ask the computer, each with a certain number of points (to 
        discourage using binary search to find the answer in 10 questions). Points are awarded if the answer to
        the question you ask is true and you receive no points otherwise. To balance
        the game, there is a 1/16 chance that the number is a power of 2, a power of 3, 
        a square, or a cube.
        
        Questions (where n should be replaced with an int):
        Is # > n -- 1 pt.
        Is # < n -- 1 pt.
        Is n | # -- 5 pts.
        Is # = n -- 10 pts.
        Is # ^ n (ie. # is a perfect nth power) -- 20 pts. 
        Is n ^ # (ie. is # a power of n) -- 20 pts.
        After correctly guessing the number, any unused questions are worth 3 points each. 
        Have fun guessing!
                        - Chaaranath
    """)
    while True:
        response = input("[0] Play\n")
        if response.strip() == "0":
            state = "PlayerGuess"
            break
        else:
            print("Please enter a valid response.")

# Parses raw text and separates into computer-readable question
def parse(raw_text : str):
    question = search(r"((?:#|\d)+)\s*([><|=^])\s*((?:#|\d)+)", raw_text)
    if question:
        q_data = question.groups()
        return list(q_data)
    return

# Checks 
def check_inequality(q : list, t : int):
    global points
    for i in range(len(q)):
        if q[i] == "#":
            q[i] = t
    
    if q[1] == ">":
        return int(q[0]) > int(q[2])
    elif q[1] == "<":
        return int(q[0]) < int(q[2])

def check_equality(q :list , t : int):
    global target_found
    for i in range(len(q)):
        if q[i] == "#":
            q[i] = t
    
    if q[1] == "=":
        if int(q[0]) == int(q[2]):
            target_found = True
        
        return int(q[0]) == int(q[2]) 

def check_divisor(q : list, t : int): 
    for i in range(len(q)):
        if q[i] == "#":
            q[i] = t
    
    if q[1] == "|":
        return (float(q[2])/float(q[0])).is_integer() 

def check_power(q : list, t : int): 
    
    for i in range(len(q)):
        if q[i] == "#":
            q[i] = t
    
    if type(q[0]) == int:

        powers = [0]
        x = 1
        while powers[-1] <= 1000:
            powers.append(x ** int(q[2]))
            x += 1
        

        if q[1] == "^":
            return (int(q[0]) in powers)
    elif type(q[2]) == int:
        x = 1
        powers = [1]
        while powers[-1] <= 1000:
            powers.append(int(q[0]) ** x)
            x += 1
        
        if q[1] == "^":
            return (int(q[2]) in powers)

    
def pick_target():
    
    x = random()
    if x > 1/8:
        target = randint(1,1000)
    elif x > 1/16: 
        target = choice(choice(powers_of_2, powers_of_3, squares, cubes))
    
    return target

def save_score(name, score):
    print("""--------------------------------------------------------------------------""")
    print("Saving Score to database...")
    fieldnames = ["Name", "Score"]
    with open("scores.csv", "a") as scoredb:
        dw = DictWriter(scoredb, fieldnames=fieldnames)
        dw.writerow({"Name" : name, "Score": score})
        scoredb.flush()
        scoredb.close()
    
    print("Scores Saved!")

    with open("scores.csv", "r") as scoredb:
        dr = DictReader(scoredb, fieldnames=fieldnames)
        max_score = 0
        player_pr = 0
        max_score_name = ""
        for row in dr:
            if int(row["Score"]) >= max_score:
                max_score = int(row["Score"])
                max_score_name = row["Name"]
            if int(row["Score"]) >= player_pr and row["Name"] == name:
                player_pr = int(row["Score"])
            
        
        print()
        print(f"Max Score: {max_score} by {max_score_name}")
        print()
        print(f"Personal best for {name}: {player_pr}")

def player_guess():
    global points, state, target_found
    target_found = False
    points = 0
    print("""--------------------------------------------------------------------------""")
    name = input("Name: ").strip()

    print("Picking a number...")
    target = pick_target()
    
    
    print("Number picked!")
    questions = 0
    while questions < 20:
        try:
            q = parse(input(f"Question {questions+1}: "))
            if q == None:
                raise ValueError
            
            
         
            for e in [check_inequality(q, target), check_equality(q, target), check_divisor(q, target), check_power(q, target)]:
                if e != None:
                    response = e

            if response == None:
                raise ValueError
            else:
                if response:
                    points += point_dict[q[1]]
                    if target_found:
                        points += (20-questions)*3
                        print(f"You found it! The number was {target}")
                        print(f"Total points: {points}")
                        break
                    else:
                        print("Yes")
                        print(f"Points: {points}")

                else:
                    print("No")
                    print(f"Points: {points}")
                questions += 1

        except ValueError:
            print("Enter Valid Question")

    if questions == 20:
        print(f"Better luck next time! The number was {target}")
        points = 0
    
    save_score(name, points)

    print("""-------------------------------------------------------------------------- \n 
            Would you like to play again?""")
    print("[0] Play again \n[1] Rules \n[2] Quit")
    while True:    
        r = input()
        if r.strip() == "0":
            break
        elif r.strip() == "1":
            state = "Rules"
            break
        elif r.strip() == "2":
            sys.exit()
        else:
            print("Please enter a valid response.")


    

def main():
    while True:
        if state == "Intro":
            intro()
        elif state == "Rules":
            rules()
        elif state == "PlayerGuess":
            player_guess()
        else:
            sys.exit("Game Exited")
    

if __name__ == "__main__":
            main()
