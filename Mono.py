from random import randint
from uuid import uuid4
class Mono:
    def __init__(self, name,password,adr,pho):
        self.balance = 0
        self.money = 0
        self.id = str(uuid4())
        self.password = password
        self.name = name
        self.adress = adr
        self.phone = pho
        self.credit = 0
        self.reg = False
        self.base_adress = []
        self.base_phone = []
        self.base_password = []
        self.base_name = []
    def to_take_cash(self):
        namb = int(input("How much: "))
        if namb < self.balance:
            self.balance -= namb
            self.money += namb
        else:
            print("Недостатньо грошей на балансі")
    def to_money(self):
        namb = int(input("How much: "))
        if namb > self.balance:
            self.money -= namb
            self.balance += namb
        else:
            print("Недостатньо грошей налом")
    def to_take_credit(self):
        namd = int(input("How much: "))
        self.balance += namd
        self.credit += namd
    def to_pay_credit(self):
        namd = int(input("How much: "))
        if namd < self.balance:
            self.balance -= namd
            self.credit -= namd
        else:
            print("Недостатньо грошей на балансі")
    def to_trans(self):
        namd = int(input("How much: "))
        if namd < self.balance:
            self.balance -= namd
    def to_exit(self):
        if self.reg == True:
            self.name = ''
            self.adress = ''
            self.password = ''
            self.id = str(uuid4())
            print('Звиняй мультіплеєр ще не зроблений')
            pass
        else:
            print('Bro login pls')
    def to_log_in(self):
        if self.reg == False:
            x = 0
            name = input("Youre name:")
            adress = input("Youre adress:")
            number = input("Youre number:")
            password = input("Youre password:")
            for i in self.base_adress:
                if i == adress:
                    x += 1
            for i in self.base_password:
                if i == password:
                    x += 1
            for i in self.base_phone:
                if i == number:
                    x += 1
            if x > 0:
                print('Oops')
            else:
                self.name = name
                self.adress = adress
                self.password = password
                self.phone = number
                self.base_adress.append(adress)
                self.base_phone.append(number)
                self.base_password.append(password)
                self.base_name.append(name)
                self.reg = True
    def to_sing_up(self):
        x = 0
        name = input("Youre name:")
        adress = input("Youre adress:")
        number = input("Youre number:")
        password = input("Youre password:")
        for i in self.base_adress:
            if i == adress:
                x += 1
        for i in self.base_password:
            if i == password:
                x += 1
        for i in self.base_phone:
            if i == number:
                x += 1
        for i in self.base_name:
            if i == name:
                x += 1
        if x == 4:
            print('Ок')
            self.reg = True
        else:
            print('Oops')
    def to_bank(self):
        n = randint(0,10)
        if n == 1:
            self.money += 1000
        else:
            self.money -= 100
    def to_work(self):
        tim = int(input("How much"))
        print("U work")
        self.money += tim*10
    def info(self):
        self.credit += self.credit * 0.1
        if self.credit > 100:
            self.balance -= 100
            self.credit = 0
        print(f"credit={self.credit} \tname={self.name} \tbalance={self.balance} \tmoney={self.money} \tid={self.id} \t adress={self.adress} \t phone={self.phone}")