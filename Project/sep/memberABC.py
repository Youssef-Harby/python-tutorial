import abc

class member(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def printPlayerData(self):
        pass

    def calcSalaryPerYear(self):
        pass

    def calcRemainingDuration(self):
        pass