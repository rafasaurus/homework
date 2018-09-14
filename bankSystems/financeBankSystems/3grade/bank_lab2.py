

def first():
    expense = 900
    worth = 1200
    active = 1000
    capital = 600
    responsibility = 400
    total_worth = 1300
    damage = 0

    active = active - expense + worth
    worth = worth - expense
    capital = capital + worth+ responsibility

    print(capital, active)


def seccond():
    expense = 800
    worth = 1100
    active = 1000
    capital = 600
    responsibility = 400
    total_worth = 1000
    damage = 0

    active = active - expense + worth - (worth-expense)
    worth = worth - expense
    responsibility = responsibility-worth

    capital = capital + worth + responsibility
    print(capital, active)

def third():
    expense = 900
    worth = 700
    damage = expense-worth
    active = 1000
    capital = 600
    responsibility = 400
    total_worth = 900

    active = active - expense + worth
    capital = capital - damage + responsibility
    print(active,capital)
def fourth():
    expense = 900
    worth = 600
    damage = expense - worth
    active = 1000
    capital = 600
    responsibility = 400
    total_worth = 900
    deposit = 300

    active = active - expense+worth+damage
    capital= capital - damage + responsibility + deposit
    print(active,capital)

first()
seccond()
third()
fourth()