import random,math
from six.moves import cPickle as pickle

class ThreeCoinDataMgr:

    def __init__(self):
        self.data_root = "./data/"
        pass

    def gen_rand_data(self, pi, p, q, exp_num):

        # pi = random.random()
        # p = random.random()
        # q = random.random()

        #n = 10000
        exp_result = []
        for i in range(exp_num):
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

            exp_result.append(output)
        return exp_result

    def gen_file_name(self, pi, p, q, coin_count):
        return self.data_root + '3coin_' + 'pi{0:.0f}_'.format(pi*100) + 'p{0:.0f}_'.format(p*100) + 'q{0:.0f}'.format(q*100) + '_' + str(coin_count/1000) + 'K'

    def write_data(self, data_file, pi, p, q, exp_result):

        #data_file = self.gen_file_name(pi, p, q)
        try:
            f = open(data_file, 'wb')
            save = {
                'pi': pi,
                'p': p,
                'q': q,
                'exp_result': exp_result,
            }
            pickle.dump(save, f, pickle.HIGHEST_PROTOCOL)
            f.close()
        except Exception as e:
            print('Unable to save data to', exp_result, ':', e)
            raise

    def load_data(self, data_file):
        with open(data_file, 'rb') as f:
            save = pickle.load(f)
            pi = save['pi']
            p = save['p']
            q = save['q']
            exp_result = save['exp_result']
            del save  # hint to help gc free up memory
        return pi, p, q, exp_result

    def gen_dataset(self, exp_num, coin_count):

        for i in range(exp_num):
            pi = round(random.random(), 2)
            p = round(random.random(), 2)
            q = round(random.random(), 2)

            exp_result = data_mgr.gen_rand_data(pi, p, q, coin_count)
            data_file = data_mgr.gen_file_name(pi, p, q, coin_count)
            data_mgr.write_data(data_file, pi, p, q, exp_result)

if __name__ == "__main__":
    data_mgr = ThreeCoinDataMgr()

    # pi = 0.7
    # p = 0.3
    # q = 0.4
    # exp_result = data_mgr.gen_rand_data(pi, p, q, 10000)
    #
    # data_file = data_mgr.gen_file_name(pi, p, q)
    # data_mgr.write_data(data_file, pi, p, q, exp_result)

    for i in range(1, 11):
        data_mgr.gen_dataset(10, i * 1000)
    #print data_mgr.load_data(data_file)