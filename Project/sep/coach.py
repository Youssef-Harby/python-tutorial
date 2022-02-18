from memberABC import *
import datetime
# 4


class coach(member):
    __coachName = None
    __coachSalaryPerWeek = None
    __coachsigningDate = None  # Date/Time DataType
    __coachContractDurationInYears = None
    __coachExperienceYears = None
    __coachBonus = None

    # Getters

    def __getCoachName(self):
        return self.__coachName

    def __getCoachSalaryPerWeek(self):
        return self.__coachSalaryPerWeek

    def __getCoachSigningDate(self):
        return self.__coachsigningDate

    def __getCoachContractDurationInYears(self):
        return self.__coachContractDurationInYears

    def __getCoachExperienceYears(self):
        return self.__coachExperienceYears

    def __getCoachBonus(self):
        return self.__coachBonus

    def __getCoachAllInfo(self):
        return self.__coachName, \
            self.__coachSalaryPerWeek, \
            self.__coachsigningDate, \
            self.__coachContractDurationInYears, \
            self.__coachExperienceYears, \
            self.__coachBonus

    # Setters

    def __setCoachName(self, cName):
        self.__coachName = cName

    def __setCoachSalaryPerWeek(self, cSalaryweek):
        if cSalaryweek <= 200000:
            self.__coachSalaryPerWeek = cSalaryweek
            # print('CoachSalaryPerWeek ', cSalaryweek)
        else:
            print("Player Salary per week should not exceed 200,000")

    def __setCoachContractDurationInYears(self, cContractDurationInYears):
        if cContractDurationInYears <= 3:
            self.__coachContractDurationInYears = cContractDurationInYears
            # print("contractDurationInYears ", cContractDurationInYears)
        else:
            print("it should be greater than or equal 3 years")

    def __setCoachExperienceYears(self, cExpInYears):
        if cExpInYears >= 8:
            self.__coachExperienceYears = cExpInYears
            # print("Coach Experience Years ", cExpInYears)
        else:
            print("it should be greater than or equal 8 years")

    def __setCoachBonus(self, coachBonus):
        if coachBonus <= 50000:
            self.__coachBonus = coachBonus
            # print('Coach Bonus ', coachBonus)
        else:
            print("Coach Bonus should not exceed 50,000")

    # Deleters

    def __delCoachName(self):
        del self.__coachName

    def __delCoachSalaryPerWeek(self):
        del self.__coachSalaryPerWeek

    def __delCoachSigningDate(self):  # Don't know add it as property or not
        del self.__coachsigningDate

    def __delCoachContractDurationInYears(self):
        del self.__coachContractDurationInYears

    def __delCoachExperienceYears(self):
        del self.__coachExperienceYears

    def __delCoachBonus(self):
        del self.__coachBonus

    #Encapsulation / Proberty
    coachName = property(__getCoachName, __setCoachName, __delCoachName)
    coachSalaryPerWeek = property(
        __getCoachSalaryPerWeek, __setCoachSalaryPerWeek, __delCoachSalaryPerWeek)
    coachSigningDate = property(__getCoachSigningDate)
    coachContractDurationInYears = property(
        __getCoachContractDurationInYears, __setCoachContractDurationInYears, __delCoachContractDurationInYears)
    coachExperienceYears = property(
        __getCoachExperienceYears, __setCoachExperienceYears, __delCoachExperienceYears)
    coachBonus = property(__getCoachBonus, __setCoachBonus, __delCoachBonus)
    player1stAllInfo = property(__getCoachAllInfo)

    def __init__(self, cName, cSalaryweek, cSigningDate, cContractDurationInYears, cExpInYears, coachBonus):
        self.__setCoachName(cName)
        self.__setCoachSalaryPerWeek(cSalaryweek)
        self.__coachsigningDate = datetime.datetime.strptime(
            str(cSigningDate), "%Y-%m-%d").strftime('%Y-%m-%d')
        self.__setCoachContractDurationInYears(cContractDurationInYears)
        self.__setCoachExperienceYears(cExpInYears)
        self.__setCoachBonus(coachBonus)

    def __repr__(self):
        return "\n Coach Name: {0}\n Coach Signing Date: {1}\n Coach Salary: {2}\n Contract Duration: {3}\n Coach Bonus: {4}\n Coach Experience Years: {5}\n".format(self.__coachName, self.__coachsigningDate, self.__coachSalaryPerWeek, self.__coachContractDurationInYears, self.__coachBonus, self.__coachExperienceYears)

    # abstract fun

    def printPlayerData(self):
        return self.__getCoachAllInfo()

    def calcSalaryPerYear(self):
        return self.coachSalaryPerWeek * 4*12

    def calcRemainingDuration(self):
        d1 = datetime.datetime.strptime(self.coachSigningDate, '%Y-%m-%d')
        d2 = datetime.datetime.today()
        # print(d2-d1)
        if (self.coachContractDurationInYears*12*30)-(d2-d1).days > 0:
            return (self.coachContractDurationInYears * 52)-((d2 - d1).days/7)
        else:
            return -1
