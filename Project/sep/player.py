from memberABC import *
import datetime
# 1
# The class member is an abstract class.
# The class member has three abstract methods: printPlayerData, calcSalaryPerYear, and
# calcRemainingDuration.

# 2


class player(member):
    __playerName = None  # i
    __playerNumber = None  # ii
    __playerSalaryPerWeek = None  # iii
    __signingDate = None  # iv - Date/Time DataType
    __contractDurationInYears = None  # v
    __numberOfMatchesPlayed = None  # vi

    # Getters

    def __getPlayerName(self):
        return self.__playerName

    def __getPlayerNumber(self):
        return self.__playerNumber

    def __getPlayerSalaryPerWeek(self):
        # print(self.__playerSalaryPerWeek)
        return self.__playerSalaryPerWeek

    def __getSigningDate(self):
        return self.__signingDate

    def __getContractDurationInYears(self):
        return self.__contractDurationInYears

    def __getNumberOfMatchesPlayed(self):
        return self.__numberOfMatchesPlayed

    def __getAllInfo(self):
        return \
            self.__playerName, \
            self.__playerNumber, \
            self.__playerSalaryPerWeek, \
            self.__signingDate, \
            self.__contractDurationInYears, \
            self.__numberOfMatchesPlayed

    # Setters

    def __setPlayerName(self, pName):
        self.__playerName = pName

    def __setPlayerNumber(self, pNumber):
        if pNumber <= 30:
            self.__playerNumber = pNumber
            return('playerNumber ', pNumber)
        else:
            return("Player Number should not exceed 3")

    def __setPlayerSalaryPerWeek(self, pSalaryPerWeek):
        if pSalaryPerWeek <= 100000:
            self.__playerSalaryPerWeek = pSalaryPerWeek
            return('playerSalaryPerWeek ', pSalaryPerWeek)
        else:
            return("Player Salary per week should not exceed 100,000")

    def __setContractDurationInYears(self, pContractDurationInYears):
        if pContractDurationInYears <= 5:
            self.__contractDurationInYears = pContractDurationInYears
            return("contractDurationInYears ", pContractDurationInYears)
        else:
            return("Max contract duration is 5 Years")

    def __setNumberOfMatchesPlayed(self, pNumberOfMatchesPlayed):
        self.__numberOfMatchesPlayed = pNumberOfMatchesPlayed

    # Deleters
    def __deletePlayerName(self):
        del self.__playerName

    def __deletePlayerNumber(self):
        del self.__playerNumber

    def __deletePlayerSalaryPerWeek(self):
        del self.__playerSalaryPerWeek

    def __deleteContractDurationInYears(self):
        del self.__contractDurationInYears

    def __deleteNumberOfMatchesPlayed(self):
        del self.__numberOfMatchesPlayed

    #Encapsulation / Proberty
    playerName = property(__getPlayerName, __setPlayerName, __deletePlayerName)
    playerNumber = property(
        __getPlayerNumber, __setPlayerNumber, __deletePlayerNumber)
    playerSalaryPerWeek = property(
        __getPlayerSalaryPerWeek, __setPlayerSalaryPerWeek, __deletePlayerSalaryPerWeek)
    playerSigningDate = property(__getSigningDate)
    playerContractDurationInYears = property(
        __getContractDurationInYears, __setContractDurationInYears, __deleteContractDurationInYears)
    playerNumberOfMatchesPlayed = property(
        __getNumberOfMatchesPlayed, __setNumberOfMatchesPlayed, __deleteNumberOfMatchesPlayed)
    player1stAllInfo = property(__getAllInfo)

    def __init__(self, pName, pNumber, pSalaryPerWeek, pSigningDate, pContractDurationInYears, pNumberOfMatchesPlayed):
        self.__setPlayerName(pName)
        self.__setPlayerNumber(pNumber)
        self.__setPlayerSalaryPerWeek(pSalaryPerWeek)
        self.__signingDate = datetime.datetime.strptime(
            str(pSigningDate), "%Y-%m-%d").strftime('%Y-%m-%d')
        self.__setContractDurationInYears(pContractDurationInYears)
        self.__setNumberOfMatchesPlayed(pNumberOfMatchesPlayed)

    # abstract fun
    def printPlayerData(self):
        return self.__getAllInfo()

    def __repr__(self):
        return "\n Name: {0}\n PlayerNumber: {1}\n Player Salary: {2}\n Contract Duration: {3}\n Number Of Matches Played: {4}\n".format(self.__playerName, self.__playerNumber, self.__playerSalaryPerWeek, self.__contractDurationInYears, self.__numberOfMatchesPlayed)

    def calcSalaryPerYear(self):
        return self.playerSalaryPerWeek * 4*12

    # calcRemainingDuration(): return remaining duration of the player in days
    # Remaining duration(in weeks) = the date (now) – signing data
    def calcRemainingDuration(self):
        d1 = datetime.datetime.strptime(self.playerSigningDate, '%Y-%m-%d')
        d2 = datetime.datetime.today()
        # print(d2-d1)
        if (self.playerContractDurationInYears*12*30)-(d2-d1).days > 0:
            return (self.playerContractDurationInYears * 52)-((d2 - d1).days/7)
        else:
            return -1
