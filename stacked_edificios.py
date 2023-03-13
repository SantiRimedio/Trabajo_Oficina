
import matplotlib.pyplot as plt
from limpieza_2022 import df
from matplotlib import rcParams
import matplotlib.patches as mpatches

rcParams['font.family'] = 'Gotham Rounded'


for i in range(1,5):
    x = 0
    trimestre = df[df["TRIMESTRE"] == i]
    for j, k in zip(["1","3"], range(0,4)):
        print(j)
        obra = trimestre[trimestre["TIPO_OBRA"] == j]
        color = ["#29BDEF","#EC607E"]
        bar = plt.bar(i, len(obra), bottom=x, color=color[k],zorder=1)
        #list.append(b)
        ax = plt.gca()
        ax.bar_label(bar,label_type='center', color="white",zorder=3, fontsize="xx-large")
        #print(ax.patch)
        x = len(obra) + x
ax = plt.gca()
#print(ax.patch)

plt.xticks([1,2,3,4],["Primer \n trimestre","Segundo \n trimestre","Tercer \n trimestre","Cuarto \n trimestre"])
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for a in [1,3,5,7]:
    b = ax.patches[a]
    print(b)
    w,h = b.get_width(), b.get_height()
    x, y = b.xy
    # top left vertex
    x2, y2 = x, y+h
    #print(x2,y2)
    # top right vertex
    x3, y3 = x+w,y+h
   # print(x3,y3)
    z = y + h - 120
    q = ((y+h-50)//120)
    for i in range(q):

        rectangle = plt.Rectangle((x+0.1,z), 0.25, 90, fc='whitesmoke', alpha=0.5,zorder=1.5)
        plt.gca().add_patch(rectangle)
        rectangle = plt.Rectangle((x+0.45,z), 0.25, 90, fc='whitesmoke', alpha=0.5, zorder=1.5)
        plt.gca().add_patch(rectangle)
        z = z-120


patch_1 = mpatches.Patch(color=color[0], label='Obra Nueva')
patch_2 = mpatches.Patch(color=color[1], label='Demolición')


plt.legend(handles=[patch_1,patch_2],frameon=False, loc="center left", bbox_to_anchor=(1.04,0.5))
plt.tight_layout()
plt.savefig("Edificios")