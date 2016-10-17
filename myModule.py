def demonstration(amount):
    i = 0
    while i < amount:
        print('Success message' + '!'*i) # Loop demo break here
        i += 1

def visual(amount):
    print('function parameter amount: ' + str(amount))
    i = 0
    print('create local variable(i) to count iterations: ' + str(i))
    while i < amount:
        print('i is less than amount')
        print('Success message')
        i += 1
        print('Add 1 to i: ' + str(i))

def welcomeMessage():
    print('...Loading custom module')

welcomeMessage() #Show the module file gets run by 'import'

## Test that this file has been run directly, not from 'import'
if __name__ == '__main__':
    demonstration( 3 )