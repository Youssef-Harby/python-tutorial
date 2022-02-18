from player import *
#3
class teamCaptain(player):
    __leadingMatches = None
    __bonus = None

    # Setters
    # def __setLeadingMatches(self,i):
    #     self.__leadingMatches = i

    def __setBonus(self, ii):
        if ii <= 100000:
            self.__bonus = ii
            print('playerSalaryPerWeek ', ii)
        else:
            print("Captain Bonus should not exceed 100,000")

    # Getters
    def __getLeadingMatches(self):
        return self.__leadingMatches

    def __getBonus(self):
        return self.__bonus

    # Deleter
    def __deleteLeadingMatches(self):
        del self.__leadingMatches

    def __deleteBonus(self):
        del self.__bonus
    LeadingMatches = property(__getLeadingMatches, __deleteLeadingMatches)
    Bonus = property(__getBonus, __setBonus, __deleteBonus)

    def __init__(self, pName, pNumber, pSalaryPerWeek, pSigningDate, pContractDurationInYears, pNumberOfMatchesPlayed,leadMatches=10,bonus=5000):
        # super().__init__(i, ii, iii, iv, v, vi)
        # Creating a player object.
        player.__init__(self, pName, pNumber, pSalaryPerWeek, pSigningDate, pContractDurationInYears, pNumberOfMatchesPlayed)
        self.__leadingMatches = leadMatches
        self.__setBonus(bonus)

    def printPlayerData(self):
        return self.player1stAllInfo + (self.__leadingMatches,self.__bonus,)

    def calcSalaryPerYear(self):
        return (self.playerSalaryPerWeek * 4 * 12) + self.__bonus

    def calcRemainingDuration(self):
        player.calcRemainingDuration(self)