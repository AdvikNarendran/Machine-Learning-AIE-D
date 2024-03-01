from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
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



# A1. Calculate intraclass spread and interclass distances
centroid_bad = np.mean(bad, axis=0)
std_bad = np.std(bad, axis=0)

centroid_med = np.mean(med, axis=0)
std_med = np.std(med, axis=0)

intraclass_spread_bad = std_bad
intraclass_spread_med = std_med

interclass_distance = np.linalg.norm(centroid_bad - centroid_med)
print("Intraclass Spread (Bad):", intraclass_spread_bad)
print("Intraclass Spread (Medium):", intraclass_spread_med)
print("Interclass Distance:", interclass_distance)

# A2. Histogram for a selected feature
selected_feature = bad['MeanAmplitude_0_1']
mean_feature = np.mean(selected_feature)
variance_feature = np.var(selected_feature)

plt.hist(selected_feature, bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.title('Histogram for Selected Feature')
plt.xlabel('Feature Values')
plt.ylabel('Frequency')
plt.show()

print("Mean of Selected Feature:", mean_feature)
print("Variance of Selected Feature:", variance_feature)

# A3. Minkowski distance with r from 1 to 10 for two feature vectors
feature_vector_1 = bad.iloc[0, :]
feature_vector_2 = bad.iloc[1, :]

minkowski_distances = []
for r in range(1, 11):
    distance = np.linalg.norm(feature_vector_1 - feature_vector_2, ord=r)
    minkowski_distances.append(distance)

plt.plot(range(1, 11), minkowski_distances, marker='o')
plt.title('Minkowski Distance vs r')
plt.xlabel('r')
plt.ylabel('Minkowski Distance')
plt.show()

# A4. Divide dataset into train & test sets
X = df.drop(['ImageName', 'class'], axis=1)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
X_train = np.ascontiguousarray(X_train)
X_test = np.ascontiguousarray(X_test)


# A5. Train a kNN classifier (k=3)
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)

# A6. Test the accuracy of the kNN
accuracy = neigh.score(X_test, y_test)
print("Accuracy of kNN (k=3):", accuracy)

# A7. Use the predict() function to study the prediction behavior
predictions = neigh.predict(X_test)

# A8. Make k=1 to implement NN classifier and compare the results
accuracies = []
for k in range(1, 12):
    neigh_k = KNeighborsClassifier(n_neighbors=k)
    neigh_k.fit(X_train, y_train)
    accuracy_k = neigh_k.score(X_test, y_test)
    accuracies.append(accuracy_k)

plt.plot(range(1, 12), accuracies, marker='o')
plt.title('Accuracy vs k')
plt.xlabel('k')
plt.ylabel('Accuracy')
plt.show()

# A9. Evaluate confusion matrix and performance metrics
conf_matrix = confusion_matrix(y_test, predictions)
precision = precision_score(y_test, predictions, average='weighted')
recall = recall_score(y_test, predictions, average='weighted')
f1 = f1_score(y_test, predictions, average='weighted')

print("Confusion Matrix:\n", conf_matrix)
print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1)
