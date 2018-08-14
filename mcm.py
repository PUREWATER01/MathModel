from random import random
import numpy as np
import math
class MCM:
    '''
    输入函数函数,积分上下限,实验次数,即可计算蒙特卡洛积分
    用__init__初始化
    solve有两种方法,投点法和平均值法
    '''

    def __init__(self, f, xlim, ylim=(0,1), times=10000):
        '''
        f是函数,按照正常python函数写,返回函数表达式
        xlim和ylim是元组或者列表
        times是实验次数,根据电脑性能选择合理的值
        '''
        self.f = f
        self.xlim = xlim
        self.ylim = ylim
        self.times = times

    def __choose_point(self, xlim, ylim):
        x = random() * (xlim[1] - xlim[0]) + xlim[0]
        y = random() * (ylim[1] - ylim[0]) + ylim[0]
        return x, y

    def solve_point(self):
        a = 0
        for i in range(self.times):
            x, y = self.__choose_point(self.xlim, self.ylim)
            if self.f(x) > y:
                a += 1
        return (a / self.times) * (self.xlim[1] - self.xlim[0]) * (self.ylim[1] - self.ylim[0])

    def solve_average(self):
        sum=0
        a = np.random.rand(self.times)*(self.xlim[1] - self.xlim[0]) + self.xlim[0]
        for i in range(self.times):
            sum+=self.f(a[i])
        return (self.xlim[1] - self.xlim[0]) * sum / self.times




def f(x):
    return math.sin(x)


mcm = MCM(f, (0, 3.141592965355), (0, 2), 1000000)
print(mcm.solve_point())
print(mcm.solve_average())