import calendar
money = 1000
years = 5
months = 20
days = 4
percentage = 20
'''
money = input("money = ")
years = input("years = ")
months = input("months = ")
days = input("days = ")
'''
def simple(money, year, month, days,percentage,days_of_year,days_of_month):
    money_year = money
    money_month = money
    money_day = money
    money_year = money_year * (1+year*percentage)

    money_month = money_month*(1 + percentage*month/days_of_month)

    money_day = money_day*(1 + percentage*days/days_of_year)


    return money_day+money_month+money_year-2*money
#def complex(money, year, month, days,percentage,days_of_year,days_of_month):
def complex(money, year,percentage):
    money_year = money

    money_year = money_year * pow((1+percentage),5)
    return money_year


def simple_complex(money, year, month, days,percentage,days_of_year,days_of_month):
    money_ = money
    days = days + month*days_of_month
    #for i_year in range(year)
    money_=money*pow((1+percentage),year) * (1+percentage*days/days_of_year)
    #money_ =
    return money_

def german_practise(money, year, month, days,percentage):
    cal = calendar.monthrange(2017,1)
    return simple(money,year,month,days,percentage,360,cal[1])
def franch_practise(money, year, month, days,percentage):
    return simple(money,year,month,days,percentage,360,29)
def england_practise(money, year, month, days,percentage):
    return simple_complex(money,year,month,days,percentage,365,30)

def german_practise_complex(money, year, month, days,percentage):
    return complex(money,year,percentage)
def franch_practise_complex(money, year, month, days,percentage):
    return complex(money,year,percentage)
def england_practise_complex(money, year, month, days,percentage):
    return complex(money,year,percentage)

def german_practise_simple_complex(money, year, month, days,percentage):
    return simple_complex(money,year,month,days,percentage,360,30)
def franch_practise_simple_complex(money, year, month, days,percentage):
    return simple_complex(money,year,month,days,percentage,360,29)
def england_practise_simple_complex(money, year, month, days,percentage):
    return simple_complex(money,year,month,days,percentage,365,30)



percentage = percentage/100
print("german practise=",german_practise(money, years, months, days, percentage))
print("franch practise=",franch_practise(money, years, months, days, percentage))
print("england practise=",england_practise(money, years, months, days, percentage))
print()
print("german practise complex=",german_practise_complex(money, years, months, days, percentage))
print("franch practise complex=",franch_practise_complex(money, years, months, days, percentage))
print("england practise complex=",england_practise_complex(money, years, months, days, percentage))
print()
print("german practise simple complex=",german_practise_simple_complex(money, years, months, days, percentage))
print("franch practise simple complex=",franch_practise_simple_complex(money, years, months, days, percentage))
print("england practise simple complex=",england_practise_simple_complex(money, years, months, days, percentage))
print()

print(calendar.monthrange(2017,12))