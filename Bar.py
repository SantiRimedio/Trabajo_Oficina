import matplotlib.pyplot as plt
from Geopandas import df1
import numpy as np
from matplotlib import cm
import matplotlib
from cmap_gcba import cmap_gcba,cmap_gcba_2_r
import matplotlib.font_manager as font_manager
from matplotlib import rcParams
from matplotlib import style
# Set font family globally
rcParams['font.family'] = 'Gotham Rounded'



df1 = df1.sort_values(by="SUP_KM", ascending=True)
plt.figure(figsize=(40,20))
ax = plt.gca()
cmap= cmap_gcba_2_r
# create normalization instance
norm = matplotlib.colors.Normalize(vmin=df1["SUP_KM"].min(), vmax=df1["SUP_KM"].max())
# create a scalarmappable from the colormap
sm = matplotlib.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
bars = plt.bar(df1["BARRIO"],df1["SUP_KM"],width=0.8, color=sm.to_rgba(df1["SUP_KM"]))
#plt.show()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
#ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['bottom'].set_linewidth(2)
ax.axhline(y=df1["SUP_KM"].mean(),lw=2, color="red", label="Promedio")
plt.text(0,210,"Promedio", color="red", fontsize=15,fontweight="bold")
plt.xticks(fontsize=30, fontweight="medium",rotation=45, horizontalalignment='right')
plt.yticks(fontsize=35, fontweight="bold")
plt.tick_params(left = False)
plt.grid(axis="y",color='lightgrey', linestyle='dashed', linewidth=2)
cbar = plt.colorbar(sm,location="right", pad=0.00, drawedges=False)
cbar.set_ticks([])
plt.tight_layout()
plt.savefig("BarrasV", dpi=300)