import glob
import json
import os
import scipy
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
import operator
from matplotlib import cm
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import LinearLocator, FormatStrFormatter


class DataPlot:

    def __init__(self):
        self.init_plotting()
        pass

    def init_plotting(self):
        plt.rcParams['figure.figsize'] = (6.5, 5)
        plt.rcParams['font.size'] = 15
        #plt.rcParams['font.family'] = 'Times New Roman'
        plt.rcParams['axes.labelsize'] = plt.rcParams['font.size']
        plt.rcParams['axes.titlesize'] = 20
        plt.rcParams['legend.fontsize'] = 13
        plt.rcParams['xtick.labelsize'] = plt.rcParams['font.size']
        plt.rcParams['ytick.labelsize'] = plt.rcParams['font.size']
        plt.rcParams['savefig.dpi'] = plt.rcParams['savefig.dpi']
        plt.rcParams['xtick.major.size'] = 3
        plt.rcParams['xtick.minor.size'] = 3
        plt.rcParams['xtick.major.width'] = 1
        plt.rcParams['xtick.minor.width'] = 1
        plt.rcParams['ytick.major.size'] = 3
        plt.rcParams['ytick.minor.size'] = 3
        plt.rcParams['ytick.major.width'] = 1
        plt.rcParams['ytick.minor.width'] = 1
        #plt.rcParams['legend.frameon'] = True
        #plt.rcParams['legend.loc'] = 'center left'
        #plt.rcParams['legend.loc'] = 'center left'
        plt.rcParams['axes.linewidth'] = 2

        #plt.gca().spines['right'].set_color('none')
        #plt.gca().spines['top'].set_color('none')
        #plt.gca().xaxis.set_ticks_position('bottom')
        #plt.gca().yaxis.set_ticks_position('left')

    def exp_mae(self):


        Y_em = [0.0008, 0.0012, 0.0012, 0.0014, 0.001, 0.001, 0.0017, 0.0015, 0.001, 0.001]
        Y_em = [i * 1000 for i in Y_em]

        Y_gibbs = [0.0036, 0.0032, 0.0018, 0.0016, 0.0021, 0.0017, 0.0018, 0.002, 0.0007, 0.0008]
        Y_gibbs = [i * 1000 for i in Y_gibbs]

        # x = [i*0.05 for i in range(2, 25)]
        x = [i for i in range(1, len(Y_em) + 1)]
        # plt.xticks(x, xticks)
        # begin subplots region
        # plt.subplot(121)
        plt.gca().margins(0.1, 0.1)
        ms = 7
        plt.plot(x, Y_em, linestyle='--', marker='s', markersize=ms, linewidth=3, color='#5461AA', label='EM')
        plt.plot(x, Y_gibbs, linestyle='--', marker='o', markersize=ms, linewidth=3, color='red', label='Gibbs Sampling')


        plt.xlabel(u'Data Size (K)')
        plt.ylabel(r'Mean absolute error ($\times 10^{-3}$)')

        # plt.xlim(1,len(Y_residual)+1)
        #plt.title(u'Subspace-Accuracy/NMI')

        # plt.yaxis.grid(color='gray', linestyle='dashed')

        #plt.gca().legend(bbox_to_anchor=(0.99, 0.99))
        #plt.gca().legend(bbox_to_anchor=(0.349, 1.005))
        #plt.gca().legend(loc = 'upper center', ncol=3)
        leg = plt.gca().legend(loc='upper right')
        leg.get_frame().set_alpha(0.5)
        #plt.yscale('log')
        plt.ylim(0.0, 7)

        plt.show()

    def exp_mape(self):


        Y_em = [0.293, 0.2891, 0.347, 0.4423, 0.3654, 0.3839, 0.6997, 0.5042, 0.315, 0.2084]
        Y_gibbs = [1.3435, 0.6611, 0.3432, 0.4666, 0.7708, 0.5685, 0.5541, 0.5714, 0.2042, 0.1701]

        # x = [i*0.05 for i in range(2, 25)]
        x = [i for i in range(1, len(Y_em) + 1)]
        # plt.xticks(x, xticks)
        # begin subplots region
        # plt.subplot(121)
        plt.gca().margins(0.1, 0.1)
        ms = 7
        plt.plot(x, Y_em, linestyle='--', marker='s', markersize=ms, linewidth=3, color='#5461AA', label='EM')
        plt.plot(x, Y_gibbs, linestyle='--', marker='o', markersize=ms, linewidth=3, color='red', label='Gibbs Sampling')


        plt.xlabel(u'Data Size (K)')
        plt.ylabel(r'Mean absolute percentage error')

        # plt.xlim(1,len(Y_residual)+1)
        #plt.title(u'Subspace-Accuracy/NMI')

        # plt.yaxis.grid(color='gray', linestyle='dashed')

        #plt.gca().legend(bbox_to_anchor=(0.99, 0.99))
        #plt.gca().legend(bbox_to_anchor=(0.349, 1.005))
        #plt.gca().legend(loc = 'upper center', ncol=3)
        leg = plt.gca().legend(loc='upper right')
        leg.get_frame().set_alpha(0.5)
        #plt.yscale('log')
        plt.ylim(0.0, 2.5)

        plt.show()

    def exp_runtime(self):


        Y_em = [0.0366, 0.0445, 0.0528, 0.0616, 0.071, 0.0799, 0.0884, 0.0984, 0.1058, 0.116]
        Y_gibbs = [0.2588, 0.5524, 0.8896, 1.2732, 1.7458, 2.2703, 2.8405, 3.5028, 4.1835, 5.0255]

        # x = [i*0.05 for i in range(2, 25)]
        x = [i for i in range(1, len(Y_em) + 1)]
        # plt.xticks(x, xticks)
        # begin subplots region
        # plt.subplot(121)
        plt.gca().margins(0.1, 0.1)
        ms = 7
        plt.plot(x, Y_em, linestyle='--', marker='s', markersize=ms, linewidth=3, color='#5461AA', label='EM')
        plt.plot(x, Y_gibbs, linestyle='--', marker='o', markersize=ms, linewidth=3, color='red', label='Gibbs Sampling')


        plt.xlabel(u'Data Size (K)')
        plt.ylabel(r'Runing time (s)')

        # plt.xlim(1,len(Y_residual)+1)
        #plt.title(u'Subspace-Accuracy/NMI')

        # plt.yaxis.grid(color='gray', linestyle='dashed')

        #plt.gca().legend(bbox_to_anchor=(0.99, 0.99))
        #plt.gca().legend(bbox_to_anchor=(0.349, 1.005))
        #plt.gca().legend(loc = 'upper center', ncol=3)
        leg = plt.gca().legend(loc='upper right')
        leg.get_frame().set_alpha(0.5)
        #plt.yscale('log')
        plt.ylim(0.0, 7)

        plt.show()


if __name__ == '__main__':

    data_plot = DataPlot()

    ''' mae'''
    data_plot.exp_mae()

    ''' mape '''
    data_plot.exp_mape()

    ''' runtime '''
    data_plot.exp_runtime()
