import random

from threecoin_datamgr import ThreeCoinDataMgr
import numpy as np

class ThreeCoinGibbsSampler:

    def __init__(self, data):
        """Initialize the Gibbs sampler """
        self.data = data

    def _initialize_gibbs_sampler(self):
        """
        Initialize the Gibbs sampler

        This sets the initial values of the C{labels} and C{thetas} parameters.
        """
        self.pi = np.random.beta(1, 1)
        self.p = np.random.beta(1, 1)
        self.q = np.random.beta(1, 1)

        toss_num = self.data_num()
        self.labels = np.array([bernoulli_sample(self.pi) for _ in range(toss_num)])

        pass


    def estimate_variables(self, iterations=10, burn_in=0, lag=0):
        """Estimate the variables.

        Run the Gibbs sampler and use the expected value of the labels as the label
        estimates.

        @param iterations: number of iterations to run
        @type iterations: integer
        @param burn_in: number of burn in iterations to ignore before returning results
        @type burn_in: integer
        @param lag: number of iterations to skip between returning values
        @type lag: integer
        @return: document label estimates
        @rtype: array
        """
        estimated_pi = 0
        estimated_p = 0
        estimated_q = 0
        for iteration, pi, p, q in self.run(iterations, burn_in, lag):
            estimated_pi += pi
            estimated_p += p
            estimated_q += q
        return estimated_pi / iterations, estimated_p / iterations, estimated_q / iterations

    def run(self, iterations=10, burn_in=0, lag=0):
        """Run the Gibbs sampler

        @param iterations: number of iterations to run
        @type iterations: integer
        @param burn_in: number of burn in iterations to ignore before returning results
        @type burn_in: integer
        @param lag: number of iterations to skip between returning values
        @type lag: integer
        """
        self._initialize_gibbs_sampler()
        lag_counter = lag
        iteration = 1
        while iteration <= iterations:
            self._iterate_gibbs_sampler()
            if burn_in > 0:
                burn_in -= 1
            else:
                if lag_counter > 0:
                    lag_counter -= 1
                else:
                    lag_counter = lag
                    yield iteration, self.pi, self.p, self.q
                    iteration += 1

    def _iterate_gibbs_sampler(self):
        """Perform a Gibbs sampling iteration.

        This updates the values of the C{labels} and C{thetas} parameters.
        """
        data_num = self.data_num()  # corpus size
        coin_counts = np.empty(data_num, int)

        # Get class counts and word counts for the classes.
        for coin_idx in range(data_num):
            coin_counts[coin_idx] = np.count_nonzero(self.labels == coin_idx)

        # Estimate the new document labels.
        for coin_idx in range(data_num):
            coin_tail = (self.data[coin_idx])
            coin_head = 1 - coin_tail

            prob_head = self.pi * self.p**coin_head * (1 - self.p)**coin_tail
            prob_tail = (1 - self.pi) * self.q**coin_head * (1 - self.q)**coin_tail
            self.labels[coin_idx] = bernoulli_sample(prob_head / (prob_head + prob_tail))

        # Estimate the new pi, p and q.
        c_0 = np.count_nonzero(self.labels == 0)
        c_1 = np.count_nonzero(self.labels == 1)
        nc0_0 = 0
        nc0_1 = 0
        nc1_0 = 0
        nc1_1 = 0
        for i in range(data_num):
            if self.labels[i] == 0:
                if self.data[i] == 0:
                    nc0_0 += 1
                else:
                    nc0_1 += 1
            else:
                if self.data[i] == 0:
                    nc1_0 += 1
                else:
                    nc1_1 += 1

        self.pi = np.random.beta(1 + c_0, 1 + c_1)
        self.p = np.random.beta(1 + nc0_0, 1 + nc0_1)
        self.q = np.random.beta(1 + nc1_0, 1 + nc1_1)


    def data_num(self):
        """
        @return: number of data
        @rtype: integer
        """
        return len(self.data)

def bernoulli_sample(distribution):
    """Sample a random integer according to a multinomial distribution.

    @param distribution: probabilitiy distribution
    @type distribution: array of log probabilities
    @return: integer in the range 0 to the length of distribution
    @rtype: integer
    """
    eta = random.random()
    if eta <= distribution:
        return 0
    else:
        return 1

if __name__ == "__main__":

    # Load the data
    data_mgr = ThreeCoinDataMgr()
    data_file = "./data/3coin_pi70_p30_q40"
    truth_pi, truth_p, truth_q, data = data_mgr.load_data(data_file)


    # Create the Gibbs sampler.
    hyp_pi = np.ones(1, int)  # uninformed coin A prior
    hyp_thetas = np.ones(2, int)  # uninformed coin B and C priors
    sampler = ThreeCoinGibbsSampler(data)

    # Use the sampler to estimate the document labels.
    estimate_pi, estimate_p, estimate_q = sampler.estimate_variables(20, 5, 2)
    print("\nEstimated pi\n%s" % estimate_pi)
    print("\nEstimated p\n%s" % estimate_p)
    print("\nEstimated q\n%s" % estimate_q)
