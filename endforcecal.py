import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
# Zoom region inset axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Global
plt.rcParams['font.size'] = 8
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['figure.dpi'] = 300
#plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.constrained_layout.use'] = True

#
fig = plt.figure()

# figure size
fixed_width_mm = 80
fixed_height_mm = 54
fixed_width_inch = fixed_width_mm / 25.4
fixed_height_inch = fixed_height_mm / 25.4
fig.set_size_inches(fixed_width_inch, fixed_height_inch)

# Import data
data1 = pd.read_csv('Force_l.csv')
data2 = pd.read_csv('Force_r.csv')
data3 = pd.read_csv('Force_DF.csv')
x = data1['Time [s]']
y1 = data1['Force1.Force_x [newton]']
y2 = data2['Force1.Force_x [newton]']
y3 = data3['Force1.Force_x [newton]']
y12 = y1 + y2

# Add subplot
ax = fig.add_subplot(111)
# curve
ax.plot(x, y1, color = 'b', label = '$F_l$', linewidth = 2)
ax.plot(x, y2, color = 'g', label = '$F_r$', linewidth = 2)
ax.plot(x, y3, color = 'r', label = '$F_{DF}$', linewidth = 2)
ax.plot(x, y12, color = 'c', label = '$F_{l+r}$', linewidth = 1, linestyle = 'dotted', marker = 'x', markersize = 2)
# axis
ax.set_xlim(x[0], x[len(x)-1])
ax.set_ylim(0, 70)
ax.set_xticks(np.linspace(x[0], x[len(x)-1], 5),['0','8','16','24','32'])
ax.set_yticks(np.linspace(-70, 70, 5),['-70','-35','0','35','70'])
ax.set_xlabel('Time (s)')
ax.set_ylabel('Force (N)')
ax.grid(True, linestyle = '--', linewidth = 0.5, color = 'gray')
ax.legend(fontsize = 8)

#
plt.show()