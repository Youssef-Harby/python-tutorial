from player import *
from teamCaptain import *
from coach import *
from team import *

p1 = player('Ronaldo', 7, 1001, '2021-02-22', 3, 27)
p2 = player('Messi', 10, 1002, '2021-02-22', 3, 27)
c1 = coach('MJ', 10000, '2021-02-22', 3, 10, 1000)
t1 = teamCaptain('Bebo', 11, 1003, '2021-02-22', 3, 27, 18, 5000)
team1 = team('Egypt', 4, c1, [p1, p2], t1, 2)
team1.addPlayer('Salah', 11, 1000, '2021-02-22', 3, 27)
# print(team1.printTeamData())
# print('Number of Players On the Team:',len(team1))
# print(team1.teamCaptain)
print(team1.calcAllSalary())
