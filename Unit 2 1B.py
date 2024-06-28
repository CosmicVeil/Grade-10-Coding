#Name: Mohan Dixit
#Date: February 27th, 2024
#Purpose: A function in the program is used to call another function.

#Define the function.
def say_hello():
    print("Hello, user.")

def call_say_hello():
    say_hello()

#Call the function which calls another function.
call_say_hello()
