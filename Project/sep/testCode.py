from player import *
from teamCaptain import *
from coach import *
from team import *

p1 = player('Ronaldo',7,1000,'2021-02-22',3,27)
c1 = coach('MJ',10000,'2021-02-22',3,10,1000)
t1 = teamCaptain('Salah',11,1000,'2021-02-22',3,27,18,5000)
team1 = team('7ambola',4,c1,[p1,p1],t1,2)
# team1.addPlayer('Salah',11,1000,'2021-02-22',3,27)