def open_account():
    print("새로운 계좌가 생성되었습니다")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {}원 입니다".format(balance+money))
    return balance+money

def withdraw(balance, money) :
    if balance > money:
        print("출금이 완료되었습니다. 잔액은{}원입니다".format(balance-money))
        return balance-money
    else :
        print("출금이 완료되지않았습니다. 잔액은 {}원 입니다".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance-money-commission # 튜플의 형태로 retrun

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission , balance = withdraw_night(balance,500)
print("수수료는 {}원이며 잔액은{}원 입니다".format(commission,balance))


def profile(name,age, *language):
    print("이름 :{}\t나이:{}\t".format(name,age),end =" ")
    for lang in language:
        print(lang, end =" ")
    
profile("유재석",20, "Java","PhP","script")