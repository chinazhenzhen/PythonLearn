# coding:utf-8
#策略模式

class CashSuper: # 抽象策略角色： 策略类，通常由一个接口或者抽象类实现。
    def AcceptCash(self, money):
        return 0

class CashNormal(CashSuper): # 具体策略角色：包装了相关的算法和行为
    def AcceptCash(self, money):
        return money

class CashRebate(CashSuper):# 具体策略角色：包装了相关的算法和行为
    discount = 0
    def __init__(self, ds):
        self.discount = ds
    def AcceptCash(self, money):
        return money * self.discount

class CashReturn(CashSuper):# 具体策略角色：包装了相关的算法和行为
    total = 0
    ret = 0
    def __init__(self, t, r):
        self.total = t
        self.ret = r
    def AcceptCash(self, money):
        if (money >= self.total):
            return money - self.ret
        else:
            return money

class CashContext: # 环境角色：持有一个策略类的引用，最终给客户端调用。
    def __init__(self, csuper):
        self.cs = csuper
    def GetResult(self, money):
        return self.cs.AcceptCash(money)

if __name__ == "__main__":
    money = input("money:")
    strategy = {}
    strategy[1] = CashContext(CashNormal())
    strategy[2] = CashContext(CashRebate(0.8))
    strategy[3] = CashContext(CashReturn(300, 100))
    ctype = input("type:[1]for normal,[2]for 80% discount [3]for 300 -100.")
    if ctype in strategy:
        cc = strategy[ctype]
    else:
        print "Undefine type.Use normal mode."
        cc = strategy[1]
    print "you will pay:%d" % (cc.GetResult(money))
