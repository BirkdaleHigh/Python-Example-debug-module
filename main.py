# Cover, Play to next, Step into (variables), Step out, Step over, Call Stack
# keys: F5 loads debugger against the current file. Ctrl+F5 loads AND runs
import myModule as example

def main(): # Debugger Example
    user_choice = input('How many new messages? ')
    example.demonstration( int(user_choice) ) # Module demo break here

# def main(): # Visual example
#     user_choice = input('How many new messages? ')
#     example.visual( int(user_choice) )

while True:
    main()
