from Mono import Mono
nick = Mono('','','','')
print("-------------------------------------------------------------------------------")
print("-------------------------------Start-------------------------------------------")
print('-------------------------------help--------------------------------------------')
while True:
    try:
        nick.to_log_in()
        nick.info()
        answer = input("Write command")
        if answer.lower().startswith("hel"):
            print("""
            Take cash
            Money
            Take credit
            Pay credit
            Trans
            Exit
            Sing up
            Bank
            Work""")
        elif answer.lower().startswith("take cash"):
            nick.to_take_cash()
        elif answer.lower().startswith("take credit"):
            nick.to_take_credit()
        elif answer.lower().startswith("money"):
            nick.to_money()
        elif answer.lower().startswith("take cash"):
            nick.to_take_cash()
        elif answer.lower().startswith("pay credit"):
            nick.to_pay_credit()
        elif answer.lower().startswith("trans"):
            nick.to_trans()
        elif answer.lower().startswith("exit"):
            nick.to_exit()
        elif answer.lower().startswith("sing up"):
            nick.to_sing_up()
        elif answer.lower().startswith("bank"):
            nick.to_bank()
        elif answer.lower().startswith("work"):
            nick.to_work()
    except:
        print('bite')