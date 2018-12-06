#!/usr/bin/python3
import logging
import xlwt
from tempfile import TemporaryFile
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')
import csv
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

index=0
index_value=0
row_index=0
row_index_value=0
field_editable = True


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

def setup_logger(name, level=logging.INFO):
    handler = logging.FileHandler("./log_files_lab_4/" + str(name) + ".log")        
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

def xls_writer(field_1, field_2, Asset, Passives):
    global index
    global index_value
    print("index:", index)
    for str_, value_ in Asset.items():
        index+=1
        sheet1.write(index,field_1,str_)
    
    for str_, value_ in Asset.items():
        index_value+=1
        sheet1.write(index_value,field_2,value_)
    
    
    for str_, value_ in Passives.items():
        index+=1
        sheet1.write(index,field_1,str_)
    
    for str_, value_ in Passives.items():
        index_value+=1
        sheet1.write(index_value,field_2,value_)
    print("index:", index)


profit = 200000
ammount_FromCommitmentsToStuff_To_Credit_Debt = 200000
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
def checkOperativeLiquidity(Passives, Asset):
    if (Asset["settlementAccount"] / Passives["commitmentsToStaff"] > 1):
        print("pass Operative Liquidity")
    else:
        print("does not pass Operative Liquidity")
def checkCurrentLiquidity(Passives, Asset):
    if ((Asset["settlementAccount"] + Asset["materials"]) / (Passives["creditDebt"] + Passives["longTermԼoans"]) >2):
        print("pass Current Liquidity")
    else:
        print("does not pass Current Liquidity")

def checkAbsoluteLiquidity(Passives, Asset):
    if ((Asset["settlementAccount"] + Asset["materials"] + Asset["generalResources"]) / (Passives["creditDebt"] + Passives["longTermԼoans"] + Passives["commitmentsToStaff"]) >2):
        print("pass Absolute Liquidity")
    else:
        print("does not pass Absolute Liquidity")
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

def AfterTransactionBalance(beforePassives, beforeAsset, afterPassives, afterAsset):
    ATB_Passives = {key: afterPassives[key] - beforePassives.get(key, 0) for key in afterPassives.keys()}
    ATB_Asset = {key: afterAsset[key] - beforeAsset.get(key, 0) for key in afterAsset.keys()}
    print("AfterTransactionOverAllBalance:", ATB_Passives)
    print("AfterTransactionOverAllBalance:", ATB_Asset)
    BalanceCompute(ATB_Passives)
    BalanceCompute(ATB_Asset)
    print("AfterTransactionOverAllBalance_Passives: ", ATB_Passives["balance"])
    print("AfterTransactionOverAllBalance_Asset: ", ATB_Asset["balance"])
    # return afterPassives - beforePassives, afterAsset - beforeAsset 
    pass


print(" ------ before transactions ------") 
result = checkAbsoluteLiquidity(Passives, Asset)
checkLiquidityBalance(Passives, Asset)
checkNonLiqudityBalance(Passives, Asset)
checkOperativeLiquidity(Passives, Asset)
checkCurrentLiquidity(Passives, Asset)
checkAbsoluteLiquidity(Passives, Asset)
BalanceCompare(Passives, Asset)
# transactions
beforePassives = Passives.copy()
beforeAsset = Asset.copy()
Passives, Asset = SettlementAccountCompute(Passives,Asset)
Passives, Asset = CreditDebtCompute(Passives,Asset)

# #TODO
sheet1.write(0, 0, "flan")
sheet1.write(0, 1, "fstan")
sheet1.write(0, 2, "flan")
sheet1.write(0, 3, "fstan")
xls_writer(0, 1, Asset, Passives)
print("index:", index)
index = 0
index_value = 0
xls_writer(2, 3, Asset, Passives)

# Passives, Asset = CommitmentsToStuffCompute(Passives,Asset)
AfterTransactionBalance(beforePassives, beforeAsset, Passives, Asset)
# Passives, Asset = CashRegisterCompute(Passives,Asset)
# Passives, Asset = CommercialCreditDebtCompute(Passives,Asset)
print(" ------ after transactions ------") 
result = checkAbsoluteLiquidity(Passives, Asset)
checkLiquidityBalance(Passives, Asset)
checkNonLiqudityBalance(Passives, Asset)
BalanceCompare(Passives, Asset)
name = "random.xls"
book.save(name)
book.save(TemporaryFile())
