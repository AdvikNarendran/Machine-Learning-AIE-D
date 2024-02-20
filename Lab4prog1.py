import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file_path = "C:\\Users\\Advik Narendran\\ml project\\patches_gabor_15816_1 3.csv"
df = pd.read_csv(excel_file_path)

bad=df[df['class'] == 'bad']
bad=bad.drop("ImageName", axis="columns")
bad=bad.drop("class",axis="columns")

med=df[df['class'] == 'medium']
med=med.drop("ImageName", axis="columns")
med=med.drop("class",axis="columns")
print(bad)

bmean=np.mean(bad,axis=0)
bstd=np.std(bad,axis=0)

mmean=np.mean(med,axis=0)
mstd=np.std(med,axis=0)

id=np.linalg.norm(bmean-mmean)
print(id)
selected_feature = bad['MeanAmplitude_0_1']
plt.hist(selected_feature, bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.title('Histogram for Selected Feature')
plt.xlabel('Feature Values')
plt.ylabel('Frequency')
plt.show()

