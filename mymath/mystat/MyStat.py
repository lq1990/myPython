import numpy as np


class MyStat:
    def __init__(self):
        pass
    
    @classmethod
    def xavg(cls, ps, ns):
        '''

        :param ps: params
        :param ns: num of param
        :return:
        '''

        sum_num = 0
        sum_den = 0
        for i in range(len(ps)):
            sum_num += ps[i] * ns[i]
            sum_den += ns[i]

        if sum_den != 0:
            return sum_num / sum_den
        else:
            return 0

    @classmethod
    def xvar(cls, ps, ns):
        xavg_val = cls.xavg(ps, ns)
        sum_num = 0
        sum_den = 0
        for i in range(len(ps)):
            sum_num += (ps[i] - xavg_val) ** 2 * ns[i]
            sum_den += ns[i]

        if sum_den > 1:
            return sum_num / (sum_den - 1)
        else:
            return 0


if __name__ == '__main__':
    pass

