import copy
def pureSalary(greedySalary_):
    greedySalary = copy.deepcopy(greedySalary_)
    # եկամտահարկ
    if (greedySalary_ <= 150000):
        greedySalary_ -= greedySalary*0.23
    elif (greedySalary_ <=2000000):
        greedySalary_ -= 150000*0.23 + (greedySalary - 150000)*0.28
    else:
        greedySalary_ -= 2000000*0.28 + (greedySalary - 2000000)*0.36

    # կենսաթոշակ
    if (greedySalary * 0.025 <= 12500):
        greedySalary_ -= greedySalary * 0.025
    else:
        greedySalary_ -= 12500
    # millitary stuff
    greedySalary_ -= 1000

    return greedySalary_


def holidaySalaryDailyFee(days, greedySalary):
    # ''' returns եկամտահարկ, կենսաթոշակ, military stuff '''
    # hevelavhchar F
    # oravardz
    premium = 20000
    commitmentForWeekends = 10000
    holidaySalary = 5000
    surcharge = premium + commitmentForWeekends + holidaySalary
    holydayDailyFee = (surcharge/12 + greedySalary)/21
    overallDailyFee = days * holydayDailyFee

    # եկամտահարկ
    greedySalary -= greedySalary / 21 * (21 - days)
    greedySalary += overallDailyFee
    if (greedySalary <= 150000):
        overallDailyFee -= greedySalary*0.23
    elif (overallDailyFee <=2000000):
        overallDailyFee -= 150000*0.23 + (greedySalary - 150000*0.23)*0.28
    else:
        overallDailyFee -= 150000*0.23 + (1850000 - 150000*0.23)*0.28 + (greedySalary - (1850000 - 150000*0.23)*0.28)*0.36

    # կենսաթոշակ
    if (greedySalary * 0.025 <= 12500):
        overallDailyFee -= greedySalary * 0.025
    else:
        overallDailyFee -= 12500
    # millitary stuff
    overallDailyFee -= 1000
    return overallDailyFee


salary = 5000000
days = 10
print("Salary: ", salary)
print("pure Salary: ", pureSalary(salary))
print("holidarySalaryDailyFee for ", days, " days: ", holidaySalaryDailyFee(days, salary))
