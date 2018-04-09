EconomyResources = {
                    "generalResources":175000, 
                    "intangibleAsset":6000, #ոչ նյութական ակտիվ
                    "settlementAccount":10000, #հաշվարկային հաշիվ
                    "cashRegister":200000, #դրամարկղ
                    "resources":5000,
                    "unfinishedProduct":4000, #անավարտ արտադրանք
                    "balance":400000 #հաշվեկշիռ
                    }

SourceOfResources = {
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
def GeneralResourcesCompute(SourceOfResources, EconomyResources):
    return SourceOfResources, EconomyResources

def IntangibleAssetCompute(SourceOfResources,EconomyResources):
    return SourceOfResources, EconomyResources

def SettlementAccountCompute(SourceOfResources,EconomyResources):
    EconomyResources["settlementAccount"] += profit - SourceOfResources["commitmentsToStaff"]
    return SourceOfResources, EconomyResources

def CashRegisterCompute(SourceOfResources,EconomyResources):
    EconomyResources["cashRegister"] += SourceOfResources["deposit"] - profit - getDeposit
    return SourceOfResources, EconomyResources

def ResourcesCompute(SourceOfResources,EconomyResources):
    return SourceOfResources, EconomyResources

def UnfinishedProductCompute(SourceOfResources,EconomyResources):
    return SourceOfResources, EconomyResources

# Source of resources compute
def CapitalCompute(SourceOfResources,EconomyResources):
    return SourceOfResources, EconomyResources

def CommercialCreditDebtCompute(SourceOfResources,EconomyResources):
    SourceOfResources["commercialCreditDebt"] += EconomyResources["generalResources"]
    return SourceOfResources, EconomyResources

def CreditDebtCompute(SourceOfResources,EconomyResources):
    SourceOfResources["creditDebt"] += ammount_FromCommitmentsToStuff_To_Credit_Debt  - SourceOfResources["commitmentsToStaff"]
    return SourceOfResources, EconomyResources

def ShortTermLoansCompute(SourceOfResources,EconomyResources):
    return SourceOfResources, EconomyResources

def CommitmentsToStuffCompute(SourceOfResources,EconomyResources):
    SourceOfResources["commitmentsToStaff"] -= ammount_FromCommitmentsToStuff_To_Credit_Debt  
    return SourceOfResources, EconomyResources

def DepositCompute(SourceOfResources,EconomyResources):
    SourceOfResources["deposit"] += getDeposit
    return SourceOfResources, EconomyResources

def BalanceCompute(Dict):
    balance = 0
    for key in Dict:
        if (key != "balance"):
            balance += Dict[key] #= sum(EconomyResources[key])
    Dict["balance"] = balance
    return Dict

def BalanceCompare(SourceOfResources, EconomyResources):
    print("balance Source:", BalanceCompute(SourceOfResources)["balance"])
    print("balance Economy Resources:", BalanceCompute(EconomyResources)["balance"])
    if BalanceCompute(SourceOfResources) == BalanceCompute(EconomyResources):
        print("balances are the same")
    else:
        print("balances are not the same")
print()
print(SourceOfResources)
print(EconomyResources)
BalanceCompare(SourceOfResources, EconomyResources)

SourceOfResources, EconomyResources = SettlementAccountCompute(SourceOfResources,EconomyResources)
SourceOfResources, EconomyResources = CashRegisterCompute(SourceOfResources,EconomyResources)
SourceOfResources, EconomyResources = CommercialCreditDebtCompute(SourceOfResources,EconomyResources)
SourceOfResources, EconomyResources = CreditDebtCompute(SourceOfResources,EconomyResources)
SourceOfResources, EconomyResources = CommitmentsToStuffCompute(SourceOfResources,EconomyResources)
print("after\n")
BalanceCompare(SourceOfResources, EconomyResources)