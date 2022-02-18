import abc
import datetime
import math
# 1
# The class member is an abstract class.
# The class member has three abstract methods: printPlayerData, calcSalaryPerYear, and
# calcRemainingDuration.


class member(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def printPlayerData(self):
        pass

    def calcSalaryPerYear(self):
        pass

    def calcRemainingDuration(self):
        pass
# 2


class player(member):
    __playerName = None  # i
    __playerNumber = None  # ii
    __playerSalaryPerWeek = None  # iii
    __signingDate = None  # iv - Date/Time DataType 
    __contractDurationInYears = None  # v
    __numberOfMatchesPlayed = None  # vi

    #Getters

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
        return self.__playerName, \
            self.__playerNumber, \
            self.__playerSalaryPerWeek, \
            self.__signingDate, \
            self.__contractDurationInYears, \
            self.__numberOfMatchesPlayed

    #Setters

    def __setPlayerName(self,i):
        self.__playerName = i

    def __setPlayerNumber(self,ii):
        if ii <= 30:
            self.__playerNumber = ii
            print('playerNumber ',ii)
        else:
            print("Player Number should not exceed 3")

    def __setPlayerSalaryPerWeek(self,iii):
        if iii <= 100000:
            self.__playerSalaryPerWeek = iii
            print('playerSalaryPerWeek ',iii)
        else:
            print("Player Salary per week should not exceed 100,000")

    def __setContractDurationInYears(self,v):
        if v <= 5:
            self.__contractDurationInYears = v
            print("contractDurationInYears ", v)
        else:
            print("Max contract duration is 5 Years")

    def __setNumberOfMatchesPlayed(self,vi):
        self.__numberOfMatchesPlayed = vi

    # def __setAllInfo(self, i, ii, iii, iv, v, vi):
    #     self.__setPlayerName(i)
    #     self.__setPlayerNumber(ii)
    #     self.__setPlayerSalaryPerWeek(iii)
    #     self.__signingDate = iv #######################################
    #     self.__setContractDurationInYears(v)
    #     self.__setNumberOfMatchesPlayed(vi)

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
    playerName= property(__getPlayerName,__setPlayerName,__deletePlayerName)
    playerNumber= property(__getPlayerNumber,__setPlayerNumber,__deletePlayerNumber)
    playerSalaryPerWeek= property(__getPlayerSalaryPerWeek,__setPlayerSalaryPerWeek,__deletePlayerSalaryPerWeek)
    playerSigningDate= property(__getSigningDate)
    playerContractDurationInYears= property(__getContractDurationInYears,__setContractDurationInYears,__deleteContractDurationInYears)
    playerNumberOfMatchesPlayed= property(__getNumberOfMatchesPlayed,__setNumberOfMatchesPlayed,__deleteNumberOfMatchesPlayed)

    def __init__(self, i, ii, iii, iv, v, vi):
        # self.__setAllInfo(i, ii, iii, iv, v, vi)
        self.__setPlayerName(i)
        self.__setPlayerNumber(ii)
        self.__setPlayerSalaryPerWeek(iii)
        self.__signingDate = datetime.datetime.strptime(str(iv), "%Y-%m-%d").strftime('%Y-%m-%d')
        # print('########',iv,self.__signingDate)
        self.__setContractDurationInYears(v)
        self.__setNumberOfMatchesPlayed(vi)

    # abstract fun
    def printPlayerData(self):
        # print(self.__getAllInfo())
        return self.__getAllInfo()

    def calcSalaryPerYear(self):
        return self.playerSalaryPerWeek *4*12

    # calcRemainingDuration(): return remaining duration of the player in days 
    # Remaining duration(in weeks) = the date (now) – signing data
    def calcRemainingDuration(self):
        d1 = datetime.datetime.strptime(self.playerSigningDate,'%Y-%m-%d')
        d2 = datetime.datetime.today()
        print(d2-d1)
        if (self.playerContractDurationInYears*12*30)-(d2-d1).days > 0:
            return math.floor((self.playerContractDurationInYears * 52)-((d2 - d1).days/7))
        else:
            return -1