import math
import cmath
import scipy.stats
from scipy.stats import norm
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
    def priceTreecall(self):
        for i in range(self.pr):
            temp = self.S*self.u**(self.pr - i)*self.d**(i)-self.K
            if temp < 0
                temp = 0
            self.list.append(temp)
        for j in range(self.pr - 1)
            for k in range(0,len(self.list) - 1,-1)
                self.list[k] = (math.exp(-self.r*self.t/self.pr)*(self.p*self.list[k]+(1-self.p)*self.list[k+1]))
            if len(list) = 1
                break
            self.list.pop()
        return self.list[0]
    def priceBSMcall(self):
        d1 = (math.log(self.S/self.K)+(self.r+self.sigma*self.sigma/2.0)*self.T/(self.sigma*cmath.sqrt(self.T))
        d2 = d1 - self.sigma*cmath.sqrt(self.T)
        c = self.S*norm.ppf(d1,0,1)- self.K*exp(-1*self.r*self.T)*norm.ppf(d2,0,1)
        return c
    def priceTreeput(self):
        for i in range(self.pr):
            temp = self.K-self.S*self.u**(self.pr - i)*self.d**(i)
            if temp < 0
                temp = 0
            self.list.append(temp)
        for j in range(self.pr - 1)
            for k in range(0,len(self.list) - 1,-1)
                self.list[k] = (math.exp(-self.r*self.t/self.pr)*(self.p*self.list[k]+(1-self.p)*self.list[k+1]))
            if len(list) = 1
                break
            self.list.pop()
        return self.list[0]
    def priceBSMput(self):
        d1 = (math.log(self.S/self.K)+(self.r+self.sigma*self.sigma/2.0)*self.T/(self.sigma*cmath.sqrt(self.T))
        d2 = d1 - self.sigma*cmath.sqrt(self.T)
        put = self.K*exp(-1*self.r*self.T)*norm.ppf(-d2,0,1)-self.S*norm.ppf(-d1,0,1)
        return put
