import glob
import random

import time
from sklearn.metrics import mean_absolute_error

from threecoin_EM import ThreeCoinEM
from threecoin_datamgr import ThreeCoinDataMgr
import numpy as np

from threecoin_gibbs import ThreeCoinGibbsSampler

def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

class ThreeCoinExpMgr:

    def __init__(self):
        """Initialize experiment """
        pass

    def head_ratio(self, pi, p, q):
        n = 100000
        head_count = 0
        for i in range(n):
            coin_A = random.random()

            if coin_A < pi:
                #choose coin B
                coin_B = random.random()
                if coin_B < p:
                    output = 0
                else:
                    output = 1
            else:
                # choose coin C
                coin_C = random.random()
                if coin_C < q:
                    output = 0
                else:
                    output = 1

            if output == 0:
                head_count += 1

        return float(head_count) / n


    def get_truth_ratio(self, data):

        n = len(data)

        head_count = 0

        for i in range(n):
            if data[i] == 0:
                head_count += 1

        return float(head_count) / n



    def exp_gibbs_sampling(self, data):

        sampler = ThreeCoinGibbsSampler(data)
        # Use the sampler to estimate the document labels.
        estimate_pi, estimate_p, estimate_q = sampler.estimate_variables(20, 5, 2)
        test_ratio = self.head_ratio(estimate_pi, estimate_p, estimate_q)

        return test_ratio


    def exp_EM(self, data):

        em_solver = ThreeCoinEM()
        estimate_pi, estimate_p, estimate_q = em_solver.expectation_max(data)
        test_ratio = self.head_ratio(estimate_pi, estimate_p, estimate_q)

        return 1- test_ratio

    def exp_mse_percount(self):

        data_mgr = ThreeCoinDataMgr()

        em_mae = []
        em_mape = []
        gibbs_mae = []
        gibbs_mape = []

        # efficiency
        em_runtime = []
        gibbs_runtime = []

        for i in range(1, 11):

            print "=====" + str(i) + "====="
            em_mae_sum = 0

            gibbs_mae_sum = 0

            y_true = []
            y_em = []
            y_gibbs = []
            exp_count = 0

            runtime_em = []
            runtime_gibbs = []
            for data_file in glob.glob("./data/*" + str(i) + 'K'):
                #print data_file

                # data_file = "./data/3coin_pi70_p30_q40"
                truth_pi, truth_p, truth_q, data = data_mgr.load_data(data_file)

                truth_ratio = exp_mgr.get_truth_ratio(data)

                start_time = time.time()
                gibbs_ratio = exp_mgr.exp_gibbs_sampling(data)
                runtime_gibbs.append(time.time() - start_time)

                start_time = time.time()
                em_ratio = exp_mgr.exp_EM(data)
                runtime_em.append(time.time() - start_time)

                y_true.append(truth_ratio)
                y_em.append(em_ratio)
                y_gibbs.append(gibbs_ratio)

                exp_count += 1

                if exp_count == 10:
                    break

            em_runtime.append(round(np.mean(runtime_em), 4))
            gibbs_runtime.append(round(np.mean(runtime_gibbs), 4))

            em_mae.append(round(mean_absolute_error(y_true, y_em), 4))
            gibbs_mae.append(round(mean_absolute_error(y_true, y_gibbs), 4))

            em_mape.append(round(mean_absolute_percentage_error(y_true, y_em), 4))
            gibbs_mape.append(round(mean_absolute_percentage_error(y_true, y_gibbs), 4))

        print em_mae
        print gibbs_mae

        print em_mape
        print gibbs_mape

        print em_runtime
        print gibbs_runtime


if __name__ == "__main__":

    # Load the data
    exp_mgr = ThreeCoinExpMgr()
    # for data_file in glob.glob("./data/*"):
    #     #print data_file
    #     data_mgr = ThreeCoinDataMgr()
    #     #data_file = "./data/3coin_pi70_p30_q40"
    #     truth_pi, truth_p, truth_q, data = data_mgr.load_data(data_file)
    #
    #     truth_ratio = exp_mgr.get_truth_ratio(data)
    #
    #     gibbs_ratio = exp_mgr.exp_gibbs_sampling(data)
    #     em_ratio = exp_mgr.exp_EM(data)
    #
    #     print "[", truth_ratio, "] ", gibbs_ratio, "|", em_ratio

    exp_mgr.exp_mse_percount()



