#!/usr/bin/env python3
"""Matplotlib template generated automatically with 
/Users/gsalam/scripts/mptemplate.py view-qed-effects.py
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from   matplotlib.backends.backend_pdf import PdfPages
from   matplotlib.ticker import ScalarFormatter
from   matplotlib.ticker import FuncFormatter
from   matplotlib import cycler
from   matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np
import copy
import hfile as h

styles = [
    {'color':'#f00000'},
    {'color':'#0000e0'},
    {'color':'#00c000'},
    {'color':'#404040'},
    {'color':'#e0a040'},
    ]
colors = cycler('color', [style['color'] for style in styles])
# see options for things to set with 
#     python -c "import matplotlib as mpl; print(mpl.rcParams)"
plt.rc('axes', prop_cycle=colors)
mpl.rcParams.update({"axes.grid" : True, "grid.linestyle": ":"})
plt.rc('figure', figsize=(5,3))

pdf_names = [["NNPDF31_nnlo_as_0118_luxqed","NNPDF31_nnlo_as_0118" ],
             ["NNPDF40_nnlo_as_01180_qed","NNPDF40_nnlo_as_01180" ],
             ["MSHT20qed_nnlo","MSHT20nnlo_as118"],
             ]

flavs=[22,-5,-4,-3,-2,-1,21,1,2,3,4,5]
flav_names=["γ",'bbar','cbar','sbar','ubar','dbar','g','d','u','s','c','b']

def main(pdf):

    # loop over all elements in pdf_names list (both levels)
    result = {}
    for row in pdf_names:
        for pdf_name in row:
            result[pdf_name] = h.get_array(f"pdf-files/{pdf_name}-Q100.dat")

    # enumerate flavs
    for iflav,flav in enumerate(flavs):
        fig,(ax0,ax1) = plt.subplots(nrows=2,figsize=(5,6),sharex=True)
        ax1.set_xlabel(r'$x$')
        ax0.set_yscale('log')
        ax0.set_xscale('log')
        ax1.set_xscale('log')
        ax1.set_ylim(0.95,1.05)
        ax0.set_title(rf"Flavour = {flav_names[iflav]}")
        ax0.set_ylabel(rf'$f_{{{flav_names[iflav]}}}(x)$')
        ax1.yaxis.set_minor_locator(MultipleLocator(0.01))
        for pdf_row in pdf_names:
            print(flav,pdf_row)
            #ax.plot(result[pdf_row[0]][1+iflav,:], result[pdf_row[0]][1+iflav,:]/result[pdf_row[1]][1+iflav,:], label=pdf_row[1])
            ax0.plot(result[pdf_row[0]][:,0], result[pdf_row[0]][:,1+iflav], label=pdf_row[1])
            if (flav == 22):
                ax1.plot(result[pdf_row[0]][:,0], result[pdf_row[0]][:,1+iflav]/result[pdf_names[0][0]][:,1+iflav], label=pdf_row[1])
                ax1.set_ylabel(rf'ratio to NNPDF31 QED')
            else:
                ax1.set_ylabel(rf'QED/no-QED')
                ax1.plot(result[pdf_row[0]][:,0], result[pdf_row[0]][:,1+iflav]/result[pdf_row[1]][:,1+iflav], label=pdf_row[1])
            #print(result[pdf_row[0]][:,1+iflav])

            #line_and_band(ax,result[pdf_name]['x'],result[pdf_name]['f'+str(flav)],label=pdf_name)
        ax0.legend(loc='upper left')
        pdf.savefig(fig,bbox_inches='tight')
        plt.close()

    # #res = h.get_array_plus_comments("filename",regexp='',columns={'x':1,'y':(3,4)}) 
    # fig,ax = plt.subplots()
    # ax.set_xlabel(r'$x$')
    # ax.set_ylabel(r'$y$')
    # # ax.set_xlim(0,2.5)
    # # ax.xaxis.set_minor_locator(MultipleLocator(0.1))
    # # ax.yaxis.set_minor_locator(MultipleLocator(0.02))
    # # ax.tick_params(top=True,right=True,direction='in',which='both')
    # # ax.set_xscale('log')
    # # ax.xaxis.set_major_formatter(FuncFormatter(h.log_formatter_fn))
    # # ax.grid(True,ls=":")
    # # ax.set_title("title")
    # # ax.text(x,y,'hello',transform=ax.transAxes)
    # ax.plot(res.x, res.y, label='label', **styles[0])
    # ax.legend(loc='upper left')
    # pdf.savefig(fig,bbox_inches='tight')
    # #pdf.savefig(fig,bbox_inches=Bbox.from_extents(0.0,0.0,7.5,4.8))
    # plt.close()

def line_and_band(ax,x,val_and_err,**extra):
    extra_no_label = copy.copy(extra)
    if ('label' in extra_no_label): del extra_no_label['label']
    ax.fill_between(x,
                    val_and_err.value-val_and_err.error,
                    val_and_err.value+val_and_err.error,
                    alpha=0.2,
                    **extra_no_label
                    )
    ax.plot(x,val_and_err.value, **extra)

if __name__ == "__main__": 
    with PdfPages('view-qed-effects.pdf') as pdf: main(pdf)


