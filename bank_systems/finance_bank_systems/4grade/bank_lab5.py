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

def pureHolidayFee():
    holidayTaxJune, holidayPensionsJune, overallDailyFeeJune = getholidayTaxAndPensions(11, 300000) 
    holidayTaxJuly, holidayPensionsJuly, overallDailyFeeJuly = getholidayTaxAndPensions(9, 300000) 
    overallHolidayFee = overallDailyFeeJune + overallDailyFeeJuly
    return overallHolidayFee - holidayTaxJune - holidayTaxJuly - holidayPensionsJune - holidayPensionsJuly

def getholidayTaxAndPensions(days, greedySalary):
    # ''' returns եկամտահարկ, կենսաթոշակ, military stuff '''

    premium = 200000
    commitmentForWeekends = 30000
    holidaySalary = 60000
    pureSalary = 200000 # for 15 days that had been worked
    surcharge = premium + commitmentForWeekends + holidaySalary # հավելավճար F
    holidayDailyFee = (surcharge/12 + greedySalary)/21
    overallDailyFee = days * holidayDailyFee
    print("overallDailyFee: ", overallDailyFee)

    # ____________________________________
    # եկամտահարկ income tax
    # աճողական գումար եկամտահարկ հունիս ամսվա
    pureSalary_ = copy.deepcopy(pureSalary)
    pureSalary_ += overallDailyFee
    pureSalary += overallDailyFee
    if (pureSalary_ <= 150000):
        pureSalary_ -= pureSalary*0.23
    elif (pureSalary_ <=2000000):
        pureSalary_ -= 150000*0.23 + (pureSalary - 150000)*0.28
    else:
        pureSalary_ -= 2000000*0.28 + (pureSalary - 2000000)*0.36
    # կենսաթոշակ
    if (pureSalary * 0.025 <= 12500):
        pensionsForMonth = pureSalary * 0.025
    else:
        pensionsForMonth -= 12500
    # print("pensionsForMonth: ", pensionsForMonth)
    incomeTaxForTheMonth = copy.deepcopy(pureSalary - pureSalary_)
    # print("incomeTaxForTheMonth: ", incomeTaxForTheMonth)
    # ____________________________________

    # ************************************
    pureSalary -= overallDailyFee
    # եկամտահարկ income tax
    incomTaxForDaysWorked = 0
    if (pureSalary <= 150000):
        incomTaxForDaysWorked = pureSalary*0.23
    elif (pureSalary_ <=2000000):
        incomTaxForDaysWorked = 150000*0.23 + (pureSalary - 150000)*0.28
    else:
        incomTaxForDaysWorked = 2000000*0.28 + (pureSalary - 2000000)*0.36

    # կենսաթոշակ
    if (pureSalary * 0.025 <= 12500):
        pensionsForDays = pureSalary * 0.025
    else:
        pensionsForDays = 12500
    print("pensionsForDays: ", pensionsForDays)
    # ************************************

    # արձակուրդի եկամտահարկ, և կենսաթոշակ 
    holidayTax = incomeTaxForTheMonth - incomTaxForDaysWorked
    holidayPensions = pensionsForMonth - pensionsForDays
    return holidayTax, holidayPensions, overallDailyFee


salary = 300000
days = 11
print("Salary: ", salary)
print("pure Salary: ", pureSalary(salary))
print("pureHolidayFee: ", pureHolidayFee())
