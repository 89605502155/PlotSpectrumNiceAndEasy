from MetrPlot import MetrPlot
import matplotlib.pyplot as plt
import matplotlib as mpl
import math
from decimal import Decimal
import numpy as np

class PlotSpectrumNiceAndEasy(MetrPlot):
    def __init__(self, lw=5, sc_x="linear",sc_y="linear", name_plot=None, x_name="X", y_name="Y",save_name="Plot",x_s=12,y_s=10,
                    y_l_s=20,x_l_s=20):
        self.lw = lw
        self.sc_x = sc_x
        self.sc_y = sc_y
        self.name_plot = name_plot
        self.x_name = x_name
        self.y_name = y_name
        self.save_name = save_name
        self.x_s = x_s
        self.y_s = y_s
        self.y_l_s = y_l_s
        self.x_l_s = x_l_s

    def main(self, x, y,save=False, **kwargs):
        mpl.rc('font',family='Times New Roman')
        fig, axs = plt.subplots(figsize=(self.x_s, self.y_s))
        plt.xscale(self.sc_x)
        plt.yscale(self.sc_y)
        axs.plot(x, y, "-", color="blue", lw=self.lw)
        
        for key, value in kwargs.items():
            axs.plot(value[:2], value[2:4], "-", color=value[4], lw=self.lw,label=key)
        x_copy=self.logger(x, self.sc_x)
        y_copy=self.logger(y, self.sc_y)
        
        
        lis_x, lis_x_num = self.ax(x_copy)
        lis_y, lis_y_num = self.ax(y_copy)

        y_pr=self.pr_axes(lis_y_num,self.sc_y)
        x_pr=self.pr_axes(lis_x_num,self.sc_x)

        axs.set_ylim(ymin=y_pr[0],ymax=y_pr[1])
        axs.set_xlim(xmin=x_pr[0],xmax=x_pr[1])

        lis_x, lis_x_num =self.format_lab_ax(lis_x, lis_x_num, self.sc_x)
        lis_y, lis_y_num =self.format_lab_ax(lis_y, lis_y_num, self.sc_y)

        axs.set_xticks(lis_x_num)
        axs.set_yticks(lis_y_num)

        axs.set_ylabel(self.y_name, fontsize=25, labelpad=8)
        axs.grid(color="black", linewidth=0.7)
        axs.set_xlabel(self.x_name, fontsize=25, labelpad=10)
        axs.set_title(self.name_plot, fontsize=28, loc="center", pad=15)
        axs.tick_params(which='major', length=10, width=2)

        axs.set_xticklabels(lis_x, fontsize=self.x_l_s)
        axs.set_yticklabels(lis_y, fontsize=self.y_l_s)

        axs.get_xaxis().set_tick_params(direction='in')
        axs.get_yaxis().set_tick_params(direction='in')

        if save:
            plt.savefig(self.save_name+'.png', format='png', dpi=300)
            plt.savefig(self.save_name+".svg", format="svg")
        plt.show()
        return 0
