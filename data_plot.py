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

    def draw_beta_recovery_cr(self, result_dir, k, p, fr, bNoise):

        if bNoise:
            noise_str = ""
        else:
            noise_str = "_nn"

        recovery_file = result_dir + 'beta-cr_' + str(k) + 'K_' + 'p' + str(p) + '_fr' + str(fr) + noise_str + '.mat'
        mat_contents = scipy.io.loadmat(recovery_file)

        Y_Graft = mat_contents["Graft_result"][0].tolist()
        Y_OS = mat_contents["OS_result"][0].tolist()
        Y_Homotopy = mat_contents["Homotopy_result"][0].tolist()
        Y_DALM = mat_contents["DALM_result"][0].tolist()
        Y_TORRENT = mat_contents["TORRENT_result"][0].tolist()
        Y_RLHH = mat_contents["RLHH_result"][0].tolist()
        Y_RoOFS = mat_contents["RoOFS_result"][0].tolist()

        # x = [i*0.05 for i in range(2, 25)]
        x = [i*0.05 for i in range(1, len(Y_RoOFS) + 1)]
        # plt.xticks(x, xticks)
        # begin subplots region
        # plt.subplot(121)
        plt.gca().margins(0.1, 0.1)
        ms = 7
        plt.plot(x, Y_Graft, linestyle='--', marker='d', markersize=ms, linewidth=3, color='#5461AA', label='Graft')
        plt.plot(x, Y_OS, linestyle='--', marker='o', markersize=ms, linewidth=3, color='green', label='OS')
        plt.plot(x, Y_Homotopy, linestyle='-.', marker='v', markersize=ms, linewidth=3, color='blue', label='Homotopy')
        plt.plot(x, Y_DALM, linestyle='-.', marker='<', markersize=ms, linewidth=3, color='#F27441', label='DALM')
        plt.plot(x, Y_TORRENT, linestyle='--', marker='s', markersize=ms, linewidth=3, color='#BD90D4', label='TORRENT')
        plt.plot(x, Y_RLHH, linestyle=':', marker='^', markersize=ms, linewidth=3, color='cyan', label='RLHH')
        plt.plot(x, Y_RoOFS, linestyle='-', marker='o', markersize=ms, linewidth=3, color='red', label='RoOFS')

        plt.xlabel(u'Corruption Ratio')
        plt.ylabel(r'$\|\beta - \beta^*\|_2$')

        # plt.xlim(1,len(Y_residual)+1)
        #plt.title(u'Subspace-Accuracy/NMI')

        # plt.yaxis.grid(color='gray', linestyle='dashed')

        #plt.gca().legend(bbox_to_anchor=(0.99, 0.99))
        #plt.gca().legend(bbox_to_anchor=(0.349, 1.005))
        #plt.gca().legend(loc = 'upper center', ncol=3)
        leg = plt.gca().legend(loc='upper left')
        leg.get_frame().set_alpha(0.5)
        #plt.yscale('log')

        '''
        if b == 10 and k == 5 and p == 100 and bNoise == 1:
            plt.ylim(0.0, 0.5)
        elif b == 10 and k == 10 and p == 100 and bNoise == 1:
            plt.ylim(0.0, 0.4)
        elif b == 10 and k == 10 and p == 400 and bNoise == 1:
            plt.ylim(0.0, 0.5)  # used for 4K
        elif b == 10 and k == 1 and p == 200 and bNoise == 1:
            plt.ylim(0.15, 0.45)
        elif b == 10 and k == 2 and p == 200 and bNoise == 1:
            plt.ylim(0.1, 0.45)
        elif b == 10 and k == 2 and p == 200 and bNoise == 0:
            plt.ylim(-0.02, 0.45)
        elif b == 10 and k == 4 and p == 400 and bNoise == 0:
            plt.ylim(-0.05, 1.95)
        '''
        plt.show()

        #pp = PdfPages("D:/Dropbox/PHD/publications/IJCAI2017_RLHH/images/beta_1.pdf")
        #plt.savefig(pp, format='pdf')
        #plt.close()

    def draw_beta_recovery_fr(self, result_dir, k, p, cr, bNoise):

        if bNoise:
            noise_str = ""
        else:
            noise_str = "_nn"

        recovery_file = result_dir + 'beta-fr_' + str(k) + 'K_' + 'p' + str(p) + '_cr' + str(cr) + noise_str + '.mat'
        mat_contents = scipy.io.loadmat(recovery_file)

        Y_Graft = mat_contents["Graft_result"][0].tolist()
        Y_OS = mat_contents["OS_result"][0].tolist()
        Y_Homotopy = mat_contents["Homotopy_result"][0].tolist()
        Y_DALM = mat_contents["DALM_result"][0].tolist()
        Y_TORRENT = mat_contents["TORRENT_result"][0].tolist()
        Y_RLHH = mat_contents["RLHH_result"][0].tolist()
        Y_RoOFS = mat_contents["RoOFS_result"][0].tolist()

        # x = [i*0.05 for i in range(2, 25)]
        x = [0.1*i for i in range(1, len(Y_RoOFS) + 1)]
        # plt.xticks(x, xticks)
        # begin subplots region
        # plt.subplot(121)
        plt.gca().margins(0.1, 0.1)
        ms = 7
        plt.plot(x, Y_Graft, linestyle='--', marker='d', markersize=ms, linewidth=3, color='#5461AA', label='Graft')
        plt.plot(x, Y_OS, linestyle='--', marker='o', markersize=ms, linewidth=3, color='green', label='OS')
        plt.plot(x, Y_Homotopy, linestyle='-.', marker='v', markersize=ms, linewidth=3, color='blue', label='Homotopy')
        plt.plot(x, Y_DALM, linestyle='-.', marker='<', markersize=ms, linewidth=3, color='#F27441', label='DALM')
        plt.plot(x, Y_TORRENT, linestyle='--', marker='s', markersize=ms, linewidth=3, color='#BD90D4', label='TORRENT')
        plt.plot(x, Y_RLHH, linestyle=':', marker='^', markersize=ms, linewidth=3, color='cyan', label='RLHH')
        plt.plot(x, Y_RoOFS, linestyle='-', marker='o', markersize=ms, linewidth=3, color='red',
                 label='RoOFS')


        plt.xlabel(u'Feature Ratio')
        plt.ylabel(r'$\|\beta - \beta^*\|_2$')

        # plt.xlim(1,len(Y_residual)+1)
        #plt.title(u'Subspace-Accuracy/NMI')

        # plt.yaxis.grid(color='gray', linestyle='dashed')

        #plt.gca().legend(bbox_to_anchor=(0.99, 0.99))
        #plt.gca().legend(bbox_to_anchor=(0.349, 1.005))
        #plt.gca().legend(loc = 'upper center', ncol=3)
        #plt.gca().legend(loc='upper left')
        leg = plt.gca().legend(loc='upper left')
        leg.get_frame().set_alpha(0.5)

        #plt.yscale('log')

        '''
        if b == 10 and k == 5 and p == 100 and bNoise == 1:
            plt.ylim(0.0, 0.5)
        elif b == 10 and k == 10 and p == 100 and bNoise == 1:
            plt.ylim(0.0, 0.4)
        elif b == 10 and k == 10 and p == 400 and bNoise == 1:
            plt.ylim(0.0, 0.5)  # used for 4K
        elif b == 10 and k == 1 and p == 200 and bNoise == 1:
            plt.ylim(0.15, 0.45)
        elif b == 10 and k == 2 and p == 200 and bNoise == 1:
            plt.ylim(0.1, 0.45)
        elif b == 10 and k == 2 and p == 200 and bNoise == 0:
            plt.ylim(-0.02, 0.45)
        elif b == 10 and k == 4 and p == 400 and bNoise == 0:
            plt.ylim(-0.05, 1.95)
        '''
        plt.show()

        # pp = PdfPages(result_dir + "../beta_1.pdf")
        # plt.savefig(pp, format='pdf')
        # plt.close()

    def draw_runtime_datasize(self, result_dir, fr, cr, p, bNoise):

        if bNoise:
            noise_str = ""
        else:
            noise_str = "_nn"

        runtime_file = result_dir + 'runtime-ds_p' + str(p) + '_fr' + str(int(fr*100)) + '_cr' + str(int(cr*100)) + noise_str + '.mat'
        mat_contents = scipy.io.loadmat(runtime_file)
        Y_Graft = mat_contents["Graft_result"][0].tolist()
        Y_OS = mat_contents["OS_result"][0].tolist()
        Y_Homotopy = mat_contents["Homotopy_result"][0].tolist()
        Y_DALM = mat_contents["DALM_result"][0].tolist()
        Y_TORRENT = mat_contents["TORRENT_result"][0].tolist()
        Y_RLHH = mat_contents["RLHH_result"][0].tolist()
        Y_RoOFS = mat_contents["RoOFS_result"][0].tolist()

        #x = [i*0.05 for i in range(2, 25)]
        x = [i for i in range(1, len(Y_RoOFS) + 1)]
        # plt.xticks(x, xticks)
        # begin subplots region
        # plt.subplot(121)
        plt.gca().margins(0.1, 0.1)
        ms = 7
        plt.plot(x, Y_Graft, linestyle='--', marker='d', markersize=ms, linewidth=3, color='#5461AA', label='Graft')
        plt.plot(x, Y_OS, linestyle='--', marker='o', markersize=ms, linewidth=3, color='green', label='OS')
        plt.plot(x, Y_Homotopy, linestyle='-.', marker='v', markersize=ms, linewidth=3, color='blue', label='Homotopy')
        plt.plot(x, Y_DALM, linestyle='-.', marker='<', markersize=ms, linewidth=3, color='#F27441', label='DALM')
        plt.plot(x, Y_TORRENT, linestyle='--', marker='s', markersize=ms, linewidth=3, color='#BD90D4', label='TORRENT')
        plt.plot(x, Y_RLHH, linestyle=':', marker='^', markersize=ms, linewidth=3, color='cyan', label='RLHH')
        plt.plot(x, Y_RoOFS, linestyle='-', marker='o', markersize=ms, linewidth=3, color='red', label='RoOFS')

        plt.xlabel(u'Data Size (K)')
        plt.ylabel(u'Running Time(s)')

        # plt.xlim(1,len(Y_residual)+1)
        #plt.title(u'Subspace-Accuracy/NMI')

        # plt.yaxis.grid(color='gray', linestyle='dashed')

        leg = plt.gca().legend(loc='upper left')
        #plt.yscale('log')
        leg.get_frame().set_alpha(0.7)

        #plt.ylim(-0.1, 40)
        plt.ylim(-0.1, 500)

        plt.show()

        #pp = PdfPages("D:/Dropbox/PHD/publications/IJCAI2017_RLHH/images/beta_1.pdf")
        #plt.savefig(pp, format='pdf')
        #plt.close()

    def draw_runtime_featnum(self, result_dir, fr, cr, k, bNoise):

        if bNoise:
            noise_str = ""
        else:
            noise_str = "_nn"

        runtime_file = result_dir + 'runtime-fn_k' + str(k) + '_fr' + str(int(fr*100)) + '_cr' + str(int(cr*100)) + noise_str + '.mat'
        mat_contents = scipy.io.loadmat(runtime_file)
        Y_Graft = mat_contents["Graft_result"][0].tolist()
        Y_OS = mat_contents["OS_result"][0].tolist()
        Y_Homotopy = mat_contents["Homotopy_result"][0].tolist()
        Y_DALM = mat_contents["DALM_result"][0].tolist()
        Y_TORRENT = mat_contents["TORRENT_result"][0].tolist()
        Y_RLHH = mat_contents["RLHH_result"][0].tolist()
        Y_RoOFS = mat_contents["RoOFS_result"][0].tolist()

        #x = [i*0.05 for i in range(2, 25)]
        x = [i for i in range(1, len(Y_RoOFS) + 1)]
        # plt.xticks(x, xticks)
        # begin subplots region
        # plt.subplot(121)
        plt.gca().margins(0.1, 0.1)
        ms = 7
        plt.plot(x, Y_Graft, linestyle='--', marker='d', markersize=ms, linewidth=3, color='#5461AA', label='Graft')
        plt.plot(x, Y_OS, linestyle='--', marker='o', markersize=ms, linewidth=3, color='green', label='OS')
        plt.plot(x, Y_Homotopy, linestyle='-.', marker='v', markersize=ms, linewidth=3, color='blue', label='Homotopy')
        plt.plot(x, Y_DALM, linestyle='-.', marker='<', markersize=ms, linewidth=3, color='#F27441', label='DALM')
        plt.plot(x, Y_TORRENT, linestyle='--', marker='s', markersize=ms, linewidth=3, color='#BD90D4', label='TORRENT')
        plt.plot(x, Y_RLHH, linestyle=':', marker='^', markersize=ms, linewidth=3, color='cyan', label='RLHH')
        plt.plot(x, Y_RoOFS, linestyle='-', marker='o', markersize=ms, linewidth=3, color='red', label='RoOFS')

        plt.xlabel(u'Feature Number (K)')
        plt.ylabel(u'Running Time(s)')

        # plt.xlim(1,len(Y_residual)+1)
        #plt.title(u'Subspace-Accuracy/NMI')

        # plt.yaxis.grid(color='gray', linestyle='dashed')

        leg = plt.gca().legend(loc='upper left')
        #plt.yscale('log')
        leg.get_frame().set_alpha(0.7)

        #plt.ylim(-0.1, 40)
        plt.ylim(-0.1, 200)

        plt.show()

    def exp_beta_recovery_cr(self):

        result_dir = '../../../publications/AAAI2018_RoOFS/experiment/'

        ''' beta recovery '''
        # figure 1a:
        p = 2000
        k = 1
        fr = 20
        bNoise = 1
        data_plot.draw_beta_recovery_cr(result_dir, k, p, fr, bNoise)

        ## figure 1b
        p = 4000
        k = 1
        fr =20
        bNoise = 1
        data_plot.draw_beta_recovery_cr(result_dir, k, p, fr, bNoise)

        ## figure 1c
        p = 4000
        k = 2
        fr = 20
        bNoise = 1
        data_plot.draw_beta_recovery_cr(result_dir, k, p, fr, bNoise)

        ## figure 1d
        p = 4000
        k = 1
        fr = 40
        bNoise = 1
        data_plot.draw_beta_recovery_cr(result_dir, k, p, fr, bNoise)

        ## figure 1e
        p = 4000
        k = 1
        fr = 80
        bNoise = 1
        data_plot.draw_beta_recovery_cr(result_dir, k, p, fr, bNoise)

        ## figure 1f
        p = 2000
        k = 1
        fr = 20
        bNoise = 0
        data_plot.draw_beta_recovery_cr(result_dir, k, p, fr, bNoise)

    def exp_beta_recovery_fr(self):

        result_dir = '../../../publications/AAAI2018_RoOFS/experiment/'

        ''' beta recovery '''
        # figure 1a:
        p = 2000
        k = 1
        cr = 20
        bNoise = 1
        data_plot.draw_beta_recovery_fr(result_dir, k, p, cr, bNoise)

        ## figure 1b
        p = 4000
        k = 1
        cr = 20
        bNoise = 1
        data_plot.draw_beta_recovery_fr(result_dir, k, p, cr, bNoise)

        ## figure 1c
        p = 2000
        k = 1
        cr = 40
        bNoise = 1
        data_plot.draw_beta_recovery_fr(result_dir, k, p, cr, bNoise)



    def exp_runtime(self):
        result_dir = '../../../publications/AAAI2018_RoOFS/experiment/'

        ## Figure 4a
        p = 2000
        fr = 0.2
        cr = 0.1
        bNoise = 1
        data_plot.draw_runtime_datasize(result_dir, fr, cr, p, bNoise)

        ## Figure 4b
        k = 1
        fr = 0.2
        cr = 0.1
        bNoise = 1
        data_plot.draw_runtime_featnum(result_dir, fr, cr, k, bNoise)


if __name__ == '__main__':

    data_plot = DataPlot()

    ''' beta recovery cr'''
    #data_plot.exp_beta_recovery_cr()

    ''' beta recovery fr '''
    #data_plot.exp_beta_recovery_fr()

    ''' runtime '''
    data_plot.exp_runtime()
