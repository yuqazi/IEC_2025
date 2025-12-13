import random

def bot_guessing_game(correct_code):
    final_guesses = []
    # Iteration or round simulator
    for i in range(10):
        # If first round, don't give previous guesses.
        if i == 0:
            final_guesses.append(guessing(correct_code, i))
        # If not first round, give previous guesses.
        else:
            final_guesses.append(guessing(correct_code, i, final_guesses[i-1]))
    # print ("Bot Guess (inside): ", final_guesses, "\n")
    return final_guesses

def guessing(values, iteration, prevIter = [-1]*10):
    
    final_iteration_guesses = []
    guess_len = len(values)
        
    # When last round, return all correct values
    if(9 - iteration <= 0):
        for value in values:
            final_iteration_guesses.append(int(value))
    
    else:
        for i in range(guess_len):
            # If the guess made last round was not correct
            if (prevIter[i] != values[i]):
                print("Interior incorrect guess1: ", values[i], " vs ", prevIter[i], "\n", "-" * 100)
                # Random combination (no repetition) to fill in the rest of the array
                starter = list(range(10))
                foundation = random.sample(starter, 9 - iteration)
                
                # Append the correct value into the list
                foundation.append(values[i])
                # Remove the incorrect guess from possible guesses this turn (optional, keep to make bot much stronger)
                if prevIter[i] in foundation:
                    foundation.remove(prevIter[i])
                
                # Choose a random value from the list/make a guess!
                iteration_guess = random.choice(foundation)
                
                # print("Round:", iteration, "\n", foundation)
                
                final_iteration_guesses.append(int(iteration_guess))
            # Else append the correct guess made last round
            else:
                print("(C)Interior correct guess: ", values[i], " vs ", prevIter[i], "\n")
                final_iteration_guesses.append(int(prevIter[i]))
            
    return final_iteration_guesses

# mylistone = [1,5,2,8,9,0]
# print (bot_guessing_game(mylistone))

# mylisttwo = [4,6,7,2]
# bot_guessing_game(mylisttwo)
# print (bot_guessing_game(mylisttwo))