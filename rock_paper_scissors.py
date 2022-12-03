# Rock, Paper, Scissors competition
# Opponent: A = Rock, B = Paper, C = Scissors
# Mine: X = Rock, Y = Paper, Z = Scissors
# Choice: Rock = 1, Paper = 2, Scissors = 3
# Round: lost = 0, Draw = 3, Win = 6

def opponent_A(my_choice): # Rock
    my_score = 0
    if my_choice == 'X': # Draw
        my_score = 1 + 3
    elif my_choice == 'Y': # I win
        my_score = 2 + 6
    elif my_choice == 'Z': # I lose
        my_score = 3
    return my_score

def opponent_B(my_choice): # Paper
    my_score = 0
    if my_choice == 'X': # I lose
        my_score = 1 
    elif my_choice == 'Y': # Draw
        my_score = 2 + 3
    elif my_choice == 'Z': # I win
        my_score = 3 + 6
    return my_score

def opponent_C(my_choice): # Scissors
    my_score = 0
    if my_choice == 'X': # I win
        my_score = 1 + 6
    elif my_choice == 'Y': # I lose 
        my_score = 2 
    elif my_choice == 'Z': # Draw 
        my_score = 3 + 3
    return my_score

results = open("rps_results.txt", 'r')
my_score = 0

for line in results:
    opponent_choice = line[0]
    my_choice = line[2]
    if opponent_choice == 'A':
        my_score += opponent_A(my_choice)            
    elif opponent_choice == 'B':
        my_score += opponent_B(my_choice)            
    elif opponent_choice == 'C':
        my_score += opponent_C(my_choice)            

print("My total score is: " + str(my_score))
results.close()

