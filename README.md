# 20 Questions: Number Edition
#### Video Demo:  <https://youtu.be/m_YRIZsbaXE>
#### Description:
This game works like the game 20 Questions, but instead of 
people/places, you have to guess a number from 1 to 1000. When prompted, you have the opportunity to ask the computer a question regarding the number (eg. Is # > 500, Does 2 | #, etc.). To discourage the use of a binary search-type strategy, each question is a ssociated with a certain number of points, which are awarded if the answer to the question is "Yes". Here are some examples of questions you can ask (where n should be replaced with an int):

Questions (where n should be replaced with an int):
+ Is # > n -- 1 pt.
+ Is # < n -- 1 pt.
+ Is n | # -- 5 pts.
+ Is # = n -- 10 pts.
+ Is # ^ n (ie. # is a perfect nth power) -- 20 pts. 
+ Is n ^ # (ie. is # a power of n) -- 20 pts.


After correctly guessing the number, any unused questions are worth 3 points each. To balance the game, there is a 1/16 chance the randomly generated number is a square, cube, power of 2, or power of 3.

There are many states in this game, each of which is displayed to the user through screens. The Start Screen is prompted when you first run the game and can take you to either the Rules Screen or the Game Screen. 

```
--------------------------------------------------------------------------
Hello! Welcome to 20 Questions: Numbers Edition.
[0] Rules 
[1] You Guess 

```
+ The Start Screen

The Rules Screen displays the rules for the game:

```
--------------------------------------------------------------------------
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

```

The Game Screen displays the game. When the Game Screen is called, the user is first prompted for their name, which will later be saved to a database along with their score. Then, a random number is generated using the `pick_target` function and the `random` library. The user is prompted for an input, where they can provide the question that will then be parsed by the `parse` function using RegEx and the `re` library. The parsed string then goes through helper functions `check_inequality`, `check_equality`, `check_divisor`, and `check_power` depending on the value of the operator. These helper functions return a boolean, which causes "Yes" to be printed if the return is `True` and "No" if `False`. Points are then awarded accordingly. After correctly guessing the number, the score of the user is saved along with their name to a csv file using the `csv` module's `DictReader` and `DictWriter` capabilities. THe user can then see their personal best score and the overall high score. Finally, the user is prompted with the option to either play again, see the rules again, or quit. In addition to the main code, I also wrote test cases which check the functionality of the parser function and the evaluator functions.

Most of the helper methods/variables relating to the game are stored in the class `State`.

This project took two weeks to fully complete. I got to the final stage of this course a few weeks before school started, so I didn't get an opportunity to submit a more complex project as I would have wanted.

This CS50 Python course has been so much fun from start to end, and I feel like I've grown a lot as a programmer from attending. In the future, I plan on tackling more challenging and intensive projects to build my coding skills and experience in coding. Thank you!

-- Chaaranath