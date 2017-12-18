import random,math

from threecoin_datamgr import ThreeCoinDataMgr


class ThreeCoinEM:

    def __init__(self):
        pass

    def expectation_max(self, data):

        # init pi, p, and q

        # init 1: 0.601991745103 0.257843754532 0.438740367994
        pi = 0.5
        p = 0.8
        q = 0.9

        # init 2: 0.5 0.3298421 0.3298421
        # pi = 0.5
        # p = 0.5
        # q = 0.5

        n = len(data)

        for it in range(10):
            # E step: compute mu = P(Z|X,theta)
            mu = []
            for xi in data:
                prob_B = pi * p**xi * (1 - p)**(1 - xi)
                prob_C = (1 - pi) * q**xi * (1 - q)**(1 - xi)
                mu_i = prob_B / (prob_B + prob_C)
                mu.append(mu_i)

            # M step
            sum_mu = sum(mu)
            #tmp = sum(1 - mu_i for mu_i in mu)
            pi = 1.0 / n * sum_mu
            #tt = [mu[i] * data[i] for i in range(n)]
            #tt2 = sum(tt)
            p = sum(mu[i] * data[i] for i in range(n)) / sum_mu
            q = sum((1 - mu[i]) * data[i] for i in range(n)) / sum(1 - mu_i for mu_i in mu)

            #print pi, p, q

        return pi, p, q

if __name__ == "__main__":

    data_mgr = ThreeCoinDataMgr()
    data_file = "./data/3coin_pi70_p30_q40"
    pi, p, q, data = data_mgr.load_data(data_file)

    em_solver = ThreeCoinEM()
    em_solver.expectation_max(data)

    pass

