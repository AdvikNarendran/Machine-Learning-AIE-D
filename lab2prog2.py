#Write a function to implement k-NN classifier. k is a variable and based on that the count of 
#neighbors should be selected.  


from collections import Counter
import numpy as np

def k_nearest_neighbors(X_train, y_train, x_new, k):
    distances = []
    for x in X_train:
        distance = np.sqrt(np.sum((x_new - x)**2))
        distances.append(distance)
    
    sorted_indices = np.argsort(distances)
    k_nearest_labels = []
    for i in sorted_indices[:k]:
        k_nearest_labels.append(y_train[i])
    
    label_counter = Counter(k_nearest_labels)
    most_common_label = label_counter.most_common(1)[0][0]
    
    return most_common_label

# User input for training set
num_samples = int(input("Enter the number of training samples: "))
num_features = int(input("Enter the number of features: "))

X_train = []
y_train = []
print("Enter training set:")
for j in range(num_samples):
    features = []
    for i in range(num_features):
        feature = float(input(f"Enter feature {i + 1} for sample {j + 1}: "))
        features.append(feature)
    label = int(input(f"Enter label for sample {j + 1} (0 or 1): "))
    X_train.append(features)
    y_train.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)

# User input for new data point and k
x_new = []
for i in range(num_features):
    feature = float(input(f"Enter feature {i + 1} of the new data point: "))
    x_new.append(feature)

k = int(input("Enter the value of k: "))

# Get the predicted label
predicted_label = k_nearest_neighbors(X_train, y_train, np.array(x_new), k)

print(f"The predicted label for the new data point is: {predicted_label}")
