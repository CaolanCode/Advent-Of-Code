# Rock Paper Scissors part II
# when I chose X, I need to lose
# when I chose Y, I need to draw
# when I chose Z, I need to win
def opponent_A(my_choice): # Rock
    my_score = 0
    if my_choice == 'X': # Draw, need to lose with scissors
        my_score = 3 
    elif my_choice == 'Y': # I win, need to draw with rock
        my_score = 1 + 3
    elif my_choice == 'Z': # I lose, need to win with paper
        my_score = 2 + 6
    return my_score

def opponent_B(my_choice): # Paper
    my_score = 0
    if my_choice == 'X': # I lose, need to lose with rock
        my_score = 1
    elif my_choice == 'Y': # Draw, need to draw with paper
        my_score = 2 + 3
    elif my_choice == 'Z': # I win, need to win with scissors 
        my_score = 3 + 6
    return my_score

def opponent_C(my_choice): # Scissors
    my_score = 0
    if my_choice == 'X': # I win, need to lose with paper
        my_score = 2 
    elif my_choice == 'Y': # I lose, need to draw with scissors 
        my_score = 3 + 3
    elif my_choice == 'Z': # Draw, need to win with rock
        my_score = 1 + 6
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