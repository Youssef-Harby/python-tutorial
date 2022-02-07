## Python OOP Project
### 1. **Member Class:**
- This class is an abstract class.
- It has only 3 abstract methods (empty methods contains
pass):
1. printPlayerData()
2. calcSalaryPerYear()
3. calcRemainingDuration()

### 2. **Player Class:**
- Player Class inherits Member class.
- Private Fields:
1. Player Name
2. Player Number
3. Player Salary per week
4. Signing Date
5. contract duration in years,
6. number of matches played
>- Note: Signing Date will be as Date/time Data type(google it)
>- c- All private fields should have (setter, getter, delete,Property)

These are some constrains that should be implemented in the setters and getters:

1. Player Number shouldn’t exceed 30.
2. Player Salary per week shouldn’t exceed 100,000
3. Max contract duration is 5 Years.
4. Signing Date is read only Fields (No setter)
5. Parametrized constructor with initial values that support constructor over loading.
>Notes:
>- Obligatory fields (must be entered via constructor)
>-(Player Name -Player Number - Signing Date)
- Optional fields:
- Salary per week = 20,000
- contract duration in years = 3
- number of matches played = 0
>Note: User will enter the values via constructor and these entered values will be assigned to the private fields of the class via Properties/setters/getters
- The class overrides the 3 functions of the Member
- Class as follows:
1. printPlayerData(): print all the private fields.
2. calcSalaryPerYear(): return the total salary of the player per Year
    - total salary per year = weekly salary * 4 * 12
3. calcRemainingDuration(): return remaining duration of the player in days
    - Remaining duration(in weeks) = the date (now) – signing data

> Note: use the data time now method (google it)
- The Player class has the following additional functions:
1. IncreamentMatches(): This functions will add +1 to the number of matches played.
2. increamentContractDutarion (number of additional years): this function receives the number of additional years and adds it to (contract duration in years)

### 3. **Team captain Class:**
- Team class inherits Player Class.
- Additional private Fields:
1. Leading Matches: (number of matches played as a
team captain)
2. Bonus
> All private fields should have (setter, getter, delete, Property)
- These are some constrains that should be implemented in the setters and getters:
1. Bonus shouldn’t exceed 100,000
2. Leading Matches is read only (No setter)
- Parametrized constructor with initial values that support constructor over loading.
>Notes:
>  1. Obligatory fields (must be entered via constructor)
>    (Player Name -Player Number - Signing Date)
- Optional fields:
1. Salary per week = 20,000
2. contract duration in years = 3
3. number of matches played = 0
4. Bonus = 5000
5. Leading Matches = 10
- The class overrides the 2 functions of the Player Class as follows:
1. printPlayerData(): print all the private fields (it will
print the additional fields of the team captain and the fields from the player (Parent Class)).
2. calcSalaryPerYear(): return the total salary of the
player per Year total salary per year = weekly salary * 4 * 12 + Bonus
- The class has additional functions:
- increamentLeadingMtaches(): this function add +1 to the Leading Matches field.
- Overload the “+” built in operator:
When two players are added => it should return the summation of their salaries.

### 4. **Coach Class:**
- Player Class inherits Member class.
- Private Fields:
1. Coach Name
2. Coach Salary per week
3. Signing Date
4. contract duration in years
5. Experience Years
6. Bonus
>Note: Signing Date will be as Date/time Data type(google it)
> - c- All private fields should have (setter, getter, delete, Property)

- >These are some constrains that should be implemented in the setters and getters:
1. Coach Salary per week shouldn’t exceed 200,000
2. Max contract duration is 3 Years.
3. Signing Date is read only Field (No setter)
4. Experience Years are read only field and it should be greater than or equal 8 years.
5. Bonus shouldn’t exceed 50,000

- Parametrized constructor with initial values that support
constructor over loading.
>Notes:
>- Obligatory fields (must be entered via constructor)
>- (Coach Name - Experience Years- Signing Date)
- **Optional fields:**
- Salary per week = 50,000
- contract duration in years = 2
- Bonus = 10,000
- **The class overrides the 3 functions of the Member Class as follows:**
1. printPlayerData(): print all the private fields.
2. calcSalaryPerYear(): return the total salary of the player per Year total salary per year = weekly salary * 4 * 12 + bonus
3. calcRemainingDuration(): return remaining duration of the player in days
   - Remaining duration(in weeks) = the date (now) – signing data
>- Note: use the data time now method (google it)
- **The Coach class has additional functions:**
1. IncreamentExperience Years(): this function increment
the number of Experience Years by +1
2. Add Bonus(value of bonus): this function receives the
value of the bonus and assign it to the bonus field
(replace the old bonus).

### 5. **Team Class:**
- Private Fields:
1. Team Name
2. Team Position in League
3. Coach (it will be a coach object)
4. PlayersList (it is a list of players)
5. Team Captain (it is a Team Captain object)
6. Number of Players
>- All private fields should have (setter, getter, delete, Property)
>- The only condition is that the Number of Players is read only.
- Parametrized constructor with initial values that support constructor over loading.
> Notes:
>   - Obligatory fields (must be entered via constructor)
>   - (Team Name - Team Position in League -Coach)
>   - initial fields (not entered by user during creating the team object)( it will have the following initial values):
>   - number of players = 0
>   - playersList = [] (empty List)
>   - Team Captain = None
- **The team class has the following functions:**
1. printTeamData(self):
   - this function will print the whole team data.
2. printCaptainInfo(self):
   - this function print the captain information only
3. add player(self, Player Name, Player Number, Player Salary per week, Signing Date, contract duration in years, number of matches played).
   - first search if the player number is already exists or not.
   - If the player number is already exist in the team => print (“change the player number”)
   - Else => create a Player object with the given data
   - Add this player object to the Players List.
   - Increase the Number of Players by +1
   - Call modify the captain function to update the team captain ( the next function)
4. modifyTheCaptain(self,bonus,NumberOfMatches played as a captain):
   - this function will search the Players list with player with largest number of matches played.
   - Take this player information from step a in addition to the bonus and NumberOfMatches played as a captain and create a Team Captain object using these data.
   - Assign the Team captain object from b to the Team captain field in the Team class.
5. Delete player(self, player number):
   - This function will delete the player with the given number in the function from the players list.
   - Decrease the players number by -1
   - If the player is not found => print “ no player exists with the given number”
6. Search Player(self, player number):
   - This function receive the player and print the whole data of the player if he is found in the team.
7. calcAllSalary(self):
   - this function returns the summation of all the players salary + coach salary.
    > - Note: you can use the “+” built in operator that us implemented in the player class.
8. overload the built in __len__ function:
   - this function will return the number of players.
9. Overload the indexer (Read Only Indexer) teamObject[ given Player number] => print the player data this indexer is read only => it will take the player number.
if the player is found it will print his whole data and return its name.

### 6. **Test the code.**
- [ ] Create a coach object.
- [ ] Create a team object (team name, team position, coach)
- [ ] Add 4 players using the function Add Player in the team object.
- [ ] Use the built in function len() to print the number of players.
- [ ] Print the team captain data.
- [ ] Print the whole team data.
- [ ] Call the calcAllSalary to find the total salaries in the team.
- [ ] Call Search Player to find a player with a specific number.
- [ ] Use the indexer to find the player with same number in point h.
- [ ] Delete one of the players using Delete player function.
- [ ] Print the team captain data.
- [ ] Print the whole team data.
- [ ] Use the built in function len() to print the number of players.
- [ ] Call the calcAllSalary to find the total salaries in the team.

Thanks to ***Eng. Mohamed Reda***