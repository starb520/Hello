
def prompt_user_input():
    '''Prompt user for a statement he/she would like to display to the screen.'''
    user_input = input("What would you like to display to the screen? ")
    return user_input

def display(user_input):
    '''Display user input to the screen.'''
    print(user_input)


# Let's make this fun. Continue to prompt user for text he/she would like to
# display until he/she is bored and doesn't want to continue.
continue_display = True
while continue_display:
    user_input = prompt_user_input()
    display(user_input)
    print()
    do_again = input("Would you like to display something else? [Y/N] ")
    if do_again.upper() == "NO" or do_again.upper() == "N":
        continue_display = False
    
# print("Hello World!")