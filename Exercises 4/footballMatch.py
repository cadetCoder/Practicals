def footballMatch():
    team1_name = input("Enter the name of the first team: ")
    team1_score = int(input("Enter the score of the first team: "))
    
    team2_name = input("Enter the name of the second team: ")
    team2_score = int(input("Enter the score of the second team: "))

##  if team 1 wins
    if team1_score > team2_score:
        team1_points = 3
        team2_points = 0
##  if team 2 wins
    elif team1_score < team2_score:
        team1_points = 0
        team2_points = 3
##  if the scores are draw
    else:
        team1_points = 1
        team2_points = 1


    print(f"{team1_name} got {team1_points} league points.")
    print(f"{team2_name} got {team2_points} league points.")
