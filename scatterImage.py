import pandas as pd
import numpy as np

df = pd.read_excel("/study/python/income.xlsx")
print(df.head(10))
fig = df.plot(kind="scatter", x="height", y="income").get_figure()
fig.savefig("/study/scatter.jpg")

url = 'http://s3.amazonaws.com/assets.datacamp.com/course/dasi/present.txt'
present = pd.read_table("/Users/lvsheng/Movies/present.txt", sep=' ')
print(present.shape)

print(present.columns)
print(present.head(63))
present_year = present.set_index('year')
plt = present_year.plot().get_figure()
plt.savefig("/study/present.jpg")
plt = present_year.plot(kind="bar").get_figure()
plt.savefig("/study/present_bar.jpg")
plt = present_year.plot(kind="bar", stacked=True).get_figure()
plt.savefig("/study/present_bar_stacked.jpg")


