import logging

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

def setup_logger(name, level=logging.INFO):
    handler = logging.FileHandler("./log_files_lab_2/" + str(name) + ".log")        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    print("logger:" + str(name))
    return logger

def logQuery(name, value):
    logger = setup_logger(name)
    logger.info("*** new query ***")
    logger.info(str(name) + ":" + str(value))
    print("creating:" + str(name))

Active = {
                    "generalResources":175000, 
                    "intangibleAsset":6000, #ոչ նյութական ակտիվ
                    "settlementAccount":10000, #հաշվարկային հաշիվ
                    "cashRegister":200000, #դրամարկղ
                    "resources":5000,
                    "unfinishedProduct":4000, #անավարտ արտադրանք
                    "balance":400000 #հաշվեկշիռ
                    }

Passives = {
                    "capital":200000,
                    "commercialCreditDebt":180000, #առևվտրային կրեդիտ պարտք
                    "creditDebt":6000,
                    "shortTermԼoans":10000, #կարճաժամկետ վարկեր
                    "commitmentsToStaff":4000, #պարտավորություններ անձնակազմին
                    "deposit":0,
                    "balance":400000
                    }

profit = 195000
ammount_FromCommitmentsToStuff_To_Credit_Debt = 500
getDeposit = 2000

# economyr resources compute
def GeneralResourcesCompute(Passives, Active): return Passives, Active

def IntangibleAssetCompute(Passives,Active):
    return Passives, Active

def SettlementAccountCompute(Passives,Active):
    Active["settlementAccount"] += profit - Passives["commitmentsToStaff"]
    logQuery("settlementAccount", Active["settlementAccount"])
    return Passives, Active

def CashRegisterCompute(Passives,Active):
    Active["cashRegister"] += Passives["deposit"] - profit - getDeposit
    logQuery("cashRegister", Active["cashRegister"])
    logQuery("deposit", Passives["deposit"])
    return Passives, Active

def ResourcesCompute(Passives,Active):
    return Passives, Active

def UnfinishedProductCompute(Passives,Active):
    return Passives, Active

# Source of resources compute
def CapitalCompute(Passives,Active):
    return Passives, Active

def CommercialCreditDebtCompute(Passives,Active):
    Passives["commercialCreditDebt"] += Active["generalResources"]
    logQuery("commercialCreditDebt", Passives["commercialCreditDebt"])
    logQuery("generalResources", Active["generalResources"])
    return Passives, Active

def CreditDebtCompute(Passives,Active):
    Passives["creditDebt"] += ammount_FromCommitmentsToStuff_To_Credit_Debt  - Passives["commitmentsToStaff"]
    logQuery("creditDebt", Passives["creditDebt"])
    logQuery("commitmentsToStaff", Passives["commitmentsToStaff"])
    return Passives, Active

def ShortTermLoansCompute(Passives,Active):
    return Passives, Active

def CommitmentsToStuffCompute(Passives,Active):
    Passives["commitmentsToStaff"] -= ammount_FromCommitmentsToStuff_To_Credit_Debt  
    logQuery("commitmentsToStaff", Passives["commitmentsToStaff"])
    return Passives, Active

def DepositCompute(Passives,Active):
    Passives["deposit"] += getDeposit
    return Passives, Active

def BalanceCompute(Dict):
    balance = 0
    for key in Dict:
        if (key != "balance"):
            balance += Dict[key] #= sum(Active[key])
    Dict["balance"] = balance
    return Dict

def BalanceCompare(Passives, Active):
    print("balance Source:", BalanceCompute(Passives)["balance"])
    print("balance Economy Resources:", BalanceCompute(Active)["balance"])
    if BalanceCompute(Passives) == BalanceCompute(Active):
        print("balances are the same")
    else:
        print("balances are not the same")
print()
print(Passives)
print(Active)
BalanceCompare(Passives, Active)

Passives, Active = SettlementAccountCompute(Passives,Active)
Passives, Active = CashRegisterCompute(Passives,Active)
Passives, Active = CommercialCreditDebtCompute(Passives,Active)
Passives, Active = CreditDebtCompute(Passives,Active)
Passives, Active = CommitmentsToStuffCompute(Passives,Active)
print("after\n")
BalanceCompare(Passives, Active)
