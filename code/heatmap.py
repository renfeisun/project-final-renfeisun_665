import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv
import datetime
import sys

data = [np.zeros((24,7)) for i in range(5)]

f = sys.argv[1]
with open(f, 'r') as fr:
    fr.readline()
    for line in fr:
        line = line.strip().split(',')
        row = col =index = 0
        for i, item in enumerate(line):
            item = item.replace('"', '').strip()
            if i == 0:
                item = datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S')
                col = item.weekday()
                row = item.hour
                index = item.month - 1
            elif i == 1:
                value = int(item)
            else:
                
                data[index][23-row][col] += value
                break
row = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
col = [str(23-i) for i in range(24)]

fig, (ax, ax2, ax3, ax4, ax5) = plt.subplots(1, 5, figsize=(20, 24))
cbar_kw={} 
cbarlabel = "Applicances"
im = ax.imshow(data[0])
cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
ax.set_xticks(np.arange(len(row)))
ax.set_yticks(np.arange(len(col)))
ax.set_xticklabels(row, fontsize=16)
ax.set_yticklabels(col, fontsize=16)
ax.set_title("January Appliances")
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

im = ax2.imshow(data[1])
cbar = ax2.figure.colorbar(im, ax=ax2, **cbar_kw)
cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
ax2.set_xticks(np.arange(len(row)))
ax2.set_yticks(np.arange(len(col)))
ax2.set_xticklabels(row, fontsize=16)
ax2.set_yticklabels(col, fontsize=16)
ax2.set_title("February Appliances")
plt.setp(ax2.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

im = ax3.imshow(data[2])
cbar = ax3.figure.colorbar(im, ax=ax3, **cbar_kw)
cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
ax3.set_xticks(np.arange(len(row)))
ax3.set_yticks(np.arange(len(col)))
ax3.set_xticklabels(row, fontsize=16)
ax3.set_yticklabels(col, fontsize=16)
ax3.set_title("March Appliances")
plt.setp(ax3.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

im = ax4.imshow(data[3])
cbar = ax4.figure.colorbar(im, ax=ax4, **cbar_kw)
cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
ax4.set_xticks(np.arange(len(row)))
ax4.set_yticks(np.arange(len(col)))
ax4.set_xticklabels(row, fontsize=16)
ax4.set_yticklabels(col, fontsize=16)
ax4.set_title("April Appliances")
plt.setp(ax4.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

im = ax5.imshow(data[4])
cbar = ax5.figure.colorbar(im, ax=ax5, **cbar_kw)
cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
ax5.set_xticks(np.arange(len(row)))
ax5.set_yticks(np.arange(len(col)))
ax5.set_xticklabels(row, fontsize=16)
ax5.set_yticklabels(col, fontsize=16)
ax5.set_title("May Appliances")
plt.setp(ax5.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

plt.tight_layout()
plt.savefig(r"figure_1.png")

