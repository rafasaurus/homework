import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='example.log',level=logging.INFO)
logging.info('So should this')
#logging.warning('And this, too')
Active = 100000
Responsibility = 80000
Capital = 30000
Income = 10000
Expense = 20000

def logQuery():
    logging.info("*** new query ***")
    logging.info("Active: "+ str(Active))
    logging.info("Responsibility:" + str(Responsibility))
    logging.info("Capital:" + str(Capital))
    logging.info("Income:" + str(Income))
    logging.info("Expense:" + str(Expense))
    logging.info("Balance:" + str(Active - Responsibility - Capital - Income + Expense))

def capitalInc_expenseInc(arg, Capital, Expense):
    Capital += arg
    Expense += arg
    return Capital, Expense


logQuery()
Capital, Expense = capitalInc_expenseInc(500, Capital, Expense)
logQuery()
