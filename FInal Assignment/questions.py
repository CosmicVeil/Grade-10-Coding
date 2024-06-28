# Function module of all global variables


curr_question = 0
curr_quest = 0
num_incorrect = 0
time_left = 600*1000
gold = 0
books_of_knowledge = 0

option_selected = "option 1"

challenge_text = ["""You are stuck in a cell. 
                  There is only one way out, a doorway with a hard stuck lock. 
                  You notice that the lock has only two numbers to type in 1 or 0. 
                  As you head over, Loki tells you about a conversation he overheard from the guards. 
                  He said they mentioned that the password to our cell was 8. 
                  You go over to enter the passcode. What do you enter?""", """The code worked! The door opens, and all 3 of you quickly leave the premises. 
                  You turn left, and see a halfway branching out in 3 different ends. 
                  One is going left, one is going straight, and one goes right. 
                  On the floor, you see strange symbols etched deep into the marble. It says:

                        To find the path you desire, go to 1101100 1100101 1100110 1110100.

                Which hallway do you go down?""", """You go down the hallway and see odd portraits. 
                You decide to quickly leave and run until the end of the hallway,
                where you are met by a big bulky guard. 
                However, the guard thinks you are guests, and asks you for the password. 
                Loki quickly comes up with a lie, telling the guard you are a mathmetician,
                who works here.
                
                However, the guard still doesn't trust you, and decides to ask you a math question,
                just to test your knowledge and see if he can let you through:

                5/(7-4)**2*(11-2).

                What is the answer?""", """As you continue your journey through the futuristic facility, 
                you stumble upon a high-tech console that requires a passcode to proceed. 
                The screen displays the following challenge:

                The passcode is hidden within this message: 'ymnx nx f xjhwjy!' 
                Beside it, is a number saying 5.
                 
                
                What do you enter into the console to pass?"""
                , """After you go down the hallway, 
                you see a sign pointing to escape shuttles! 
                Eureka, you think knowing it's the way out. 
                You quickly run to the door, and find out it's locked, 
                but it has no keypad, only a computer. 
                Sylvie mentions how she has seen this type of door before, 
                where you have to hack into the system to enter. 
                She quickly walks up to it and starts coding. 
                After a brief moment, 
                she asks you how she can generate a random number between 1 and 1000.

                What do you respond?
""",f"""You run to a space full of shuttles. 
You quickly load into one, and try to start it. However, Loki points at the locked screen, 
and says that a password is needed. 
You look around the shuttle to find any clues, but find none. 
In the end, you resort to looking at the screen, where it turns into a puzzle: 

What is the value of sum which is printed out: 

sum = 0
for i in range(1, 10, 2):
    sum += i
"""]

challenge_image = ["challenge1.jpg", "challenge2.jpeg","challenge3.jpeg", "challenge4.jpeg", "challenge5.jpeg", "challenge6.png"]
challenge_answer = ["1000", "left", "5","this is a secret", "random.randint(1,1000)", "25"]
challenge_hint = ["Think about the decimal representation of the number!", "Convert it to decimal, then think of ASCII characters!", "Remember: Brackets, Exponents, Divide, Multiply, Add, Subtract", "Think about shifting the characters", "It is a function inside the random module!", "The 2 means it skips one number each time!"]

sidequest_text = ["""You go down the hallway and see a dark room. 
                Loki tells you to go in, 
                but you don’t want to, what do you do?""", """You see a small chest discreetly hidden on the other side of the escape shuttle room. 
                Knowing your greed, you have an urge to take it.
                However, another side of you wants to just escape Lamentis. 
                Do you check the chest?"""]
sidequest_image = []
sidequest_options = [["Check the room!", "Run the other way!"], ["Check the chest", "Leave as quick as you can"]]
sidequest_answer = [[[1,100], [0,0]], [[-3, 100],[0,0]]]
sidequest_text_shown = [["""You go inside and find a chest. 
                         When you open the chest you find 1 book of knowledge
                         and a 100 gold.""", """You leave as quickly as you can!"""], ["""You quickly run to the chest.
                                                                                       You run back, but then guards start chasing you!
                                                                                       In your haste, you drop all your books of knowledge!""", """You leave as quickly as you can!, running to the shuttles."""]]

user_text = ""

ending_texts = ["""You quickly speed off into the nearest galaxy. 
                However, 20 spaceships start following you, at max speed. 
                Just when you think it's over, 
                a turbo button pops up on the spaceship's window. 
                You click it, and fly away to safety…""", """You enter gold and quickly start the ship. 
                As you leave, you look back at the planet and wave goodbye. 
                You cruise safely for 30 minutes until 30 ships surround you. 
                All around, every single way is blocked. 
                They capture your ship, 
                and escort you back to the prison. 
                Back again, you say, 
                knowing you have to do all that work again…
""", """You enter gold and speed through to the nearest safe galaxy. 
Behind you, the enemy spaceships follow in pursuit. 
One shoots out your wings, 
making you  crash back onto the planet. 
Loki yells out, 

“You’ve done it! You’ve killed us all”..."""]
score = 0