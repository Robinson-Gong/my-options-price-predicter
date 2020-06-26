import math
import cmath
class Parameter:
    def __init__(self,strikeprice,currentprice,volatility,rate,time,period):
        self.K = strikeprice
        self.S = currentprice
        self.sigma = volatility
        self.r = rate
        self.T = time
        self.pr = period
        self.t = self.T/slef.pr
        self.u = math.exp(sigma*cmath.sqrt(t))
        self.d = u**(-1)
        self.p = (math.exp(r*t)-d)/(u-d)
        self.list=[]
    def pricepredict(self):
        for i in range(self.pr):
            self.list.append(self.S*self.u**(self.pr - i)*self.d**(i))
        for j in range(self.pr - 1)
            for k in range(len(self.list) - 1)
                self.list[k] = (math.exp(-self.r*self.t/self.pr)*(self.p*self.list[k]+(1-self.p)*self.list[k+1]))
            if len(list) = 1
                break
            self.list.pop()
        return self.list[0]
class 
