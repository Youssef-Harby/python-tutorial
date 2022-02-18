from player import *
from teamCaptain import *
from coach import *


class team:

    #Fields
    __teamName = None
    __teamPositionInLeague = None
    __coach = coach # (it will be a coach object)
    __playersList = player # (it is a list of players)
    __teamCaptain = teamCaptain # (it is a Team Captain object)
    __numberOfPlayers = None

    #Getters

    def __getTeamName(self):
        return self.__teamName
    
    def __getTeamPositionInLeague(self):
        return self.__teamPositionInLeague
    
    def __getCoach(self):
        return self.__coach

    def __getPlayersList(self):
        return self.__playersList

    def __getTeamCaptain(self):
        return self.__teamCaptain

    def __getNumberOfPlayers(self):
        return self.__numberOfPlayers

    #Setters

    def __setTeamName(self,teamName):
        self.__teamName = teamName
    
    def __setTeamPositionInLeague(self,teamPosInLeague):
        self.__teamPositionInLeague = teamPosInLeague
    
    def __setCoach(self,coach):
        self.__coach = coach

    def __setPlayersList(self,playersList):
        self.__playersList = playersList

    def __setTeamCaptain(self,teamCaptain):
        self.__teamCaptain = teamCaptain

    def __setNumberOfPlayers(self,numberOfPlayers):
        self.__numberOfPlayers = numberOfPlayers

    #Deleters

    def __delTeamName(self):
        del self.__teamName
    
    def __delTeamPositionInLeague(self):
        del self.__teamPositionInLeague
    
    def __delCoach(self):
        del self.__coach

    def __delPlayersList(self):
        del self.__playersList

    def __delTeamCaptain(self):
        del self.__teamCaptain

    def __delNumberOfPlayers(self):
        del self.__numberOfPlayers

    teamName = property(__getTeamName,__setTeamName,__delTeamName)
    teamPosInLeague = property(__getTeamPositionInLeague,__setTeamPositionInLeague,__delTeamPositionInLeague)
    coach = property(__getCoach,__setCoach,__delCoach)
    playersList = property(__getPlayersList,__setPlayersList,__delPlayersList)
    teamCaptain = property(__getTeamCaptain,__setTeamCaptain,__delTeamCaptain)
    numberOfPlayers = property(__getNumberOfPlayers)

    def __init__(self,teamName,teamPosInLeague,coach,playersList = [],teamCaptain='Hoss',numberOfPlayers=0):
        self.__setTeamName(teamName)
        self.__setTeamPositionInLeague(teamPosInLeague)
        # self.__setCoach(coach)
        #coach.__init__(self, cName, cSalaryweek, cSigningDate, cContractDurationInYears, cExpInYears, coachBonus)
        self.__setPlayersList(list(playersList)) #[ ] Empty List
        # teamCaptain.__init__(self)
        self.__setTeamCaptain(teamCaptain)
        self.__setNumberOfPlayers(numberOfPlayers)

    def __len__(self):
      return len(self.__getPlayersList())

    def addPlayer(self, pName, pNumber, pSalaryPerWeek, pSigningDate, pContractDurationInYears, pNumberOfMatchesPlayed):
      i = player(pName, pNumber, pSalaryPerWeek, pSigningDate, pContractDurationInYears, pNumberOfMatchesPlayed)

    def printTeamData(self):
        return self.teamName,self.teamPosInLeague,self.coach.printPlayerData,self.playersList,self.teamCaptain,self.numberOfPlayers
    
    def printCaptainInfo(self):
        return self.teamCaptain
    def addPlayer():
        pass