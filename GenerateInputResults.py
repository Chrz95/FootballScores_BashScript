import random as rd

teams = ['Greece','Portugal','Spain','France','Germany','England','Australia','Norway']

team_dict ={x:[0,0,0] for x in teams}

files = rd.randint(1,5)

f = open("scores1","w")

times = rd.randint(3,100)

win_score = 3
defeat_score = 0
draw_score = 1

for i in range (0,times):

   team1 = rd.randint(0,len(teams) - 1)
   team2 = rd.randint(0,len(teams) - 1)
   
   while team2 == team1:
        team2 = rd.randint(0,len(teams) - 1)

   team1 = teams[team1]
   team2 = teams[team2]

   score1 = rd.randint(0,10)
   score2 = rd.randint(0,10)

   if (score1 > score2): # team1 wins, team2 loses
      team_dict[team1][0] = team_dict[team1][0] + win_score
      team_dict[team1][1] = team_dict[team1][1] + score1
      team_dict[team1][2] = team_dict[team1][2] + score2

      team_dict[team2][0] = team_dict[team2][0] + defeat_score
      team_dict[team2][1] = team_dict[team2][1] + score2
      team_dict[team2][2] = team_dict[team2][2] + score1
   elif (score1 == score2): # Draw

      team_dict[team1][0] = team_dict[team1][0] + draw_score
      team_dict[team1][1] = team_dict[team1][1] + score1
      team_dict[team1][2] = team_dict[team1][2] + score2

      team_dict[team2][0] = team_dict[team2][0] + draw_score
      team_dict[team2][1] = team_dict[team2][1] + score2
      team_dict[team2][2] = team_dict[team2][2] + score1
   else:
      team_dict[team1][0] = team_dict[team1][0] + defeat_score
      team_dict[team1][1] = team_dict[team1][1] + score1
      team_dict[team1][2] = team_dict[team1][2] + score2

      team_dict[team2][0] = team_dict[team2][0] + win_score
      team_dict[team2][1] = team_dict[team2][1] + score2
      team_dict[team2][2] = team_dict[team2][2] + score1




   f.write(team1 + "-" + team2 + ":" + str(score1) + "-" + str(score2) + "\n")

print(team_dict)

f.close()
