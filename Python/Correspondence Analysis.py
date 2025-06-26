import mca
import matplotlib.pyplot as plot
import pandas as pd

## ルート設定 ##########
Root_Dir = "C:/Users/fuu_m/OneDrive/NRIコンペ2021/"


# データ読込 ##########
character = pd.read_csv(Root_Dir + "04_document/corres_5.2.csv", index_col=0)

mca_counts = mca.MCA(character)
rows = mca_counts.fs_r(N=2)
cols = mca_counts.fs_c(N=2)

plot.scatter(rows[:,0], rows[:,1], c='b',marker='o')
labels = character.index
for label,x,y in zip(labels,rows[:,0],rows[:,1]):
    plot.annotate(label,xy = (x, y))

plot.scatter(cols[:,0], cols[:,1], c='r',marker='x')
labels = character.columns
for label,x,y in zip(labels,cols[:,0],cols[:,1]):
    plot.annotate(label,xy = (x, y))

plot.show()

# 寄与率の確認
print(mca_counts.L)

# 2軸での寄与率
print(mca_counts.L[0]+mca_counts.L[1])


