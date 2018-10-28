#!/usr/bin/python3
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

Asset = {
    "generalResources": 25000, #հիմնական միջոցներ  # ''' A '''
    "materials": 20000, #նյութեր                  # ''' B '''
    "settlementAccount": 35000, #հաշվարկային հաշիվ # ''' C '''
    "mainProduct": 50000,                             # ''' D '''
    "delayedExpenses": 40000, #հետաձգված ծախսեր       # ''' E '''
    "unfinshedJobs": 70000,                           # ''' F '''
    "damage": 30000,                                  # ''' G '''
    "balance":75000 #հաշվեկշիռ
    # "intangibleAsset":6000, #ոչ նյութական ակտիվ
    # "cashRegister":200000, #դրամարկղ
    # "resources":5000,
    # "unfinishedProduct":4000, #անավարտ արտադրանք
}

Passives = {
    "capital":60000,                                            # ''' H  ''' 
    "profit":10000,                                                 # ''' I  ''' 
    "creditDebt":70000,                                             # ''' J  ''' 
    "commitmentsToStaff":100000, #պարտավորություններ անձնակազմին # ''' K  ''' 
    "longTermԼoans":30000, #կարճաժամկետ վարկեր                      # ''' L  ''' 
    "balance":75000                                                       
    # "commercialCreditDebt":180000, #առևվտրային կրեդիտ պարտք
    # "deposit":0,
}

profit = 20000
ammount_FromCommitmentsToStuff_To_Credit_Debt = 20000
getDeposit = 2000

# # economyr resources compute
# def GeneralResourcesCompute(Passives, Asset): return Passives, Asset

def checkAbsoluteLiquidity(Passives, Asset):
    " C > K "
    " B > J "
    " A > L "
    " D + E + F + G < H + I "
    if (Asset["settlementAccount"] < Passives["commitmentsToStaff"]
     or Asset["materials"] < Passives["creditDebt"] 
     or Asset["generalResources"] < Passives["longTermԼoans"] 
     or Asset["delayedExpenses"] + Asset["mainProduct"] + Asset["unfinshedJobs"] + Asset["balance"] > Passives["capital"] + Passives["profit"]):
        print("> doesnt pass Absolute Liquidity")
        return 0
    else:
        print("> pass Absolute Liquidity")
        return 1


def checkLiquidityBalance(Passives, Asset):
    " A + B + C > K > L + J "
    " D + E + F + F < H + I "
    if (Asset["generalResources"] + 
        Asset["materials"] + 
        Asset["settlementAccount"] < 
        Passives["creditDebt"] + 
        Passives["commitmentsToStaff"] + 
        Passives["longTermԼoans"]):
        print("> doesnt pass Liquidity Balance")
        return 0
    else:
        print("> pass Liquidity Balance")
        return 1
    pass
def checkNonLiqudityBalance(Passives, Asset):
    " A + B + C > K < L + J "
    " D + E + F + F > H + I "
    if (Asset["generalResources"] + 
       Asset["materials"] + 
       Asset["settlementAccount"] > 
       Passives["creditDebt"] + 
       Passives["commitmentsToStaff"] + 
       Passives["longTermԼoans"]):
        print("> doesnt pass None Liquidity Balance")
        return 0
    else:
        print("> pass None Liquidity Balance")
        return 1

    
def IntangibleAssetCompute(Passives,Asset):
    return Passives, Asset

def SettlementAccountCompute(Passives,Asset):
    Asset["settlementAccount"] += profit - Passives["commitmentsToStaff"]
    logQuery("settlementAccount", Asset["settlementAccount"])
    return Passives, Asset

# def CashRegisterCompute(Passives,Asset):
#     Asset["cashRegister"] += Passives["deposit"] - profit - getDeposit
#     logQuery("cashRegister", Asset["cashRegister"])
#     logQuery("deposit", Passives["deposit"])
#     return Passives, Asset

def ResourcesCompute(Passives,Asset):
    return Passives, Asset

def UnfinishedProductCompute(Passives,Asset):
    return Passives, Asset

# Source of resources compute
def CapitalCompute(Passives,Asset):
    return Passives, Asset

# def CommercialCreditDebtCompute(Passives,Asset):
#     Passives["commercialCreditDebt"] += Asset["generalResources"]
#     logQuery("commercialCreditDebt", Passives["commercialCreditDebt"])
#     logQuery("generalResources", Asset["generalResources"])
#     return Passives, Asset

def CreditDebtCompute(Passives,Asset):
    Passives["creditDebt"] += ammount_FromCommitmentsToStuff_To_Credit_Debt  - Passives["commitmentsToStaff"]
    logQuery("creditDebt", Passives["creditDebt"])
    logQuery("commitmentsToStaff", Passives["commitmentsToStaff"])
    return Passives, Asset

def ShortTermLoansCompute(Passives,Asset):
    return Passives, Asset

# def CommitmentsToStuffCompute(Passives,Asset):
#     Passives["commitmentsToStaff"] -= ammount_FromCommitmentsToStuff_To_Credit_Debt  
#     logQuery("commitmentsToStaff", Passives["commitmentsToStaff"])
#     return Passives, Asset

def DepositCompute(Passives,Asset):
    Passives["deposit"] += getDeposit
    return Passives, Asset

def BalanceCompute(Dict):
    balance = 0
    for key in Dict:
        if (key != "balance"):
            balance += Dict[key] #= sum(Asset[key])
    Dict["balance"] = balance
    return Dict

def BalanceCompare(Passives, Asset):
    print(" --- balance compare ---")
    print("* balance Passives:", BalanceCompute(Passives)["balance"])
    print("* balance Asset:", BalanceCompute(Asset)["balance"])
    if BalanceCompute(Passives)["balance"] == BalanceCompute(Asset)["balance"]:
        print("  balances are the same")
    else:
        print("  balances are not the same")
# print(Passives)
# print(Asset)
BalanceCompare(Passives, Asset)


print(" ------ before transactions ------") 
result = checkAbsoluteLiquidity(Passives, Asset)
checkLiquidityBalance(Passives, Asset)
checkNonLiqudityBalance(Passives, Asset)
BalanceCompare(Passives, Asset)
# transactions
Passives, Asset = SettlementAccountCompute(Passives,Asset)
Passives, Asset = CreditDebtCompute(Passives,Asset)
# Passives, Asset = CommitmentsToStuffCompute(Passives,Asset)
# Passives, Asset = CashRegisterCompute(Passives,Asset)
# Passives, Asset = CommercialCreditDebtCompute(Passives,Asset)
print(" ------ after transactions ------") 
result = checkAbsoluteLiquidity(Passives, Asset)
checkLiquidityBalance(Passives, Asset)
checkNonLiqudityBalance(Passives, Asset)
BalanceCompare(Passives, Asset)
